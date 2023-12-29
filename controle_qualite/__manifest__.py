{
    'name': 'controle qualite',
    "license": "OPL-1",
    'summary': "",
    "description": """""",
    "version": "1.0",
    "category": "Qualité",

    'depends': ['base','product','mrp'],
    'data': [
        'security/ir.model.access.csv',
        'views/rapport_nonconformite.xml',
        'reports/report_non_conformite.xml',
        'reports/report.xml',
    ],
    "installable": True,
    "application": True,
}