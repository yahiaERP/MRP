from odoo import models, fields

class ProductProduct(models.Model):
    _inherit = 'mrp.production'

    product_id = fields.Many2one(
        'product.product', 'Product',
        domain="""[
            ('type', 'in', ['product']),
            '|',
                ('company_id', '=', False), 
                ('company_id', '=', company_id)
        ]
        """,
        readonly=True, required=True, check_company=True,
        states={'draft': [('readonly', False)]})
   