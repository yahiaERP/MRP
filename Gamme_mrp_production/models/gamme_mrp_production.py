from odoo import models, fields, api, _
from odoo.exceptions import ValidationError
import logging


_logger = logging.getLogger(__name__)


class mrp_production(models.Model):

    _inherit = "mrp.production"

    prescription_lines = fields.One2many(
        'phases', 'mrp_production_id', string="phase", compute="_compute_prescription_lines")
    outil_ids = fields.Many2many('outil', string="Outils", related="product_id.product_tmpl_id.outils")
    composant_ids = fields.Many2many('composant', string="Composants", related="product_id.product_tmpl_id.details_composant")

    @api.depends("product_id")
    def _compute_prescription_lines(self):
        phase_ids = self.env['gamme'].search(
            [('product_id', '=', self.product_id.id)])
        self.prescription_lines = phase_ids.prescription_line_ids

    @api.onchange('prescription_lines')
    def _onchange_prescription_lines(self):
        if not self.prescription_lines:
            self.workorder_ids = False
        else:
            for prescription in self.prescription_lines:
                self.workorder_ids = [(0, 0, {
                    'name': prescription.operations,
                    'employe': prescription.employe.id,
                    'workcenter_id': prescription.Poste.id,
                    'duration_expected': prescription.temps_alloué
                })]

    class Phase(models.Model):
        _name = "phases_fabrication"
        _description = "Appointment Prescription Lines"

    sl_no = fields.Integer(string="numéro poste", readonly=True)
    phases = fields.Char(string="phases")
    operations = fields.Char(string="operations")
    outils = fields.Many2many('outil')
    schema_croquis = fields.Binary(string="schema et croquis")
    Poste = fields.Many2one('mrp.workcenter')
    employe = fields.Many2one('hr.employee', related="Poste.employee_id")
    Note = fields.Char(string="Note",compute="afficher")
    employe_rempl = fields.Many2one('hr.employee', related="Poste.employe_remp")
    temps_alloué = fields.Float('Total Seconds')
    renseignements = fields.Text(string="renseignements")
    phase = fields.Many2one('mrp.production', string="phase")

    @api.onchange('employe')
    def afficher(self):
        self.note=self.employe.note
