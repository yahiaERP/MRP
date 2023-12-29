from odoo import models,fields,api
from datetime import datetime

class conformite(models.Model):
    _name="conformite"
    _rec_name="numero"

    numero=fields.Char()
    nc_interne=fields.Char()
    nc_reception=fields.Char()
    nc_client=fields.Char()
    code_barre=fields.Integer(size=30)
    produit=fields.Many2one('product.product')
    designation_produit=fields.Char()
    ordre_fabrication=fields.Many2one('mrp.production')
    fournisseur=fields.Char()
    date_arrivage=fields.Date()
    quantite_recu=fields.Integer()
    client=fields.Char()
    reception=fields.Char()
    description_conformite=fields.Text()
    responsable_production=fields.Many2one('hr.employee')
    controleur_qualite=fields.Many2one('hr.employee')
    responsable_magasin=fields.Many2one('hr.employee')
    responsable_technique=fields.Many2one('hr.employee')
    derogation=fields.Char()
    retour_fournisseur=fields.Text()
    rebuts=fields.Char()
    reparation=fields.Char()
    date=fields.Date(strin="Date",default=datetime.today())

   