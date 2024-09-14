from odoo import fields, models, api


class Employee(models.Model):
    _inherit = 'hr.employee'

    MIN_YEARS_OF_EXPERIENCE = 0
    MAX_YEARS_OF_EXPERIENCE = 30

    years_of_experience = fields.Integer(string='Years of Experience', groups='group_employee_manager')
    _sql_constraints = [
        ('check_years_of_experience', 'CHECK(years_of_experience >= 0 AND years_of_experience <= 30)',
         'Years of experience must be between 0 and 30')
    ]

    # @api.constrains('years_of_experience')
    # def _check_experience(self):
    #     for employee in self:
    #         if (employee.years_of_experience < self.MIN_YEARS_OF_EXPERIENCE
    #                 or employee.years_of_experience > self.MAX_YEARS_OF_EXPERIENCE):
    #             raise models.ValidationError('Years of experience Error')

    @api.model
    def create(self, vals):
        if vals.get('years_of_experience') < self.MIN_YEARS_OF_EXPERIENCE or vals.get('years_of_experience') > self.MAX_YEARS_OF_EXPERIENCE:
            raise models.ValidationError('Years of experience Error')
        return super(Employee, self).create(vals)

    def write(self, vals):
        if vals.get('years_of_experience') < self.MIN_YEARS_OF_EXPERIENCE or vals.get('years_of_experience') > self.MAX_YEARS_OF_EXPERIENCE:
            raise models.ValidationError('Years of experience Error')
        return super(Employee, self).write(vals)

