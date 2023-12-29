{
    'name': 'Gamme de montage',
    "license": "OPL-1",
    'summary': "",
    "description": """""",
    "version": "1.0",

    "category": "Comptabilité",

    'depends': ['base', 'mrp', 'mrp_workcenter_fields', 'hr', ],
    'data': [
        'security/ir.model.access.csv',
        'views/gamme_montage.xml',
    ],
    "installable": True,
    "application": True,
}
