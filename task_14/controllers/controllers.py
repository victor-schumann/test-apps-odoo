# -*- coding: utf-8 -*-
# from odoo import http


# class Task14(http.Controller):
#     @http.route('/task_14/task_14', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/task_14/task_14/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('task_14.listing', {
#             'root': '/task_14/task_14',
#             'objects': http.request.env['task_14.task_14'].search([]),
#         })

#     @http.route('/task_14/task_14/objects/<model("task_14.task_14"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('task_14.object', {
#             'object': obj
#         })
