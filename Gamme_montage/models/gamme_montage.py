from odoo import models, fields, api


class gamme(models.Model):
    _name = 'gamme'

    name = fields.Char(string='Order Reference',copy=False, readonly=True, default=lambda self: ('New'))
    barcode = fields.Char(string='code-barre')
    product_id = fields.Many2one('product.product', 'product_id')
    outil = fields.Char(string="outils")
    liste_composant = fields.Char(
        string="composants", compute="_onchange_barcode_scan", store=True, readonly=False)
    Poste = fields.Many2one('mrp.workcenter')
    employe = fields.Many2one('hr.employee')
    schema = fields.Binary(string="schéma éléctrique ")
    schema_gamme = fields.Binary(string="schéma éléctrique ")
    prescription_line_ids = fields.One2many('phases', 'phase', string="phase")

    @api.onchange('barcode', 'liste_composant', 'product')
    def _onchange_barcode_scan(self):
        product_rec = self.env['product.product']
        for record in self:
            if record.barcode:
                product_id = product_rec.search([('barcode', '=', record.barcode)])
                record.product_id = product_id
            if record.product_id:
                record.liste_composant = record.product_id.details_composant.mapped(
                    "Nom_composant")
            if record.product_id:
                record.outil = record.product_id.outils.mapped("nom_outil")

    def set_line_number(self):
        sl_no = 0
        for line in self.prescription_line_ids:
            sl_no += 1
            line.sl_no = sl_no
        return

    @api.model
    def create(self, vals):
        vals['name'] = self.env['ir.sequence'].next_by_code('gamme') or ('New')
        res = super().create(vals)
        res.set_line_number()
        return res

    def write(self, values):
        res = super().write(values)
        self.set_line_number()
        return res


class Phase(models.Model):
    _name = "phases"
    _description = "Appointment Prescription Lines"

    sl_no = fields.Integer(string="numero poste", readonly=True)
    phases = fields.Char(string="phases", required=True)
    operations = fields.Char(string="operations")
    outils = fields.Many2many('outil', string="outils")
    schema_croquis = fields.Binary(string="schema et croquis")
    Poste = fields.Many2one('mrp.workcenter')
    employe = fields.Many2one('hr.employee', related="Poste.employee_id")
    kanban_state = fields.Selection([
        ('normal', 'Grey'),
        ('done', 'Green'),
        ('blocked', 'Red')
    ], string='statut', default='normal', tracking=True, copy=False)
    Note = fields.Char(string="Note")
    employe_rempl = fields.Many2one('hr.employee', related="Poste.employe_remp")
    temps_alloué = fields.Float('Total Seconds')
    renseignements = fields.Text(string="renseignements")
    phase = fields.Many2one('gamme', string="Appointment")
    mrp_production_id = fields.Many2one('mrp.production', string="Appointment")
