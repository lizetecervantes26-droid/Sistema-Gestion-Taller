import mysql.connector

class Conexion:

    @staticmethod
    def conectar():
        return mysql.connector.connect(
            host="localhost",
            user="root",
            password="",
            database="taller_mecanico",
            port=3308
        )