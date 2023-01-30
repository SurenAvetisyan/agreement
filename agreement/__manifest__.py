{
    'name': "agreement",
    'summary': """Agreement""",
    'author': "Avetisyan",
    'category': 'CRM',
    'version': '15.0.0.1',

    # any module necessary for this one to work correctly
    'depends': ['base', 'mail'],

    # always loaded
    'data': [
        # start Roles and groups
        'security/ir.model.access.csv',
        'security/security.xml',
        # end Roles and groups

        # start sequence
        'views/ir_sequence.xml',
        # end sequence

        # start cron job
        'views/cron_job.xml',
        'views/mail_template.xml',
        # end cron job

        # start views
        'views/agreement.xml',
        'views/agreement_types.xml',
        'views/menuitem.xml',
        # end views
    ],
}
