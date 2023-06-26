# -*- coding: utf-8 -*-
from random import randint

from odoo import models, fields, api, _
import requests

from odoo.exceptions import ValidationError


class MailingContact(models.Model):
    _inherit = 'mailing.contact'

    # Basic
    test_id = fields.Char(string="TEST ID", default=lambda self: str(randint(100000, 999999)))

    # Contact Fields
    age = fields.Integer(string="Age")
    gender = fields.Selection([
        ('male', 'Male'),
        ('female', 'Female'),
        ('other', 'Other')], string="Gender", default='other')
    street = fields.Char()
    city = fields.Char()
    state = fields.Char()
    postcode = fields.Char()

    def import_contact(self):
        response = requests.get(f'https://randomuser.me/api/?results=1')
        data = response.json()
        user = data['results'][0]
        user_country_id = self.env['res.country'].search([('name', '=', user['location']['country'])], limit=1).id

        self.write({
            'name': f"{user['name']['first']} {user['name']['last']}",
            'age': user['registered']['age'] + 18,
            'gender': user['gender'],
            'street': user['location']['street']['name'],
            'city': user['location']['city'],
            'state': user['location']['state'],
            'country_id': user_country_id,
            'postcode': user['location']['postcode'],
            'email': user['email'],

        })

    @api.constrains('email')
    def _check_unique_email(self):
        for contact in self:
            if self.search_count([('email', '=', contact.email)]) > 1:
                raise ValidationError("Contact with the same email already exists!")

    @api.model
    def delete_all_contacts(self):
        if self.env['mailing.contact'].search_count([]) > 0:
            print("\n\tDeleting all contacts... Possibly\n")
            self.env['mailing.contact'].search([]).unlink()



