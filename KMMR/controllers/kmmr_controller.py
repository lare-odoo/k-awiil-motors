from odoo import http

class Kmmr (http.Controller):
    @http.route ('/compare/', auth = 'public', website = True)
    def index (self, **kw):
        bikes = http.request.env['product.template'].search([("type", "=", "motorcycle")])
        return http.request.render (
            'KMMR.compare_bikes', {
                'bikes': bikes,
            }
        )
    