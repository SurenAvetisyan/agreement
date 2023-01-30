from odoo import models, fields, api


class AgreementTypes(models.Model):
    _name = 'agreement.types'
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _description = 'Agreement Types'

    name = fields.Char(string='Name', required=True, tracking=True)
    active = fields.Boolean(string='Active', tracking=True)

    _sql_constraints = [
        ('name_uniq', 'unique (name)', """Only one value can be defined for each given usage!"""),
    ]
