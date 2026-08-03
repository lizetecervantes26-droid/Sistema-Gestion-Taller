import sys
import os

sys.path.append(os.path.dirname(os.path.dirname(__file__)))

from repositorio_serv import RepositorioServicios
from servicio import Servicio


def test_insertar_servicio():

    # Arrange
    repo = RepositorioServicios()

    servicio = Servicio(
        None,
        "PRUEBA PYTEST",
        "AUTO PYTEST",
        "SERVICIO PYTEST",
        999
    )

    # Act
    repo.insertar(servicio)

    # Assert
    registros = repo.buscar_general("PRUEBA PYTEST")

    assert len(registros) > 0

    # Limpiar la BD
    for registro in registros:
        repo.eliminar(registro[0])

def test_mostrar_servicios():

    # Arrange
    repo = RepositorioServicios()

    # Act
    registros = repo.mostrar()

    # Assert
    assert isinstance(registros, list)

def test_buscar_servicio():

    # Arrange
    repo = RepositorioServicios()

    servicio = Servicio(
        None,
        "BUSCAR PYTEST",
        "JETTA",
        "CAMBIO",
        500
    )

    repo.insertar(servicio)

    registros = repo.buscar_general("BUSCAR PYTEST")
    id_servicio = registros[0][0]

    # Act
    encontrado = repo.buscar(id_servicio)

    # Assert
    assert encontrado is not None
    assert encontrado[1] == "BUSCAR PYTEST"

    # Limpiar
    repo.eliminar(id_servicio)

def test_actualizar_servicio():

    repo = RepositorioServicios()

    servicio = Servicio(
        None,
        "ACTUALIZAR",
        "AUTO",
        "SERVICIO",
        100
    )

    repo.insertar(servicio)

    registros = repo.buscar_general("ACTUALIZAR")
    id_servicio = registros[0][0]

    servicio_actualizado = Servicio(
        id_servicio,
        "ACTUALIZADO",
        "AUTO",
        "SERVICIO",
        300
    )

    repo.actualizar(servicio_actualizado)

    actualizado = repo.buscar(id_servicio)

    assert actualizado[1] == "ACTUALIZADO"
    assert actualizado[4] == 300

    repo.eliminar(id_servicio)

def test_eliminar_servicio():

    repo = RepositorioServicios()

    servicio = Servicio(
        None,
        "ELIMINAR",
        "AUTO",
        "SERVICIO",
        200
    )

    repo.insertar(servicio)

    registros = repo.buscar_general("ELIMINAR")
    id_servicio = registros[0][0]

    repo.eliminar(id_servicio)

    eliminado = repo.buscar(id_servicio)

    assert eliminado is None