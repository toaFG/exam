from odoo import fields, models, api


class EmployeeCertificate(models.Model):
    _name = 'employee.certificate'

    name = fields.Char(string='Name', required=True)


