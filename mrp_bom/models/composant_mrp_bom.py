from odoo import models,fields,api

class composnat_bom(models.Model):
    _inherit="mrp.bom"

    composant=fields.Many2one('nomenclature',string="composants")
    categorie=fields.Char(string="categorie")
    reference=fields.Char(string="reference")

    @api.onchange('composant')
    def afficher(self):
        self.categorie=self.composant.categorie
        self.reference=self.composant.reference