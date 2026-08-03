from repositorio_serv import RepositorioServicios
from servicio import Servicio
from exceptions.costo_invalido import CostoInvalidoError
from exceptions.servicio_no_encontrado import ServicioNoEncontradoError


class ControladorServicios:

    def __init__(self):
        self.repositorio = RepositorioServicios()

    # Registrar
    def registrar(self, cliente, vehiculo, tipo_servicio, costo):

        if cliente.strip() == "":
            raise ValueError("El cliente es obligatorio.")

        if vehiculo.strip() == "":
            raise ValueError("El vehículo es obligatorio.")

        if tipo_servicio.strip() == "":
            raise ValueError("El tipo de servicio es obligatorio.")

        if float(costo) <= 0:
            raise CostoInvalidoError()

        servicio = Servicio(
            None,
            cliente,
            vehiculo,
            tipo_servicio,
            float(costo)
        )

        self.repositorio.insertar(servicio)

    # Mostrar
    def mostrar(self):
        return self.repositorio.mostrar()

    # Buscar
    def buscar(self, id):
        return self.repositorio.buscar(id)

# Buscar general
    def buscar(self, id):

        servicio = self.repositorio.buscar(id)

        if servicio is None:
            raise ServicioNoEncontradoError()

        return servicio

    # Actualizar
    def actualizar(self, id, cliente, vehiculo, tipo_servicio, costo):
        if float(costo) <= 0:
            raise CostoInvalidoError()
        
        servicio = Servicio(
            id,
            cliente,
            vehiculo,
            tipo_servicio,
            float(costo)
        )

        self.repositorio.actualizar(servicio)

    # Eliminar
    def eliminar(self, id):

        servicio = self.repositorio.buscar(id)

        if servicio is None:
            raise ServicioNoEncontradoError()

        self.repositorio.eliminar(id)