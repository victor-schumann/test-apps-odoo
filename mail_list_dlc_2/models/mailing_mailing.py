# -*- coding: utf-8 -*-

from odoo import models, fields, api


class MailingContact(models.Model):
    _inherit = 'mailing.mailing'

    # Basic
    name2 = fields.Char(string="TEST")


