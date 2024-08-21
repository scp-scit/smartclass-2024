from odoo import api, fields, models


class Spaceship(models.Model):
    """Model used to store information about spaceships"""
    _name = 'space.spaceship'
    _description = 'Spaceship'

    name = fields.Char(string="name")
    manufacture_date = fields.Date(string="Date")
    number = fields.Integer(string="Number")
    device_type = fields.Selection(selection=[('Bike', 'Bike'),
                                   ('Car', 'Car'),
                                   ('Train', 'Train'),
                                   ('other', 'Other')], 
                        string='Device Type',)
