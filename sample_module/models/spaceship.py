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
    contact_id = fields.Many2one('res.partner',   
                string='Contact', index=True)
    cost_per_gallon = fields.float(string="Cost Per Gallon")
    gallons_per_tank = fields.Integer(string="Gallons per tank")

    cost_per_tank = fields.Float(string = "Cost to Fill Tank", compute="_compute_cost_per_tank")

    @api.depends('cost_per_gallonm','gallongs_per_tank')
    def _compute_cost_per_tank(self):
            Spaceship.cost_per_tank = Spaceship.cost_per_gallon * Spaceship.gallons_per_tank;


