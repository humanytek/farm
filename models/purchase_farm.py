from openerp import api, fields, models


class FarmArea(models.Model):
    _name = 'farm.area'

    purchase_order_id = fields.Many2one('purchase.order')
    farm_id = fields.Many2one('farm')
    hired_area = fields.Float()
    expected_performance = fields.Float(default=12)
    tons_to_validate = fields.Float(compute="_get_tons_to_validate", store=False)
    regime = fields.Selection([
        ('riego', 'Riego'),
        ('temporal', 'Temporal'),
    ], default='riego')
    validated_production = fields.Float()
    validated_year = fields.Integer(size=4)
    annex_folio = fields.Char()
    expiration = fields.Date()
    client = fields.Many2one('res.partner')
    ownership_type = fields.Selection([
        ('propio', 'Propio'),
        ('derivado', 'Derivado'),
    ])

    @api.one
    @api.depends('hired_area', 'expected_performance')
    def _get_tons_to_validate(self):
        self.tons_to_validate = self.hired_area * self.expected_performance

class FarmInherit(models.Model):
    _inherit = 'purchase.order'

    farm_area_ids = fields.One2many('farm.area', 'purchase_order_id')
