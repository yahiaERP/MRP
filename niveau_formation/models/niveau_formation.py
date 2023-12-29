from odoo import models, fields,api


class niveau(models.Model):
    _name ='formation'
    _rec_name="echelle"


    echelle = fields.Char(string='echelle')
    niveau_etude = fields.Char(string="designation")
    note_formation=fields.Integer(string="Note")
    
  
    