# -*- coding: utf-8 -*-

from odoo import models, fields, api


class MaintenanceEquipmentCategory(models.Model):
    _inherit = 'maintenance.equipment.category'
    _description = 'task_14.task_14'

    message = fields.Char(string="Message", default="Hello World!")
