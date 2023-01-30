from odoo import models, fields,  api
from odoo.tools.translate import _
from odoo import exceptions
from datetime import datetime


class Agreement(models.Model):
    _name = 'agreement'
    _description = 'Agreement'

    number = fields.Char(string='Number', required=True, readonly=True, default=lambda self: _('New'))
    partner_id = fields.Many2one('res.partner', string='Client', required=True)
    kind_id = fields.Many2one('agreement.types', string='Kind Agreement', required=True)
    state = fields.Selection(
        [('draft', 'Draft'), ('in_progress', 'In Progress'), ('active', 'Active'), ('completed', 'Completed')],
        string='State', default='draft', readonly=True, required=True)
    start_date = fields.Date(string="Start Date", required=True)
    end_date = fields.Date(string="End Date", required=True)
    author_id = fields.Many2one('res.users', string='Author', required=True, default=lambda self: self.env.user)


    @api.model
    def create(self, vals):
        if vals.get('number', _('New')) == _('New'):
            vals['number'] = self.env['ir.sequence'].next_by_code('agreement') or _('New')
        res = super(Agreement, self).create(vals)
        return res

    def to_approval(self):
        if self.author_id.id == self.env.user.id:
            self.state = 'in_progress'
        else:
            raise exceptions.ValidationError('You can\'t change status on a contract that you didn\'t create !')
        return True

    def approve(self):
        template = self.env.ref('agreement.mail_template_agreement_mail', raise_if_not_found=False)
        print(template)
        print(self.author_id)
        if template:
            template.send_mail(self.author_id.id, force_send=True)
        self.state = 'active'
        return True

    def to_revision(self):
        self.state = 'draft'
        return True

    def cron_method(self):
        agreements = self.search([
            ('state', '=', 'active'),
            ('end_date', '>=', datetime.today()),
        ])
        if agreements:
            agreements.write({
                "state": 'completed'
            })
