# -*- coding: utf-8 -*-

from odoo import models, fields

class ProductPricelist(models.Model):
    _inherit = 'product.pricelist'

    restrict_to_contacts = fields.Boolean(
        string='Restringir a contactos específicos',
        default=False,
        help='Si está marcado, esta lista de precios solo podrá ser asignada a los contactos permitidos.'
    )
    allowed_partner_ids = fields.Many2many(
        'res.partner',
        'product_pricelist_partner_rel',
        'pricelist_id',
        'partner_id',
        string='Contactos Permitidos',
        help='Contactos autorizados a usar esta lista de precios.'
    )
