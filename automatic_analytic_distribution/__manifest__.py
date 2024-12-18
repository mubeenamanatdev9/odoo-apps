{
    'name': 'automatic_analytic_distribution',

    'summary': 'automatic_analytic_distribution',

    'version': '1.0.0.0.0',

    'author': 'Mubeen Amanat (mubeenamanat.dev@gmail.com)',

    "maintainer": "Mubeen Amanat",

    "website": "https://mubeenamanat.com",

    'category': 'Accounting/Accounting',

    'description': 'automatic_analytic_distribution',

    'depends': ['account'],

    'sequence': 10,
    'data': [
	'views/account_move_ext.xml'
    ],

    'assets': {
        'web.assets_backend': [
        ],
        'web.assets_frontend': [
    	
        ]

    },

    'installable': True,

    'application': True,

    'auto_install': False,

    'price': 1.00,

    "currency": "USD",

    "license": "LGPL-3",
}

