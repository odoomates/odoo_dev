{
    'name': 'Odoo V12 Development Tutorials',
    'version': '12.0.2.1.0',
    'category': 'Extra Tools',
    'summary': 'Odoo Development Tutorials For Beginners and Experts',
    'sequence': '10',
    'license': 'AGPL-3',
    'author': 'Odoo Mates',
    'maintainer': 'Odoo Mates',
    'website': 'odoomates.com',
    'live_test_url': 'https://www.youtube.com/watch?v=BDepk0LhVuI&list=PLqRRLx0cl0hoJhjFWkFYowveq2Zn55dhM&index=1',
    'depends': ['sale', 'mail', 'report_xlsx', 'web_timeline'],
    'demo': [],
    'data': [
        'security/security.xml',
        'security/ir.model.access.csv',
        'data/sequence.xml',
        'data/data.xml',
        'data/cron.xml',
        'wizards/create_appointment.xml',
        'views/patient.xml',
        'views/appointment.xml',
        'views/doctor.xml',
        'views/lab.xml',
        'views/sale_order.xml',
        'views/template.xml',
        'views/settings.xml',
        'reports/patient_card.xml',
        'reports/report.xml',
        'reports/sale_report_inherit.xml',
        'reports/appointment.xml',
        'data/mail_template.xml',
        'views/website_form.xml',
    ],
    'images': ['static/description/banner.png'],
    'installable': True,
    'application': True,
    'auto_install': False,
}
# Video Explanation: https://www.youtube.com/watch?v=BDepk0LhVuI&list=PLqRRLx0cl0hoJhjFWkFYowveq2Zn55dhM&index=1
