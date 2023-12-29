{
    'name': 'niveau formation',
    "license": "OPL-1",
    'summary': "",
    "description": """""",
    "version": "1.0",
   
    "category": "Hr",

    'depends': ['base','hr'],
    'data': [
        'security/ir.model.access.csv',
        'views/niveau_formation.xml',
        'views/formation_interne.xml',
        'views/qualification.xml',
        'views/anciennete.xml',
        'views/degre_autonomie.xml',
        'views/hr_employe.xml',
    ],
    "installable": True,
    "application": True,
}
