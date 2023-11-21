import mysql.connector

try:
    credenciales = {
        "host": '172.18.115.53',    # Cambia esto al host de tu base de datos MariaDB
        "user": 'desarrollo1',   # Cambia esto a tu nombre de usuario
        "password": 'P4ssw0rd23.*',  # Cambia esto a tu contraseña
        "database": 'portal_clientes'  # Cambia esto al nombre de tu base de datos
    }

    print("Conexión a MariaDB exitosa")
    conn_mariaBD_portal = mysql.connector.connect(**credenciales)
    
    # Aquí puedes realizar operaciones en tu base de datos MariaDB
    
except mysql.connector.Error as e:
    print("Ocurrió un error al conectar a MariaDB: ", e)