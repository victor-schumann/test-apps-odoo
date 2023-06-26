# -*- coding: utf-8 -*-
import random

from odoo import models, fields, api
from odoo.exceptions import ValidationError


class Car(models.Model):
    _name = 'car.car'
    _description = 'Cars'

    name = fields.Char(string='Name')
    horse_power = fields.Integer(string='Horse Power')
    door_number = fields.Integer(string='Door Number')
    max_speed = fields.Integer(string='Max Speed (MPH)', compute='get_max_speed')
    random_message = fields.Char(string='Custom Message', compute='get_random_message')

    driver_id = fields.Many2one('res.partner', string='Driver')
    parking_id = fields.Many2one('parking.parking', string='Parking')
    feature_ids = fields.Many2many('features.features', string='Features')

    status = fields.Selection([
        ('new', 'New'),
        ('in-use', 'In-Use'),
        ('sold', 'Sold'),
        ('totalled', 'Totalled')
    ], string='Status', default='new')

    car_sequence = fields.Char(string='Sequence')

    @api.model
    def create(self, vals):
        print("\n\tYou are on the method create override")
        print('\tvals', vals)
        print('\tname', vals['name'])
        print('\thorse_power', vals['horse_power'])
        print('\tdoor_number', vals['door_number'])
        print("\tEnd of method create override\n")

        if vals['name'] == 'Tarantino':
            vals['name'] = 'Glass of Milk'

        vals['car_sequence'] = self.env['ir.sequence'].next_by_code('car.sequence')
        result = super(Car, self).create(vals)
        return result

    def write(self, vals):
        print("\n\tYou are on the method write override")
        print("\tEnd of method write override\n")

        horse_power = vals.get('horse_power')
        # Apparently, the value is automatically none when the field is ReadOnly.
        # It is not pretty, but it works.
        if horse_power is not None and horse_power == 998:
            raise ValidationError("The horse power is too damn high! Maybe... Don't!")
        result = super(Car, self).write(vals)
        return result

    def unlink(self):
        print("\n\tYou are on the method unlink override")
        print("\tEnd of method unlink override\n")

        for rec in self:
            if rec.name == 'Glass of Milk':
                raise ValidationError("You can't delete such a nutritious glass of milk, you monster!")

        result = super(Car, self).unlink()
        return result

    def get_max_speed(self):
        self.max_speed = self.horse_power ** (1 / 3) * 20

    def get_random_message(self):
        # print('driver_id', self.driver_id)
        # print('driver_id id', self.driver_id.id)
        # print('driver_id name', self.driver_id.name)
        messages = {
            "That car may look sleek, but it's about as fast as a turtle on tranquilizers!",
            "I've seen snails move faster than this rust bucket.",
            "If that car were any slower, it'd be going backwards.",
            f"This car handles like a shopping cart with a broken wheel, {self.driver_id.name}!",
            "You call that a sports car? I call it a retirement home on wheels.",
            "This ride is about as aerodynamic as a brick.",
            f"If I wanted to go this slow, I'd just walk, {self.driver_id.name}.",
            f"{self.driver_id.name}, you're doing great, but let's pick up the pace!",
            f"{self.driver_id.name}, with your skills, you deserve a better car than this!",
            "This car has about as much speed as a tortoise with a hangover."
        }
        self.random_message = random.choice(list(messages))

    def mail_driver_about_car(self):
        # Make sure to, when testing, use contacts that have email addresses.
        template_id = self.env.ref('custom_module1.car_mail_template')
        if template_id:
            print("\n\tThe email was sent, probably!\n")
            template_id.send_mail(
                self.id,
                force_send=True,
                raise_exception=True,
                email_values={
                    'email_to': self.driver_id.email,
                })


class Parking(models.Model):
    _name = 'parking.parking'
    name = fields.Char(string='Name')
    car_ids = fields.One2many('car.car', 'parking_id', string='Cars')


class Features(models.Model):
    _name = 'features.features'
    name = fields.Char(string='Name')
    value = fields.Float(string='Value')
