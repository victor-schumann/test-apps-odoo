import base64
import requests
from randomuser import RandomUser

from odoo import models, fields, api
from odoo.exceptions import ValidationError


def _encode_image(image_url):
    try:
        response = requests.get(image_url)
        response.raise_for_status()
    except requests.exceptions.HTTPError:
        raise ValidationError('Could not get image from URL')

    image_base64 = base64.b64encode(response.content)
    return image_base64.decode('utf-8')


class MailingList(models.Model):
    _name = 'mailing_list.mailing_list'
    _description = 'Exercise #1 of Task #12'

    partner_name = fields.Many2one('res.partner', string='Name', onchange='_on_partner_name_change')
    partner_id = fields.Many2one('res.partner')
    sequence_id = fields.Many2many('contact_sequences.contact_sequences', string='Mail Lists')

    partner_image = fields.Binary(string='Image', compute='_compute_partner_fields', store=True)
    email = fields.Char(string='Email', store=True)
    zip = fields.Char(string='ZIP', store=True)
    gender = fields.Selection([
        ('male', 'Male'),
        ('female', 'Female'),
        ('undisclosed', 'Undisclosed')], string="Gender", default='undisclosed')

    @api.depends('partner_name')
    def _compute_partner_fields(self):
        print(self)
        print("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!1\n\n")
        for record in self:
            if record.partner_name:
                record.partner_id = record.partner_name.id
                record.email = record.partner_name.email
                record.zip = record.partner_name.zip
                record.partner_image = record.partner_name.image_1920

    def add_to_mail_list(self):
        print('\n\tAdding to mail list (supposedly)...\n')

    def create_contact(self, user):
        partner_vals = {
            'name': user.get_full_name(),
            'email': user.get_email(),
            'zip': user.get_zipcode(),
            'image_1920': _encode_image(user.get_picture()),
        }

        self.write({'gender': user.get_gender()})
        return self.env['res.partner'].create(partner_vals)

    def prepare_and_create_partner_from_api(self, number_of_partners=1):
        partners = self.env['res.partner']

        for record in range(number_of_partners):
            record = self.create_contact(RandomUser())
            partners |= record
        return partners

    @api.depends('partner_name')
    def send_api_request_solo(self):
        for record in self:
            self.partner_name = self.create_contact(RandomUser())

        return {'type': 'ir.actions.client', 'tag': 'reload'}


class ContactSequences(models.Model):
    _name = 'contact_s.contact_s'

    sequence_name = fields.Char(string='Sequence Name')
    contact_ids = fields.Many2many('res.partner', string='Contacts')

    def send_spam(self):
        print('\n\tSending SPAM! (supposedly)...\n')
