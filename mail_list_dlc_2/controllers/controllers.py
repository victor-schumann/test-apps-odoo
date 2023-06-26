# -*- coding: utf-8 -*-
# from odoo import http


# class MailListDlc2(http.Controller):
#     @http.route('/mail_list_dlc_2/mail_list_dlc_2', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/mail_list_dlc_2/mail_list_dlc_2/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('mail_list_dlc_2.listing', {
#             'root': '/mail_list_dlc_2/mail_list_dlc_2',
#             'objects': http.request.env['mail_list_dlc_2.mail_list_dlc_2'].search([]),
#         })

#     @http.route('/mail_list_dlc_2/mail_list_dlc_2/objects/<model("mail_list_dlc_2.mail_list_dlc_2"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('mail_list_dlc_2.object', {
#             'object': obj
#         })
