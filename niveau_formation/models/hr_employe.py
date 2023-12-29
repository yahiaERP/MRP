from odoo import fields,api,models

class employe(models.Model):
    _inherit="hr.employee"

    echelle=fields.Many2one('interne',string="echelle")
    niveau=fields.Many2one('formation',string="niveau de  formation")
    date_debut=fields.Date(string="Date Début")
    date_fin=fields.Date(string="Date fin")
    ancienete=fields.Many2one('anciennete',string="ancienete")
    categorie=fields.Many2one('qualification',string="categorie")
    echelle_autonomie=fields.Many2one('autonomie',string="Autonomie")
    design_autonomie=fields.Char(string="designation autonomie",readonly=True)
    qualification_fonction=fields.Char(string="qualification")
    designation=fields.Char(string="designation")
    niveau_etude=fields.Char(string="niveau etude")
    note_evaluation=fields.Integer(string="Note evaluation",readonly=True)
    note_eval=fields.Integer(string="Note",readonly=True)
    evaluation=fields.Integer(string="Note",readonly=True)
    note_formation=fields.Integer(string="note formation",readonly=True)
    note_eval_autonomie=fields.Integer(string="note autonomie",readonly=True)
    Note=fields.Integer(string="Note",compute="_compute_somme",store=True)
    reclamation=fields.Integer(string="Nombre de reclamations",readonly=False)


    @api.onchange('echelle','ancienete','categorie','niveau','echelle_autonomie')
    def afficher(self):
        self.designation=self.echelle.designation
        self.note_evaluation=self.echelle.note_evaluation
        self.note_eval=self.ancienete.note_eval
        self.note_formation=self.niveau.note_formation
        self.qualification_fonction=self.categorie.qualification_fonction
        self.evaluation=self.categorie.evaluation
        self.note_eval_autonomie=self.echelle_autonomie.note_eval_autonomie
        self.design_autonomie=self.echelle_autonomie.design_autonomie
        self.niveau_etude=self.niveau.niveau_etude
        
    
    @api.onchange('note_formation','note_eval','note_evaluation','note_eval_autonomie')
    def _compute_somme(self):
        for record in self:
            record.Note = record.note_formation+record.note_eval+record.note_evaluation+record.note_eval_autonomie
            
    
    



        