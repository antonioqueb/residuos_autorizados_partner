from odoo import models, fields

class CatalogoResiduo(models.Model):
    _name = "residuo.catalogo"
    _description = "Catálogo Oficial de Residuos Autorizados"
    _rec_name = "nombre_clave"

    clave = fields.Char(string="Clave", required=True)
    descripcion = fields.Char(string="Descripción", required=True)
    nombre_clave = fields.Char(compute="_compute_nombre_clave", store=True)

    @fields.depends("clave", "descripcion")
    def _compute_nombre_clave(self):
        for rec in self:
            rec.nombre_clave = f"{rec.clave} - {rec.descripcion}"
