from odoo import models,fields,api
# _*_ coding: utf-8 _*_
import qrcode
import base64
from io import BytesIO
from odoo.exceptions import UserError


class product(models.Model):

    _inherit = 'product.template'

    numero_serie = fields.Char(string="numéro de série")
    description=fields.Text(string="description")
    type_article=fields.Selection([ ('comp', 'composant' )],'type')
    modele = fields.Char(string="modele")
    date_fabrication = fields.Date(string="date de fabrication ")
    date_arrivage = fields.Date(string="date arrivage")
    details_composant = fields.Many2many('composant', string="composants")
    outils = fields.Many2many('outil', string="outils")
    capacite=fields.Char()
    durée_granatie=fields.Integer(string="durée garantie")
    reference = fields.Char(string="référence")
    nom_fournisseur = fields.Char(string="Nom Fournisseur")
    qr_code = fields.Binary("QR Code")
    name=fields.Char(string="name")


    
    def generate_qr(self):
        if self.name:
            if self.list_price:
                if self.default_code:
                    qr = qrcode.QRCode(
                        version=1,
                        error_correction=qrcode.constants.ERROR_CORRECT_L,
                        box_size=10,
                        border=4,
                    )
                    qr.add_data(self.numero_serie)
                    qr.add_data('\n')
                    qr.add_data(self.modele)
                    qr.add_data('\n')
                    qr.add_data(self.date_fabrication)
                    qr.add_data('\n')
                    qr.add_data(self.details_composant)
                    qr.add_data('\n')
                    qr.make(fit=True)
                    img = qr.make_image()
                    tmp = BytesIO()
                    img.save(tmp, format="PNG")
                    qr_img = base64.b64encode(tmp.getvalue())
                    self.qr_code = qr_img
                else:
                    raise UserError(
                        _('Check if Product Name, Sales Price or Internal Reference empty'))
