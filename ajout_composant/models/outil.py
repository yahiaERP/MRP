from odoo import fields, models

class outil(models.Model):
    _name ='outil'
    _rec_name="nom_outil"

    nom_outil = fields.Char(string='Nom des outils')