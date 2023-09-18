from odoo import fields , models, api
from odoo.exceptions import  ValidationError, UserError
class Hospital_customers(models.Model):
    _inherit = 'res.partner'

    related_patient_id = fields.Many2one('patient')

    @api.constrains('related_patient_id')
    def valid_email(self):
        for rec in self :
            if rec.email == rec.related_patient_id.email:
                raise ValidationError('This  email  is  assigned to  Customer try another one')
        
    def unlink(self):
        for rec in self :
            if rec.related_patient_id:
                raise UserError('This customer is linked to patient')