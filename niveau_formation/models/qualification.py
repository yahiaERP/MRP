from odoo import models, fields,api


class qualification(models.Model):
    _name ='qualification'
    _description="qualificaion employé selon la catégorie"
    _rec_name="categorie"


    categorie = fields.Char(string='categorie')
    qualification_fonction = fields.Char(string="qualification fonction")
    evaluation=fields.Integer(string="Note évaluation")
    