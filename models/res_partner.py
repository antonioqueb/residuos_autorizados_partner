from odoo import models, fields

class ResPartner(models.Model):
    _inherit = "res.partner"

    residuos_autorizados_ids = fields.Many2many(
        comodel_name="residuo.catalogo",
        string="Tipo de residuos autorizados",
        help="Selecciona los tipos de residuos autorizados para este contacto, de acuerdo al catálogo oficial."
    )
