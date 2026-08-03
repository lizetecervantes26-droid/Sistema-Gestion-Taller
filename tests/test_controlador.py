import sys
import os

sys.path.append(os.path.dirname(os.path.dirname(__file__)))

import pytest

from controlador_serv import ControladorServicios
from exceptions.costo_invalido import CostoInvalidoError
from exceptions.servicio_no_encontrado import ServicioNoEncontradoError


def test_costo_menor_a_cero():

    controlador = ControladorServicios()

    with pytest.raises(CostoInvalidoError):
        controlador.registrar(
            "Juan",
            "Jetta",
            "Cambio de aceite",
            -500
        )


def test_cliente_vacio():

    controlador = ControladorServicios()

    with pytest.raises(ValueError):
        controlador.registrar(
            "",
            "Jetta",
            "Cambio de aceite",
            500
        )


def test_vehiculo_vacio():

    controlador = ControladorServicios()

    with pytest.raises(ValueError):
        controlador.registrar(
            "Juan",
            "",
            "Cambio de aceite",
            500
        )


def test_tipo_servicio_vacio():

    controlador = ControladorServicios()

    with pytest.raises(ValueError):
        controlador.registrar(
            "Juan",
            "Jetta",
            "",
            500
        )


def test_eliminar_servicio_inexistente():

    controlador = ControladorServicios()

    with pytest.raises(ServicioNoEncontradoError):
        controlador.eliminar(99999)