#!/bin/bash
echo 'ejecuta etl'
cd '/home/administrador/pentaho/data-integration/'
sh '/home/administrador/pentaho/data-integration/kitchen.sh' -file:/home/portal/PortalClientes-ETL_DetalleProductos/Job_DetalleProductos.kjb " -param:CUENTA=PentahoBot"
