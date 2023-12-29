from odoo import fields,api,models

class anciennete(models.Model):
    _name="anciennete"
    _rec_name="ancienete"

    ancienete=fields.Char(string="ancienete")
    note_eval=fields.Integer(string="note evaluation")