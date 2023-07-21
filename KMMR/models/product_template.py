from odoo import fields, models

class ProductTemplate (models.Model):
    _inherit = "product.template"

    registry_id = fields.Many2one (
         comodel_name = "motorcycle.registry",
         string = "Motorcycle Registry",
         ondelete = "set null",
    )
    
    detailed_type = fields.Selection (
        selection_add = [('motorcycle', 'Motorcycle')], 
        ondelete = {
            'motorcycle': 'set consu'
        }
    )
    type = fields.Selection (
        selection_add = [('motorcycle', 'Motorcycle')], 
        ondelete = {
            'motorcycle': 'set consu'
        }
    )

    make = fields.Char ()
    model = fields.Char ()
    year = fields.Char ()
    horsepower = fields.Float ()
    top_speed = fields.Float ()
    torque = fields.Float ()
    battery_capacity = fields.Selection (
        selection = [
            ('xs', 'Economical'),
            ('sm', 'Small'),
            ('md', 'Medium'),
            ('lg', 'Large'),
            ('xl', 'Extra Large'),
        ],
        default = 'md'
    )
    charge_time = fields.Float ()
    range_field = fields.Float (string = "Range")
    curb_weight = fields.Float ()
    launch_date = fields.Date ()
    picture = fields.Image ()
    