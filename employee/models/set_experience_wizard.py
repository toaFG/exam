from odoo import models, fields

class SetExperienceWizard(models.TransientModel):
    _name = 'set.experience.wizard'

    year_of_experience = fields.Integer('Years of Experience')

    def set_experience(self):
        active_ids = self.env.context.get('active_ids')
        employees = self.env['hr.employee'].browse(active_ids)
        for employee in employees:
            employee.write({'years_of_experience': self.year_of_experience})
        return True