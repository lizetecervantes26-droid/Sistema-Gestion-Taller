from conexion import Conexion
from servicio import Servicio


class RepositorioServicios:

    # INSERT
    def insertar(self, servicio):

        conexion = Conexion.conectar()
        cursor = conexion.cursor()

        sql = """
        INSERT INTO servicios(cliente, vehiculo, tipo_servicio, costo)
        VALUES (%s, %s, %s, %s)
        """

        datos = (
            servicio.cliente,
            servicio.vehiculo,
            servicio.tipo_servicio,
            servicio.costo
        )

        cursor.execute(sql, datos)
        conexion.commit()

        cursor.close()
        conexion.close()

        print("Servicio registrado correctamente.")

    def mostrar(self):

        conexion = Conexion.conectar()
        cursor = conexion.cursor()

        sql = "SELECT * FROM servicios"

        cursor.execute(sql)

        registros = cursor.fetchall()

        cursor.close()
        conexion.close()

        return registros

        # BUSCAR POR ID
    def buscar(self, id):

        conexion = Conexion.conectar()
        cursor = conexion.cursor()

        sql = "SELECT * FROM servicios WHERE id = %s"

        cursor.execute(sql, (id,))

        servicio = cursor.fetchone()

        cursor.close()
        conexion.close()

        return servicio

# BUSCAR GENERAL
    def buscar_general(self, texto):

        conexion = Conexion.conectar()
        cursor = conexion.cursor()

        sql = """
        SELECT *
        FROM servicios
        WHERE cliente LIKE %s
        OR vehiculo LIKE %s
        OR tipo_servicio LIKE %s
        OR CAST(costo AS CHAR) LIKE %s
        """

        parametro = f"%{texto}%"

        cursor.execute(
            sql,
            (parametro, parametro, parametro, parametro)
        )

        registros = cursor.fetchall()

        cursor.close()
        conexion.close()

        return registros

        # ACTUALIZAR
    def actualizar(self, servicio):

        conexion = Conexion.conectar()
        cursor = conexion.cursor()

        sql = """
        UPDATE servicios
        SET cliente=%s,
            vehiculo=%s,
            tipo_servicio=%s,
            costo=%s
        WHERE id=%s
        """

        datos = (
            servicio.cliente,
            servicio.vehiculo,
            servicio.tipo_servicio,
            servicio.costo,
            servicio.id
        )

        cursor.execute(sql, datos)
        conexion.commit()

        cursor.close()
        conexion.close()

        print("Servicio actualizado correctamente.")

        # ELIMINAR
    def eliminar(self, id):

        conexion = Conexion.conectar()
        cursor = conexion.cursor()

        sql = "DELETE FROM servicios WHERE id=%s"

        cursor.execute(sql, (id,))

        conexion.commit()

        cursor.close()
        conexion.close()

        print("Servicio eliminado correctamente.")