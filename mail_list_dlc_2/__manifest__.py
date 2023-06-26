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

    'category': 'Uncategorized',
    'version': '0.1',

    'depends': ['task_14'],

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
    'application': False,
}
