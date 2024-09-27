from odoo import fields, models, api
import logging

_logger = logging.getLogger(__name__)

class Employee(models.Model):
    _inherit = 'hr.employee'

    MIN_YEARS_OF_EXPERIENCE = 0
    MAX_YEARS_OF_EXPERIENCE = 30

    th_years_of_experience = fields.Integer(string='Years of Experience',
                                            groups='employee.employee_management_aum_group_employee_manager')

    th_certificate_ids = fields.Many2many('employee.certificate', string='Certificates')
    th_skill_ids = fields.Many2many('employee.skills', string='Skills')

    _sql_constraints = [
        ('check_years_of_experience', 'CHECK(th_years_of_experience >= 0 AND th_years_of_experience <= 30)',
         'Years of experience must be between 0 and 30')
    ]

    @api.model
    def create(self, vals):
        employee = super(Employee, self).create(vals)
        employee._update_skills_from_certificates()
        return employee

    def write(self, vals):
        if 'th_certificate_ids' in vals:
            old_certificates = self.th_certificate_ids
            new_certificates = self.env['employee.certificate'].browse(vals['th_certificate_ids'][0][2])
            removed_certificates = old_certificates - new_certificates

            if removed_certificates:
                self._remove_skills_from_removed_certificates(removed_certificates)

        res = super(Employee, self).write(vals)

        if 'th_certificate_ids' in vals:
            self._update_skills_from_certificates()

        return res

    @api.constrains('th_years_of_experience')
    def _check_experience(self):
        for employee in self:
            if (employee.th_years_of_experience < self.MIN_YEARS_OF_EXPERIENCE
                    or employee.th_years_of_experience > self.MAX_YEARS_OF_EXPERIENCE):
                raise models.ValidationError('Years of experience must be between 0 and 30')

    def _update_skills_from_certificates(self):
        for employee in self:
            certificate_skills = employee.th_certificate_ids.mapped('skill_ids')
            existing_skills = employee.th_skill_ids

            skill_progress_mapping = {}
            for skill in certificate_skills:
                if skill.name not in skill_progress_mapping:
                    skill_progress_mapping[skill.name] = skill.th_level_progress
                else:
                    skill_progress_mapping[skill.name] = max(skill_progress_mapping[skill.name],
                                                             skill.th_level_progress)

            for skill_name, progress in skill_progress_mapping.items():
                employee_skill = existing_skills.filtered(lambda s: s.name == skill_name)
                if employee_skill:
                    employee_skill.th_level_progress = max(employee_skill.th_level_progress, progress)
                else:
                    available_skill = self.env['employee.skills'].search([('name', '=', skill_name)], limit=1)
                    if available_skill:
                        employee.th_skill_ids = [(4, available_skill.id)]
                        available_skill.th_level_progress = max(available_skill.th_level_progress, progress)
                    else:
                        _logger.warning(f"Skill '{skill_name}' not found")

    def _remove_skills_from_removed_certificates(self, removed_certificates):
        for employee in self:
            removed_skills = removed_certificates.mapped('skill_ids')
            remaining_certificates_skills = employee.th_certificate_ids.mapped('skill_ids')

            _logger.info(f"Removed certificates: {[cert.name for cert in removed_certificates]}")
            _logger.info(f"Removed skills: {[skill.name for skill in removed_skills]}")
            _logger.info(f"Remaining certificates: {[cert.name for cert in employee.th_certificate_ids]}")
            _logger.info(f"Remaining skills: {[skill.name for skill in remaining_certificates_skills]}")

            skills_to_remove = removed_skills.filtered(lambda skill: skill not in remaining_certificates_skills)
            _logger.info(f"Skills to remove: {[skill.name for skill in skills_to_remove]}")
            employee.th_skill_ids = [(3, skill.id) for skill in skills_to_remove]