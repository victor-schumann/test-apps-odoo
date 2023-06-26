# -*- coding: utf-8 -*-
{
    'name': "test_14",

    'summary': 'summary',

    'description': '',

    'author': "My Company",
    'website': "https://www.yourcompany.com",

    'category': 'Human Resources',
    # "price": 100.00,
    # "currency": "EUR",

    'depends': ['base', 'mail', 'mail_list_dlc_2'],

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
    'application': True,
}
