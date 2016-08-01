from openerp import api, fields, models


class Farm(models.Model):
    _inherit = 'purchase.order'

    farm_id = fields.Many2one('farm')
    folio = fields.Char(related="farm_id.folio", readonly=True)
    farm_owner = fields.Many2one('res.partner', related="farm_id.farm_owner", readonly=True)
    city = fields.Many2one('res.country.state.city', related="farm_id.city", readonly=True)
    coords = fields.Char(related="farm_id.coords", readonly=True)
    area = fields.Float(related="farm_id.area", readonly=True)

    hired_area = fields.Float()
    expected_performance = fields.Float(default=12)
    regime = fields.Selection([
        ('riego', 'Riego'),
        ('temporal', 'Temporal'),
    ], default='riego')
    validated_production = fields.Float()
    validated_year = fields.Integer(size=4)
    annex_folio = fields.Integer()
    client = fields.Many2one('res.partner')
    ownership_type = fields.Selection([
        ('propio', 'Propio'),
        ('derivado', 'Derivado'),
    ])
