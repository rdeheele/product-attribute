# Copyright 2020 PlanetaTIC - Marc Poch <mpoch@planetatic.com>
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from odoo import api, fields, models


class ProductApplication(models.Model):
    _name = 'product.application'
    _inherit = [_name, 'custom.info']

    custom_info_template_id = fields.Many2one(
        context={"default_model": _name})
    custom_info_ids = fields.One2many(
        context={"default_model": _name})

    name = fields.Char(
        string='Application Name',
        compute='_get_application_name',
        required=False
    )

    @api.model
    def _get_application_name(self):
        for app in self:
            items = []
            for tmpl in app.custom_info_template_id:
                for prop in tmpl.property_ids:
                    items.append(str(prop.default_value))
            app.name = ' | '.join(items)
