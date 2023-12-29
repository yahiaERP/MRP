from odoo import models, fields


class ordre(models.Model):
    _inherit = "mrp.workorder"
    _description = "ordre de fabrication MRP"

    outils = fields.Many2many('outil', string="outils")
    composants = fields.Many2one('composant',string="composants")
    employe=fields.Many2one('hr.employee')

    def print_mrp_workorder(self):
        return self.env.ref('workorder.action_report_mrp_workorder').report_action(self)
