# -*- coding: utf-8 -*-
{
    'name': "inherit pdf",

    'summary': """
        """,

    'description': """
        Easy to get a copied of invoice, Just only one click
        ====================================================
    """,

    'author': "Sahassawat Posungnern",
    'website': "",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/14.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Tools',
    'version': '0.1',
    'license': 'AGPL-3',
    # any module necessary for this one to work correctly
    'depends': ['base', 'account', ],

    'images': ['static/description/thumbnail.png'],
    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        'report/invoice_report_inherit.xml',
        'report/receipt_actions.xml',
        # 'views/views.xml',
        # 'views/templates.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        # 'demo/demo.xml',
    ],
}
