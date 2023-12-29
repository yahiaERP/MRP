# _*_ coding: utf-8 _*_
import qrcode
import base64

from io import BytesIO

from odoo import models, fields, api
from odoo.exceptions import UserError


class MrpWorkcenter(models.Model):
    _inherit = 'mrp.workcenter'

    qr_code = fields.Binary("QR Code")
    numero_poste = fields.Char(string="numéro de la poste")
    employee_id = fields.Many2one(
        'hr.employee', string="Employé", domain="[('Note', '>=', Note)]")
    heure_sortie=fields.Float('Time')
    employe_remp=fields.Many2one(
        'hr.employee', string="Employé remplacant", domain="[('Note', '>=', Note)]")
    heure_remplacement=fields.Float('Time')
    note_employe = fields.Integer(string="note employe", compute="compute_note")
    duree = fields.Float('durée', help="Time in minutes for the setup.")
    Note = fields.Integer()

    def generate_qr(self):
        if not self.name or not self.employee_id or not self.duree:
            raise UserError(
                _('Veuillez vérifier que le nom, employé et la durée sont remplis'))
        else:
            qr = qrcode.QRCode(
                version=1,
                error_correction=qrcode.constants.ERROR_CORRECT_L,
                box_size=10,
                border=4,
            )
            qr.add_data(self.name)
            qr.add_data("\n")
            qr.add_data(self.employee_id.name)
            qr.add_data("\n")
            qr.add_data(self.duree)
            qr.make(fit=True)
            img = qr.make_image()
            tmp = BytesIO()
            img.save(tmp, format="PNG")
            qr_img = base64.b64encode(tmp.getvalue())
            self.qr_code = qr_img

    @api.onchange('employee_id')
    def compute_note(self):
        self.note_employe = self.employee_id.Note
