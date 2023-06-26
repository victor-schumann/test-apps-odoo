# -*- coding: utf-8 -*-
{
    'name': "custom_module1",

    'summary': """
        Short (1 phrase/line) summary of the module's purpose, used as
        subtitle on modules listing or apps.openerp.com""",

    'description': """
        Long description of module's purpose
    """,

    'author': "My Company",
    'website': "https://www.yourcompany.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/16.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base', 'mail'],

    # always loaded
    'data': [
        'data/sequence.xml',
        'data/car_mail_template.xml',
        'wizard/car_wizard.xml',

        'security/security.xml',
        'security/ir.model.access.csv',

        'views/views.xml',
        'views/templates.xml',
        'views/car.xml',
        'views/parking.xml',
        'views/res_partner_iherit_form_view.xml',

    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}
