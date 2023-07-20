{
    'name': "Motorcycle Registry",
    'summary': "Manage Registration of Motorcycles",
    'description': """Motorcycle Registry
        ====================
        This Module is used to keep track of the Motorcycle Registration and Ownership of each motorcycled of the brand.
        """,
    'author': 'lare-odoo',
    'website': 'https://github.com/lare-odoo/k-awiil-motors',
    'category': 'Kawiil/Kawiil',
    'depends': ['base'],
    'data': [
        'security/motorcycle_groups.xml',
        'security/ir.model.access.csv',
        'data/registry_data.xml',
        'views/KMMR_menuitems.xml',
        'views/motorcycle_views.xml'
    ],
    'demo': [
        #'demo/kmmr_demo.xml',
    ],
    'application': True,
    'license': 'OPL-1',
}