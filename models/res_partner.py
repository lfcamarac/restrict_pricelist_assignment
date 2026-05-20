# -*- coding: utf-8 -*-

from odoo import models, api, _
from odoo.exceptions import ValidationError

class ResPartner(models.Model):
    _inherit = 'res.partner'

    @api.constrains('property_product_pricelist')
    def _check_property_product_pricelist_restriction(self):
        for partner in self:
            pricelist = partner.property_product_pricelist
            if pricelist and pricelist.restrict_to_contacts:
                allowed_partners = pricelist.allowed_partner_ids
                # Permitimos si el contacto mismo o su contacto comercial principal están permitidos
                if partner not in allowed_partners and partner.commercial_partner_id not in allowed_partners:
                    raise ValidationError(_(
                        "La lista de precios '%s' está restringida y no puede ser asignada al contacto '%s' porque no está en la lista de contactos autorizados."
                    ) % (pricelist.display_name, partner.name))
