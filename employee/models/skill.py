from odoo import fields, models, api


class EmployeeSkill(models.Model):
    _name = 'employee.skill'

    name = fields.Char(string='Skill Name', required=True)
    skill_rate = fields.Float(string='Skill Rate', required=True)




