import os
def sumar(a: float, b: float) -> float:
    """Devuelve la suma de dos números."""
    return a + b


def dividir(a: float, b: float) -> float:
    """Divide dos números; no acepta cero como divisor."""
    if b == 0:
        raise ValueError("No se puede dividir entre cero")
    return a / b


def calcular_descuento(precio: float, porcentaje: float) -> float:
    """Devuelve el precio final después de aplicar el descuento."""
    if precio < 0:
        raise ValueError("El precio no puede ser negativo")
    if not 0 <= porcentaje <= 100:
        raise ValueError("El descuento debe estar entre 0 y 100")
    return round(precio * (1 - porcentaje / 100), 2)
 