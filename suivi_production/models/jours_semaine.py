from odoo import models,fields,api 

class jours(models.Model):
    _name="jours"
    _rec_name="jours_semaine"

    jours_semaine=fields.Char()