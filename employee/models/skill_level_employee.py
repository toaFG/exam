from odoo import fields, models


class SkillLevels(models.Model):
    _name = 'employee.skills.level'

    th_skill_type_id = fields.Many2one('employee.skills.type', ondelete='cascade')
    name = fields.Char(string='Name', required=True)

