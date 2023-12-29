from odoo import fields,api,models

class anciennete(models.Model):
    _name="autonomie"
    _rec_name="echelle_autonomie"

    echelle_autonomie=fields.Char(string="Echelle")
    design_autonomie=fields.Char(string="designation")
    note_eval_autonomie=fields.Integer(string="Note")