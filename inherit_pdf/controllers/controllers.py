# -*- coding: utf-8 -*-
# from odoo import http


# class InheritPdf(http.Controller):
#     @http.route('/inherit_pdf/inherit_pdf/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/inherit_pdf/inherit_pdf/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('inherit_pdf.listing', {
#             'root': '/inherit_pdf/inherit_pdf',
#             'objects': http.request.env['inherit_pdf.inherit_pdf'].search([]),
#         })

#     @http.route('/inherit_pdf/inherit_pdf/objects/<model("inherit_pdf.inherit_pdf"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('inherit_pdf.object', {
#             'object': obj
#         })
