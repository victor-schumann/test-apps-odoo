from random import randint

# -*- coding: utf-8 -*-
import requests
from odoo import models, fields, api


class WizardFile(models.Model):
    _name = 'wizard.file'

    # Basic
    wiz_counter = fields.Integer(string="How many contacts to affect?", default=1)

    # Wizard Action
    def import_contacts(self):
        response = requests.get(f'https://randomuser.me/api/?results={self.wiz_counter}')
        data = response.json()

        for user in data['results']:
            # Perform a search to link the country of the random user with the correct country ID in Odoo
            user_country_id = self.env['res.country'].search([('name', '=', user['location']['country'])], limit=1).id

            while self.env['mailing.contact'].search_count([('email', '=', user['email'])]) > 0:
                print(f"\n\n\tContact with the same email already exists! it is the {user['email']}\n\n")
                unique_response = requests.get(f'https://randomuser.me/api/?results=1')
                user = unique_response.json()['results'][0]

            mailing_contact = self.env['mailing.contact'].create({
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

        return {
            'type': 'ir.actions.client',
            'tag': 'reload',
        }

    def drop_contacts(self):
        contact_count = self.env['mailing.contact'].search_count([])
        if contact_count <= self.wiz_counter:
            contacts_to_drop = self.env['mailing.contact'].search([])
        else:
            contacts_to_drop = self.env['mailing.contact'].search([], limit=self.wiz_counter)

        contacts_to_drop.unlink()

        return {
            'type': 'ir.actions.client',
            'tag': 'reload',
        }

