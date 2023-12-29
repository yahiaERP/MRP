{
    'name': 'suivi prod',
    "license": "OPL-1",
    'summary': "",
    "description": """""",
    "version": "1.0",
   
    "category": "production",

    'depends': ['base','mrp','product'],
    'data': [
        'security/ir.model.access.csv',
        'views/suivi_production.xml',
        'views/jours_semaine.xml',
        'reports/report.xml',
        'reports/rapport_production.xml',
    ],
    "installable": True,
    "application": True,
}
