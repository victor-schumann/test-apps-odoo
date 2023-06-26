# -*- coding: utf-8 -*-
# from odoo import http


# class CustomModule2(http.Controller):
#     @http.route('/custom_module2/custom_module2', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/custom_module2/custom_module2/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('custom_module2.listing', {
#             'root': '/custom_module2/custom_module2',
#             'objects': http.request.env['custom_module2.custom_module2'].search([]),
#         })

#     @http.route('/custom_module2/custom_module2/objects/<model("custom_module2.custom_module2"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('custom_module2.object', {
#             'object': obj
#         })
