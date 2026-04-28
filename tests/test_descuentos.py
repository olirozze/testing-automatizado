import pytest
from app.descuentos import calcular_precio_final

def test_descuento_valido():
    assert calcular_precio_final(1000, 20) == 800

def test_descuento_invalido():
    with pytest.raises(ValueError):
        calcular_precio_final(1000, 120)

def test_descuento_total():
    assert calcular_precio_final(2000, 100) == 0
