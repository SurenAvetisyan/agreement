{
    'name': "agreement",
    'summary': """Agreement""",
    'author': "Avetisyan",
    'category': 'CRM',
    'version': '15.0.0.1',

    # any module necessary for this one to work correctly
    'depends': ['base'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        'security/security.xml',
        'views/agreement_types.xml',
        'views/menuitem.xml',
    ],
}
