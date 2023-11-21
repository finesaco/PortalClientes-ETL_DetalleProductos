import pandas as pd
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import smtplib
from datetime import datetime
import string 

from conexion.conexion_siif import db2_connection
from conexion.conexion_mariaDB_portal import conn_mariaBD_portal
import ibm_db
import os

#fecha y hora actual
fecha = datetime.now()
fecha_actual = fecha.strftime('%Y-%m-%d %H:%M')

os.chdir('/home/PaymentHistory/conexion/')



#credenciales de correo electronico
# crear instancia de objeto de mensaje
msg = MIMEMultipart()

server = smtplib.SMTP('smtp.office365.com')
msg['From'] = "reportanalitica@finesa.com.co"
password = "Has20332"

#cantidad de registros tabla siif
conn = db2_connection()
cursor= conn.cursor()
cursor.execute("select count(*) as cantidad from finecontab.crehist")
df_siif = cursor.fetchone()
cantidad_siif = df_siif[0]
cursor.close()
print("cantidad siif: "+ str(cantidad_siif))

#cantidad de registros tabla portal
cursor = conn_mariaBD_portal.cursor()
cursor.execute("SELECT count(*) FROM portal_clientes.historico_pagos")
df_portal = cursor.fetchone()
cantidad_portal = df_portal[0]
cursor.close()
print("cantidad db portal "+ str(cantidad_portal))


if cantidad_siif == cantidad_portal:
    print("Los registros son iguales")
else:
    message = "Cordial saludo; \n\nEl proceso ETL Portal Historico de Pagos termino con FALLAS para la fecha: "+fecha_actual+"\n\nRegistros SIIF: "+str(cantidad_siif)+"\nRegistros db_portal: "+str(cantidad_portal)
    msg.attach(MIMEText(message, 'plain'))
    server.starttls()
    server.login(msg['From'], password)
    msg['To'] = "freddyarteaga@finesa.com.co,leinercruz@finesa.com.co,mariaparra@finesa.com.co,brendagarcia@finesa.com.co"
    msg['Subject'] = "IMPORTANTE: IMPORTANTE: PROCESO ETL HISTORICO PAGOS"
    server.sendmail(msg['From'], msg['To'].split(","), msg.as_string())
    server.quit()