from odoo import models,fields

class indice(models.Model):
    _name="indice"
    _rec_name="article"

    article=fields.Char(string="article")
    indice_arrivage=fields.Char(string="indice d'arrivage")
    indices=fields.One2many('indice_arrivage','ind',string="indice d'arrivage")


class indices(models.Model):
    _name="indice_arrivage"

    indice_arrivage=fields.Char(string="indice d'arrivage")
    quantite=fields.Integer(string="quantite")
    ind = fields.Many2one('indice', string="Composants")

    