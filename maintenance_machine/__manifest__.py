{
    "name": "controle machine",
    "license": "OPL-1",
    "summary": "",
    "description": """""",
    "version": "1.0",
    "category": "maintenance",
    "depends": ["base", "product"],
    "data": [
        "security/ir.model.access.csv",
        "views/rapport_intervention.xml",
        "views/rapport_maintenance.xml",
        "reports/intervention_report.xml",
        "reports/maintenance_report.xml",
        "reports/report.xml",
    ],
    "installable": True,
    "application": True,
}
