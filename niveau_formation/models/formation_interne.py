from odoo import models, fields,api


class niveau(models.Model):
    _name ='interne'
    _rec_name='niveau'


    niveau = fields.Char(string='niveau')
    designation = fields.Char(string="designation")
    note_evaluation=fields.Integer(string="Note")
    