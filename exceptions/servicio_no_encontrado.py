class ServicioNoEncontradoError(Exception):

    def __init__(self, mensaje="No se encontró el servicio."):
        super().__init__(mensaje)