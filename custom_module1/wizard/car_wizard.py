from odoo import models, fields, api


class CarWizard(models.TransientModel):
    _name = 'car.wizard'
    _description = 'Car Wizard'
    horse_power_plus = fields.Integer(string='Horse Power Update')

    # Wizard Action
    def add_horse_power(self):
        self.env['car.car'].browse(self.env.context.get('active_id')).write({
            'horse_power': self.horse_power_plus
        })
        return {'type': 'ir.actions.act_window_close'}
