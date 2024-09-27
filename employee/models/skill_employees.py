from odoo import fields, models
from odoo.api import onchange


class EmployeeSkills(models.Model):
    _name = 'employee.skills'

    name = fields.Char(string='Skill Name', required=True)
    th_skill_level_id = fields.Many2one('employee.skills.level', required=False, ondelete='cascade')
    th_skill_type_id = fields.Many2one('employee.skills.type', required=False, ondelete='cascade')
    th_level_progress = fields.Float(string='Progress Level', required=False)

    @onchange('th_skill_level_id')
    def _onchange_th_skill_level_id(self):
        level_mapping = {
            'Advanced Level': 100,
            'Intermediate Level': 70,
            'Basic Level': 40
        }
        self.th_level_progress = level_mapping.get(self.th_skill_level_id.name, 0) if self.th_skill_level_id else 0

    @onchange('th_level_progress')
    def _onchange_th_level_progress(self):
        self.th_level_progress = max(0, min(100, self.th_level_progress))

        level_mapping = [
            (0, 40, 'Basic Level'),
            (40, 70, 'Intermediate Level'),
            (70, 100, 'Advanced Level')
        ]
        for min_prog, max_prog, level_name in level_mapping:
            if min_prog <= self.th_level_progress <= max_prog:
                self.th_skill_level_id = self.env['employee.skills.level'].search([('name', '=', level_name)], limit=1)
                break
