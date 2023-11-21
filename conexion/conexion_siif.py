import jaydebeapi
import ibm_db
import os


def db2_connection():
    db2_url = "jdbc:as400://172.18.115.7/FINESAAS"
    db2_user = "USUARIOPHP"
    db2_password = "S0p0rt3#"
    jt400_jar = "jt400.jar"
   # print(os.getcwd())
    
    try:    
      db2_connection = jaydebeapi.connect("com.ibm.as400.access.AS400JDBCDriver", 
                                 db2_url, 
                                 [db2_user, db2_password], 
                                 jt400_jar
                                  ) 
      print(f"Conection DB2 OK")
      return db2_connection
    
    except Exception as e:
        print(f"Error connecting to DB2: {e}")
        return None
        
#db2_connection()
        
