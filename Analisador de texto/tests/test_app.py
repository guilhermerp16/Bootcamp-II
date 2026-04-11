from app.main import (
    contar_caracteres,
    contar_palavras,
    limpar_texto,
    mostrar_top_palavras
)


def test_contar_caracteres():
    resultado = contar_caracteres("aaa")
    assert resultado["a"] == 3


def test_contar_palavras():
    resultado = contar_palavras("ola ola mundo")
    assert resultado["ola"] == 2
    assert resultado["mundo"] == 1


def test_limpar_texto():
    texto = "Olá, mundo!!!"
    resultado = limpar_texto(texto)
    assert resultado == "olá mundo"


def test_top_palavras():
    contador = {"a": 5, "b": 2, "c": 1}
    top = mostrar_top_palavras(contador, limite=2)
    assert top[0][0] == "a"
    assert len(top) == 2
