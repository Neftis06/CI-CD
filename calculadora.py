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

def calcular_envio(total_compra: float, distancia_km: int, express: bool = False) -> float:
    """Calcula envío gratis desde $1,000; express cuesta $70 adicionales."""
    if total_compra < 0:
        raise ValueError("El total de la compra no puede ser negativo")
    if distancia_km < 0:
        raise ValueError("La distancia no puede ser negativa")
    if total_compra >= 1000:
        costo = 0
    elif distancia_km <= 5:
        costo = 50
    elif distancia_km <= 20:
        costo = 90
    else:
        costo = 150
    if express:
        costo += 70
    return float(costo)