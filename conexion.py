import mysql.connector

def conectar():
    try:
        db = mysql.connector.connect(
            host="localhost",
            user="root",
            passwd="",
            database="coltis_task_python",
            port=3306
        )
        print("Se ha conectado a la aplicación")

        return db
    except Exception as ex:
        print("Error al conectarse a la base de datos", ex)