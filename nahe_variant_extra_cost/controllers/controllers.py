# -*- coding: utf-8 -*-
# from odoo import http


# class NaheVariantExtraCost(http.Controller):
#     @http.route('/nahe_variant_extra_cost/nahe_variant_extra_cost', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/nahe_variant_extra_cost/nahe_variant_extra_cost/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('nahe_variant_extra_cost.listing', {
#             'root': '/nahe_variant_extra_cost/nahe_variant_extra_cost',
#             'objects': http.request.env['nahe_variant_extra_cost.nahe_variant_extra_cost'].search([]),
#         })

#     @http.route('/nahe_variant_extra_cost/nahe_variant_extra_cost/objects/<model("nahe_variant_extra_cost.nahe_variant_extra_cost"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('nahe_variant_extra_cost.object', {
#             'object': obj
#         })
