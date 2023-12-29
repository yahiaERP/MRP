from odoo import fields, models,api

class composant(models.Model):
    _name ='composant'
    _rec_name="nom_composant"

    reference=fields.Char(string="Reference")
    designation=fields.Char(string="Designation")
    nom_composant = fields.Many2one('indice',string='Nom du composant')
    quantite=fields.Integer(string="Quantite")
    photo=fields.Binary(string="photo")


    



   