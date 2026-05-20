# -*- coding: utf-8 -*-

from odoo.tests import common
from odoo.exceptions import ValidationError

class TestPricelistRestriction(common.TransactionCase):

    @classmethod
    def setUpClass(cls):
        super(TestPricelistRestriction, cls).setUpClass()
        # Crear contactos de prueba
        cls.partner_a = cls.env['res.partner'].create({
            'name': 'Cliente Autorizado A',
        })
        cls.partner_b = cls.env['res.partner'].create({
            'name': 'Cliente No Autorizado B',
        })

        # Crear tarifas
        cls.pricelist_public = cls.env['product.pricelist'].create({
            'name': 'Tarifa Pública (Sin Restringir)',
            'restrict_to_contacts': False,
        })
        cls.pricelist_restricted = cls.env['product.pricelist'].create({
            'name': 'Tarifa Restringida (Solo Cliente A)',
            'restrict_to_contacts': True,
            'allowed_partner_ids': [(6, 0, [cls.partner_a.id])],
        })

    def test_01_assign_public_pricelist_allowed(self):
        """Prueba que cualquier contacto puede usar una tarifa pública/no restringida."""
        self.partner_a.property_product_pricelist = self.pricelist_public
        self.partner_b.property_product_pricelist = self.pricelist_public
        self.assertEqual(self.partner_a.property_product_pricelist, self.pricelist_public)
        self.assertEqual(self.partner_b.property_product_pricelist, self.pricelist_public)

    def test_02_assign_restricted_pricelist_authorized_allowed(self):
        """Prueba que un contacto autorizado puede tener asignada la tarifa restringida."""
        self.partner_a.property_product_pricelist = self.pricelist_restricted
        self.assertEqual(self.partner_a.property_product_pricelist, self.pricelist_restricted)

    def test_03_assign_restricted_pricelist_unauthorized_raises(self):
        """Prueba que un contacto NO autorizado lanza ValidationError al intentar asignarle la tarifa restringida."""
        with self.assertRaises(ValidationError):
            self.partner_b.property_product_pricelist = self.pricelist_restricted

    def test_04_sale_order_restricted_pricelist_authorized_allowed(self):
        """Prueba que crear un pedido de venta para un contacto autorizado con la tarifa restringida es permitido."""
        order = self.env['sale.order'].create({
            'partner_id': self.partner_a.id,
            'pricelist_id': self.pricelist_restricted.id,
        })
        self.assertEqual(order.pricelist_id, self.pricelist_restricted)

    def test_05_sale_order_restricted_pricelist_unauthorized_raises(self):
        """Prueba que crear un pedido de venta para un contacto NO autorizado con la tarifa restringida lanza ValidationError."""
        with self.assertRaises(ValidationError):
            self.env['sale.order'].create({
                'partner_id': self.partner_b.id,
                'pricelist_id': self.pricelist_restricted.id,
            })
