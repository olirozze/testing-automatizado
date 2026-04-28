import pytest
from app.descuentos import calcular_precio_final


def test_descuento_valido():
    resultado = calcular_precio_final(1000, 20)
    assert resultado == 800


def test_descuento_invalido():
    with pytest.raises(ValueError):
        calcular_precio_final(1000, 120)


def test_descuento_total_edge_case():
    resultado = calcular_precio_final(2000, 100)
    assert resultado == 0
