from odoo import fields,models


class intervention(models.Model):
    _name="intervention"
    _rec_name="demandeur"


    date=fields.Date()
    demandeur=fields.Many2one('hr.employee')
    resultat = fields.Selection([
        ('bon', 'bon'),
        ('fait', 'fait'),
        ('encours', 'en cours '),
    ], string='resultat', required=True)
    degre_urgence=fields.Char(string="degre urgence")
    type_intervention=fields.Selection([
        ('depannage', 'depannage'),
        ('reparation', 'reparation'),
        ('reglage', 'reglage'),
        ('controle', 'controle '),
        ('hydraulique', ' hydraulique'),
         ('reconstruction_mecanique', ' reconstruction mecanique'),
          ('electrique_pneumatique', 'electrique pneumatique'),
    ], string='type d"intervention', required=True)
    description_intervention=fields.Text()
    prescription_line = fields.One2many('phases_interv', 'phases', string="phase")


class Phase(models.Model):
    
    _name = "phases_interv"
    

    n_operation = fields.Integer(string="n°", readonly=True)
    type_intervention = fields.Char(string="type intervention", required=True)
    debut_intervention = fields.Char(string="debut intervention")
    fin_intervention = fields.Char(string="fin intervention")
    duree = fields.Float(string="durée")
    observation = fields.Text(string="observations")
    phases = fields.Many2one('intervention', string="Appointment")