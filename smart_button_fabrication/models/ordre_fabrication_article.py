from odoo import models,fields,api

class ordre(models.Model):
    _inherit = 'product.template'

    def get_ordre_fab(self):
        self.ensure_one()
        return {
            'type': 'ir.actions.act_window',
            'name': 'ordre de fabrication',
            'view_mode': 'tree',
            'res_model': 'mrp.production',
            #'domain': [('name', '=', product_tmpl_id.product_id)],
            'context': "{'create': False}"
        }

 