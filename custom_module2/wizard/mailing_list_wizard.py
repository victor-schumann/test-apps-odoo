from odoo import models, fields, api
from odoo.fields import Command


class MailingListWizard(models.TransientModel):
    _name = 'mailing_list.wizard'
    _description = 'Exercise #2 of Task #12'

    contacts_to_add = fields.Integer(string='Contacts to add')

    def add_to_mail_list(self):
        # obj_dic_key = self.env.context.get('active_id')

        print(self.env.context)

        print('\n\tAdding to mail list (supposedly)...\n')

        contacts = self.env['mailing_list.mailing_list'].prepare_and_create_partner_from_api(self.contacts_to_add)
        active_record = self.env[self.env.context.get('active_model')].browse(
            self.env.context.get('active_id')).exists()
        if active_record:
            active_record.write({
                'contact_ids': [(6, 0, contacts.ids)]
            })
        print(contacts)
