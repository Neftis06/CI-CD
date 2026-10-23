import pytest

from calculadora import calcular_descuento, dividir, sumar, calcular_envio


@pytest.mark.parametrize(
    ("a", "b", "esperado"),
    [(2, 3, 5), (-3, 2, -1), (0, 0, 0)],
)
def test_sumar(a: float, b: float, esperado: float) -> None:
    assert sumar(a, b) == esperado


def test_dividir() -> None:
    assert dividir(10, 2) == 5


def test_dividir_entre_cero() -> None:
    with pytest.raises(ValueError, match="dividir entre cero"):
        dividir(10, 0)


def test_calcular_descuento() -> None:
    assert calcular_descuento(200, 10) == 180
    assert calcular_descuento(100, 0) == 100
    assert calcular_descuento(100, 100) == 0


def test_rechaza_precio_negativo() -> None:
    with pytest.raises(ValueError, match="precio"):
        calcular_descuento(-100, 10)


@pytest.mark.parametrize("porcentaje", [-1, 101])
def test_rechaza_descuento_fuera_de_rango(porcentaje: float) -> None:
    with pytest.raises(ValueError, match="descuento"):
        calcular_descuento(100, porcentaje)

@pytest.mark.parametrize(
    ("compra", "distancia", "express", "esperado"),
    [
        (1000, 10, False, 0.0),    # Envío gratis
        (500, 4, False, 50.0),     # Distancia corta
        (500, 10, False, 90.0),    # Distancia media
        (500, 30, False, 150.0),   # Distancia larga
        (500, 10, True, 160.0),    # Recargo express (90 + 70)
    ],
)
def test_calcular_envio_exitoso(compra: float, distancia: int, express: bool, esperado: float) -> None:
    assert calcular_envio(compra, distancia, express) == esperado


def test_calcular_envio_errores() -> None:
    # Total negativo
    with pytest.raises(ValueError, match="total de la compra no puede ser negativo"):
        calcular_envio(-1, 3, False)
    
    # Distancia negativa
    with pytest.raises(ValueError, match="distancia no puede ser negativa"):
        calcular_envio(200, -1, False)