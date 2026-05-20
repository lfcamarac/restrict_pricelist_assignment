# -*- coding: utf-8 -*-

from odoo import models, fields, api, _
from odoo.exceptions import ValidationError

class SaleOrder(models.Model):
    _inherit = 'sale.order'

    commercial_partner_id = fields.Many2one(
        'res.partner', 
        related='partner_id.commercial_partner_id', 
        string='Entidad Comercial Relacionada',
        store=False
    )

    @api.constrains('pricelist_id', 'partner_id')
    def _check_pricelist_partner_restriction(self):
        for order in self:
            pricelist = order.pricelist_id
            partner = order.partner_id
            if pricelist and pricelist.restrict_to_contacts:
                if not partner:
                    raise ValidationError(_(
                        "Debe seleccionar un cliente antes de usar la lista de precios restringida '%s'."
                    ) % pricelist.display_name)
                allowed_partners = pricelist.allowed_partner_ids
                if partner not in allowed_partners and partner.commercial_partner_id not in allowed_partners:
                    raise ValidationError(_(
                        "La lista de precios '%s' está restringida y no puede ser utilizada para el cliente '%s' porque no está en la lista de contactos autorizados."
                    ) % (pricelist.display_name, partner.name))
