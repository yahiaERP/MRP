from odoo import models,fields,api

class nomenclature_composant(models.Model):
    _name="nomenclature"
    _rec_name="nom_composant"

    nom_composant=fields.Many2one('composant')
    product=fields.Many2one('product.product')
    categorie=fields.Selection([
        ('mecanique', 'Mécanique'),
        ('electrique', 'electrique'),
        ('accessoires', 'Accessoires'),
    ], string='categorie', required=True)

    reference=fields.Char()


    
