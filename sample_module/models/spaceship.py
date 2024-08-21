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
    cost_per_gallon = fields.Float(string="Cost Per Gallon")
    gallons_per_tank = fields.Integer(string="Gallons per tank")

    cost_per_tank = fields.Float(string = "Cost to Fill Tank", compute="_compute_cost_per_tank")


    ship_length = fields.Integer(string="Ship Length")
    ship_width = fields.Integer(string="Ship Width")
    ship_height = fields.Integer(string="Ship Height")
    
    ship_volume = fields.Float(string = "Ship Volume", compute="_compute_ship_volume")   


    @api.depends('cost_per_gallon','gallons_per_tank')
    def _compute_cost_per_tank(self):
        for spaceship in self: 
            spaceship.cost_per_tank = spaceship.cost_per_gallon * spaceship.gallons_per_tank
    
                
        
    @api.depends('ship_height','ship_width','ship_length')
    def _compute_ship_volume(self):
        for spaceship in self: 
            spaceship.ship_volume = spaceship.ship_height * spaceship.ship_length * spaceship.ship_width

    spaceships = fields.One2Many(comodel_name='sale.order',inverse_name='spaceship_id',string="spaceships")


    


