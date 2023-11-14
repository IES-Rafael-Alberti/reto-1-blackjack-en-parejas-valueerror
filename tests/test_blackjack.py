from src.blackjack import dar_Carta, imprimir_Mano, comprobar_Ganador
import pytest


@pytest.mark.parametrize(
    "input_n1, input_n2, input_n3, input_n4, input_n5, input_n6, input_n7, input_n8, expected",
    [
        ("A234567890JQKA234567890JQKA234567890JQKA234567890JQK", "CCCCCCCCCCCCCTTTTTTTTTTTTTPPPPPPPPPPPPPDDDDDDDDDDDDD", 3, "", "", 0, False, False, "4&4&C&4&False&False"),
        ("A234567890JQKA234567890JQKA234567890JQKA234567890JQK", "CCCCCCCCCCCCCTTTTTTTTTTTTTPPPPPPPPPPPPPDDDDDDDDDDDDD", 3, "3", "C", 3, False, False, "4&34&CC&7&False&False"),
        ("A234567890JQKA234567890JQKA234567890JQKA234567890JQK", "CCCCCCCCCCCCCTTTTTTTTTTTTTPPPPPPPPPPPPPDDDDDDDDDDDDD", 0, "A", "D", 11, False, True, "1&AA&DC&12&True&True"),
        ("A234567890JQKA234567890JQKA234567890JQKA234567890JQK", "CCCCCCCCCCCCCTTTTTTTTTTTTTPPPPPPPPPPPPPDDDDDDDDDDDDD", 5, "A", "D", 11, False, True, "6&A6&DC&17&False&True")
    ]
)


def test_dar_Carta_params(input_n1, input_n2, input_n3, input_n4, input_n5, input_n6, input_n7, input_n8, expected):
    assert dar_Carta(input_n1, input_n2, input_n3, input_n4, input_n5, input_n6, input_n7, input_n8) == (expected)


@pytest.mark.parametrize(
    "input_n1, input_n2, input_n3, input_n4, input_n5, expected",
    [
        ("A", "C", False, False, 11, "Un As de Corazones\n\nValor mano: 11\n__________________________"),
        ("A4", "CC", False, True, 15, "Un As de Corazones\nUn 4 de Corazones\n\nValor mano: 15\n__________________________"),
        ("AA", "CD", True, True, 12, "Un As de Corazones\nUn As de Diamantes\n\nValor mano: 12\n__________________________"),
        ("K", "T", False, False, 10, "Un Rey de Tréboles\n\nValor mano: 10\n__________________________")
    ]
)


def test_imprimir_Mano(input_n1, input_n2, input_n3, input_n4, input_n5, expected):
    assert imprimir_Mano(input_n1, input_n2, input_n3, input_n4, input_n5) == (expected)


@pytest.mark.parametrize(
    "input_n1, input_n2, input_n3, input_n4, input_n5, expected",
    [
        (22, 25, 3, "Manuel", "Fran", "JUEGO TERMINADO - Ronda 3&Game over ¡Los dos os habéis pasado!"),
        (19, 25, 3, "&", "Fran", "JUEGO TERMINADO - Ronda 3&¡Gana J1 - &!"),
        (12, 12, 1, "Manuel", "Fran", "JUEGO TERMINADO - Ronda 1&¡Empate!"),
        (22, 13, 3, "Bhxj", "15 ", "JUEGO TERMINADO - Ronda 3&¡Gana J2 - 15 !")
    ]
)


def test_comprobar_Ganador(input_n1, input_n2, input_n3, input_n4, input_n5, expected):
    assert comprobar_Ganador(input_n1, input_n2, input_n3, input_n4, input_n5) == (expected)


