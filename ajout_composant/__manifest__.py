{
    'name': 'Ajout composant',
    "license": "OPL-1",
    'summary': "",
    "description": """""",
    "version": "1.0",
   
    "category": "Comptabilité",

    'depends': ['base','mrp'],
    'data': [
        'security/ir.model.access.csv',
        'views/indice_arrivage.xml',
        'views/ajout_composant.xml',
        'views/outils.xml',
        'views/nomenclature_composant.xml'
        
    ],
    "installable": True,
    "application": True,
}