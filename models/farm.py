from openerp import api, fields, models


class Farm(models.Model):
    _name = 'farm'

    id = fields.Char()
    folio = fields.Char(size=12)
    owner = fields.Many2one('res.partner')
    city = fields.Many2one('res.country.state.city')
    coords = fields.Char()
    area = fields.Float()
