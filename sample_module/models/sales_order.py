from odoo import api, fields, models

class ResPartner(models.Model):
    _inherit = 'res_partner'

    spaceship_id = fields.Many2One(comodel_name='space.spaceship',string="Spaceship")
                                   