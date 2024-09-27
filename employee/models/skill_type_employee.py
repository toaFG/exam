from odoo import fields, models, api


class SkillTypes(models.Model):
    _name = 'employee.skills.type'

    name = fields.Char(string='Name', required=True)
    th_skill_ids = fields.One2many('employee.skills', 'th_skill_type_id', string="Skills")
    th_skill_level_ids = fields.One2many('employee.skills.level', 'th_skill_type_id', string="Levels")
