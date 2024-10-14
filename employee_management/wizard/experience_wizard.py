from odoo import models, fields


class SetExperienceWizard(models.TransientModel):
    _name = 'set.experience.wizard'

    year_of_experience = fields.Integer('Years of Experience')
    skills = fields.Many2many('employee.skills', string='Skills')
    certificates = fields.Many2many('employee.certificate', string='Certificates')

    def set_employee_details(self):
        active_ids = self.env.context.get('active_ids', [])
        employees = self.env['hr.employee'].browse(active_ids)

        for employee in employees:
            self._update_employee_experience(employee)
            self._update_employee_skills(employee)
            self._update_employee_certificates(employee)
        return True

    def _update_employee_experience(self, employee):
        if self.year_of_experience:
            employee.write({'th_years_of_experience': self.year_of_experience})

    def _update_employee_skills(self, employee):
        if self.skills:
            employee.write({'th_skill_ids': [(6, 0, self.skills.ids)]})

    def _update_employee_certificates(self, employee):
        if self.certificates:
            employee.write({'th_certificate_ids': [(6, 0, self.certificates.ids)]})
