{
    'name': 'Automatic Analytic Distribution',

    'summary': 'automatic_analytic_distribution',

    'version': '1.0.0.0.0',

    'author': 'Mubeen Amanat',

    "maintainer": "Mubeen Amanat",

    "website": "https://mubeenamanat.com",

    'support': 'mubeenamanat.dev@gmail.com',

    'category': 'Accounting/Accounting',

    'description': 'It Allows You to Put Automatic Analytic Distrbution Value on Invoices lines, Bills. Just Select Once and update on all lines',

    'depends': ['account'],
    'images' : ['static/description/imgs/img.png'],

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

