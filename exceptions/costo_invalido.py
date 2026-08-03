class CostoInvalidoError(Exception):

    def __init__(self, mensaje="El costo debe ser mayor que cero."):
        super().__init__(mensaje)