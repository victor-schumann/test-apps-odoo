# -*- coding: utf-8 -*-
{
    'name': "mail_list_dlc_2",

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
    'depends': ['base', 'mass_mailing', 'sale'],

    # always loaded
    'data': [
        'security/ir.model.access.csv',
        'wizard/wizard_view.xml',
        'views/mailing_contact_form_inherit.xml',
        'views/menus.xml',

    ],

    'assets': {
        'web.assets_backend': [
            'button_near_create/static/src/js/tree_button.js',
        ],
        'web.assets_qweb': [
            'button_near_create/static/src/xml/tree_button.xml',
        ],
    },
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}
