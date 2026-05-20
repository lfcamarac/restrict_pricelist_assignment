# Restricción de Asignación de Tarifa (restrict_pricelist_assignment)

Este módulo para Odoo 17 permite restringir el uso de tarifas (pricelists) específicas para que solo puedan ser asignadas a contactos autorizados.

## Características

- **Bloqueo de Tarifas:** Permite marcar una tarifa como "Restringida a Contactos Seleccionados".
- **Lista de Autorización:** Define una lista de contactos permitidos para cada tarifa restringida.
- **Validación en Contactos:** Evita que se asigne una tarifa restringida a un contacto que no esté en su lista de permitidos.
- **Validación en Ventas:** Bloquea la creación de presupuestos o pedidos de venta si se intenta usar una tarifa restringida con un cliente no autorizado.
- **Filtros Dinámicos:** Los selectores de tarifas en el Formulario de Contacto y en el Pedido de Venta filtran automáticamente las tarifas para mostrar solo las permitidas.

## Instalación

1. Copie esta carpeta en su directorio de addons.
2. Actualice la lista de aplicaciones en Odoo.
3. Instale el módulo `restrict_pricelist_assignment`.

## Pruebas

El módulo incluye pruebas unitarias automatizadas. Puede ejecutarlas con el comando:
```bash
odoo-bin -c odoo.conf -i restrict_pricelist_assignment --test-enable --stop-after-init
```
