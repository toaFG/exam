from odoo import fields, models, api


class EmployeeCertificate(models.Model):
    _name = 'employee.certificate'

    name = fields.Char(string='Name', required=True)
    skill_ids = fields.Many2many('employee.skills', string='Skills')
    validity_start = fields.Date(string='Validity Date')
    validity_end = fields.Date(string='Validity End')
    rate = fields.Float(string='Rate')
    link = fields.Char(string='Link')

    @api.constrains('validity_start', 'validity_end')
    def _check_validity_dates(self):
        for certificate in self:
            if certificate.validity_start and certificate.validity_end:
                if certificate.validity_start > certificate.validity_end:
                    raise models.ValidationError('Validity start date must be before validity end date')

