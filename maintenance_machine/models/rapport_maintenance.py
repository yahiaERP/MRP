from odoo import models,fields

class conformite(models.Model):
    _name="maintenance"
    _rec_name="ref"

    elabore_par =fields.Many2one('hr.employee')
    verifie_par=fields.Many2one('hr.employee')
    ref=fields.Char()
    source=fields.Char()
    date=fields.Date()
    materiel_equipement=fields.Text(string="materiel/equipement")
    version=fields.Integer(String="version")
    code=fields.Char()
    ddi=fields.Date(String="date du dernier intervention")
    pdi=fields.Date(String="prochaine date d'intervention")
    constructeur=fields.Char()
    atelier=fields.Char()
    prescription = fields.One2many('phases_maint', 'phases', string="phase")


class Phase(models.Model):

    _name = "phases_maint"
    
    no = fields.Integer(string="no", readonly=True)
    operation = fields.Char(string="operation")
    frequence = fields.Char(string="fréquence")
    resultat = fields.Char(string="resultat")
    type_manipulation= fields.Text(string="type de manipulation ")
    observation=fields.Text(string="observation")
    phases = fields.Many2one('maintenance', string="Appointment")





    
