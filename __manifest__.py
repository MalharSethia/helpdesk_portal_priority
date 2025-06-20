{
    'name': 'Helpdesk Priority Portal',
    'version': '17.0.1.0.0',
    'category': 'Website/Website',
    'summary': 'Add priority field to helpdesk portal view',
    'description': """
        Extends OCA Helpdesk portal functionality by adding a priority dropdown
        field to the portal ticket creation and editing forms, and displays
        priority in the ticket detail view.
    """,
    'author': 'Your Company',
    'website': 'https://www.yourcompany.com',
    'depends': [
        'helpdesk_mgmt',  # OCA Helpdesk base module
        'portal',
        'website',
    ],
    'data': [
        'views/portal_templates.xml',
    ],
    'installable': True,
    'auto_install': False,
    'application': False,
}
