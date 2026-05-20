# -*- coding: utf-8 -*-
{
    'name': 'Restricción de Asignación de Tarifa',
    'version': '17.0.1.0.0',
    'category': 'Sales',
    'summary': 'Bloquea tarifas para que solo puedan asignarse a contactos autorizados',
    'description': """
Módulo para Odoo 17 que permite restringir listas de precios/tarifas para que solo se puedan asignar en la ficha del contacto o en el pedido de venta de los contactos seleccionados.
    """,
    'author': 'TecnoSegura',
    'website': 'https://www.tecnosegura.com',
    'license': 'LGPL-3',
    'depends': ['sale_management'],
    'data': [
        'views/product_pricelist_views.xml',
        'views/res_partner_views.xml',
        'views/sale_order_views.xml',
    ],
    'installable': True,
    'application': False,
    'auto_install': False,
}
