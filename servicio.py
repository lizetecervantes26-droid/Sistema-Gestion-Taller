class Servicio:

    def __init__(self, id, cliente, vehiculo, tipo_servicio, costo):
        self.id = id
        self.cliente = cliente
        self.vehiculo = vehiculo
        self.tipo_servicio = tipo_servicio
        self.costo = costo

    def __str__(self):
        return f"""
ID: {self.id}
Cliente: {self.cliente}
Vehículo: {self.vehiculo}
Tipo de servicio: {self.tipo_servicio}
Costo: ${self.costo}
"""