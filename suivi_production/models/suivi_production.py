from odoo import fields,api,models

class production(models.Model):
    _name="production"
    _rec_name="product"


    qte_initiale=fields.Integer()
    nb_fabrique=fields.Integer()
    debut = fields.Float('Time', help="Time in minutes for the setup.")
    reste=fields.Integer(string="reste a fabriquer")
    nb_ouvrier=fields.Integer(string="nombre d'ouvriers")
    testeurs=fields.Many2one('hr.employee',string="testeurs")
    date=fields.Date(string="date début fabrication")
    product=fields.Many2one('product.product')
    jours_semaine=fields.Many2one('jours',string="jours de la semaine")
    production=fields.One2many('suivi_journalier','prod',string="production")

   
    
class production(models.Model):
    _name="suivi_journalier"

    qte_initiale=fields.Integer()
    nb_fabrique=fields.Integer()
    debut = fields.Date(help="Time in minutes for the setup.")
    reste=fields.Integer(string="reste a fabriquer",compute="compute_quantite")
    nb_ouvrier=fields.Integer(string="nombre d'ouvriers")
    testeurs=fields.Many2many('hr.employee',string="testeurs")
    prod = fields.Many2one('production', string="Appointment")

    @api.onchange("qte_initiale",'nb_fabrique')
    def compute_quantite(self):
        for record in self:
            record.reste=record.qte_initiale-record.nb_fabrique




                        