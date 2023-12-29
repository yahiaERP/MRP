{
    'name': 'Gamme mrp',
    "license": "OPL-1",
    'summary': "",
    "description": """""",
    "version": "1.0",

    "category": "fabrication",

    'depends': ['base', 'mrp', 'mrp_workcenter_fields', 'Gamme_montage'],
    'data': [
        'security/ir.model.access.csv',
        'views/gamme_mrp_production.xml',
        'reports/report.xml',
        'reports/travail_magasin.xml',
    ],
    "installable": True,
    "application": True,
}
