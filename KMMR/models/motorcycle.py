import re
from odoo import api, fields, models
from odoo.exceptions import ValidationError

# Inherit from basic Model
class Course(models.Model):
    _name = 'motorcycle.registry'
    _description = 'Motorcycle registry'
    _rec_name = 'registry_number'
    
    # The record set here is irrelevant, it will
    # be overridden when creating a record
    registry_number = fields.Char(
        string="Registry Number",   # Display name
        default="MRN0000",          # Pattern
        required=True,
        copy=False,                 # If duplicating, don't copy this value
        readonly=True,              # Users can't change this value
        )

    # VIN format:
    # -- Make - 2 capital letters
    # -- Model - 2 capital letters
    # -- Year - 2 digits
    # -- Battery Capacity - 2 capital letters or digits
    # -- Serial Number - 6 digits
    vin = fields.Char (string="VIN",required=True)

    # Computed from VIN
    make = fields.Char (compute = "_get_brand_make_model", inverse = "_set_brand_make_model")
    model = fields.Char (compute = "_get_brand_make_model", inverse = "_set_brand_make_model")
    year = fields.Char (compute = "_get_brand_make_model", inverse = "_set_brand_make_model")
    
    # We're using res.partner model to handle contact
    # info, including name, phone and email.
    # This requires a relationship field.

    motorcycle_owner_id = fields.Many2one (
        comodel_name = "res.partner", 
        string = "Owner", 
        ondelete = "restrict", 
        required = True
        )
    
    owner_phone = fields.Char (related = "motorcycle_owner_id.phone")
    owner_email = fields.Char (related = "motorcycle_owner_id.email")

    picture = fields.Image()
    current_mileage = fields.Float()
    license_plate = fields.Char()
    certificate_title = fields.Binary(string="Certificate Title")
    register_date = fields.Date()
    
    # The create method takes a list of values
    # to create the record, and the 'self' to
    # get relevant data from the environment

    # This model decorator indicates that the 
    # method refers to the model, and not a record

    # If a user tries to do a massive input, 
    # that might not be so great. Which is why we use
    # 'model_create_multi' instead, and we work over
    # a list by iterating through all the records

    # @api.model
    # def create(self, vals):
    @api.model_create_multi
    def create(self, vals_list):
        for vals in vals_list:
        # If the registry number is equal to the default
        # pattern set above, we use the sequence
            if vals.get('registry_number', ('MRN0000')) == ('MRN0000'):
                vals['registry_number'] = self.env['ir.sequence'].next_by_code('registry.number')

        return super().create(vals_list)
            
    @api.constrains('license_plate')
    def _check_license_plate (self):
        regex = re.compile ("[A-Z]{1,4}[0-9]{1,3}([A-Z]{2})?$")

        for motorcycle in self:
            if re.search(regex, motorcycle.license_plate) is None:
                raise ValidationError ('License plate doesn\'t match format')
            
    @api.constrains('vin')
    def _check_registration_no(self):
        for motorcycle in self:
            domain = [('vin', '=', motorcycle.vin)]
            count = self.sudo().search_count(domain)

            if count > 1:
                raise ValidationError ("VIN should be unique")
            
    @api.constrains('vin')
    def _check_vin (self):
        regex = re.compile ("[A-Z]{4}\d{2}([A-Z]|\d){2}\d{6}")

        for motorcycle in self:
            if len(motorcycle.vin) != 14 or re.search(regex, motorcycle.vin) is None:
                raise ValidationError ('VIN doesn\'t match format')

            # Check how to make following code work by
            # searching through the entire DB

            # domain = [('vin', '=', motorcycle.vin)]
            # count = self.sudo().search_count(domain)

            # if count > 1:
            #     raise ValidationError ("VIN should be unique")

    @api.depends ('vin')
    def _get_brand_make_model (self):
        for motorcycle in self:
            motorcycle.make = motorcycle.vin[0:2]
            motorcycle.model = motorcycle.vin[2:4]
            motorcycle.year = motorcycle.vin[4:6]

    def _set_brand_make_model (self):
        for motorcycle in self:
            if not motorcycle.make: continue
            motorcycle.make = ""
            if not motorcycle.model: continue
            motorcycle.model = ""
            if not motorcycle.year: continue
            motorcycle.year = ""