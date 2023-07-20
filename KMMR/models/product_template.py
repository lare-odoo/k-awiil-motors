from odoo import api, fields, models

class ProductTemplate (models.Model):
    _inherit = "product.template"

    registry_id = fields.Many2one (
         comodel_name = "motorcycle.registry",
         string = "Motorcycle Registry",
         ondelete = "set null",
    )

    make = fields.Char (related = "registry_id.make", readonly=False)
    model = fields.Char (related = "registry_id.model", readonly=False)
    year = fields.Char (related = "registry_id.year", readonly=False)
    curb_weight = fields.Float (related = "registry_id.curb_weight", readonly=False)
    launch_date = fields.Date (related = "registry_id.launch_date", readonly=False)
    horsepower = fields.Float (related = "registry_id.horsepower", readonly=False)
    top_speed = fields.Float (related = "registry_id.top_speed", readonly=False)
    torque = fields.Float (related = "registry_id.torque", readonly=False)
    battery_capacity = fields.Selection (related = "registry_id.battery_capacity", readonly=False)
    charge_time = fields.Float (related = "registry_id.charge_time", readonly=False)
    range_field = fields.Float (related = "registry_id.range_field", readonly=False)
    
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
    