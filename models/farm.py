from openerp import api, fields, models


class Farm(models.Model):
    _name = 'farm'

    id_farm = fields.Char(required=True)
    folio = fields.Char(size=12, required=True)
    owner = fields.Many2one('res.partner', required=True)
    city = fields.Many2one('res.country.state.city', required=True)
    coords = fields.Char(required=True)
    area = fields.Float(required=True)
