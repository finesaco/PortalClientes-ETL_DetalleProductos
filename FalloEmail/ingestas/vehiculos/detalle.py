import pandas as pd
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import smtplib
from datetime import datetime
import string 

#fecha y hora actual
fecha = datetime.now()
fecha_actual = fecha.strftime('%Y-%m-%d %H:%M')

#credenciales de correo electronico
# crear instancia de objeto de mensaje
msg = MIMEMultipart()

server = smtplib.SMTP('smtp.office365.com')
msg['From'] = "reportanalitica@finesa.com.co"
password = "8L5sQ]Jslkzv[1Y"


message = "Cordial saludo; \n\nEl ETL detalle productofn falló en su ingesta para la fecha: "+fecha_actual
msg.attach(MIMEText(message, 'plain'))
server.starttls()
server.login(msg['From'], password)
msg['To'] = "freddyarteaga@finesa.com.co,leinercruz@finesa.com.co,mariaparra@finesa.com.co,brendagarcia@finesa.com.co"
msg['Subject'] = "IMPORTANTE: FALLA EN ETL DETALLE VH "+fecha_actual
server.sendmail(msg['From'], msg['To'].split(","), msg.as_string())
server.quit()
