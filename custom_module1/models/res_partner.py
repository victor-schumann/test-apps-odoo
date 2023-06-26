from odoo import models, fields


class ResPartner(models.Model):
    _inherit = 'res.partner'
    message1 = fields.Char(string='Custom Message 1')
    message2 = fields.Char(string='Custom Message 2')