from odoo import models, fields, api


class AgreementTypes(models.Model):
    _name = 'agreement.types'
    _description = 'Agreement Types'

    name = fields.Char(string='Name', required=True)
    active = fields.Boolean(string='Active')
