from openerp import api, fields, models, _


class Farm(models.Model):
    _name = 'farm'

    name = fields.Char(string="Farm ID", required=True)
    folio = fields.Char(size=12, required=True)
    owner = fields.Many2one('res.partner', required=True)
    city = fields.Many2one('res.country.state.city', required=True)
    coords = fields.Char(required=True)
    area = fields.Float(required=True)

    _sql_constraints = [
        ('farm_id_unique',
         'UNIQUE(name)',
         _("The farm id must be unique")),
    ]
