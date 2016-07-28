from openerp import api, fields, models


class Farm(models.Model):
    _inherit = 'purchase.order'

    farm_id = fields.Many2one('farm', required=True)
    folio = fields.Char(related="farm_id.folio", readonly=True)
    farm_owner = fields.Many2one('res.partner', related="farm_id.farm_owner", readonly=True)
    city = fields.Many2one('res.country.state.city', related="farm_id.city", readonly=True)
    coords = fields.Char(related="farm_id.coords", readonly=True)
    area = fields.Float(related="farm_id.area", readonly=True)

    hired_area = fields.Float(required=True)
    regime = fields.Selection([
        ('riego', 'Riego'),
        ('temporal', 'Temporal'),
    ], required=True)
    expected_performance = fields.Float()
    validated_production = fields.Float(required=True)
    validated_year = fields.Integer(size=4, required=True)
    annex_folio = fields.Integer(required=True)
    client = fields.Many2one('res.partner', required=True)
    ownership_type = fields.Selection([
        ('propio', 'Propio'),
        ('derivado', 'Derivado'),
    ], required=True)
