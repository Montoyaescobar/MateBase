"""Tema 2: Raices cuadradas y radicales."""
import random
from core.formato import potencia, potencia_html
from core.opciones import armar_opciones


def generar(dificultad):
    from .mensajes import RECUERDAS_RADICALES
    if dificultad == "facil":
        n = random.randint(2, 8) * 2
        correcta = n // 2
        enunciado = f"Simplifica: √({potencia_html(n)})"
        candidatos = [n, n * 2, correcta + 1, correcta - 1]
        recuerda = RECUERDAS_RADICALES["facil"]

    elif dificultad == "medio":
        n = random.randint(2, 8) * 3
        correcta = n // 3
        enunciado = f"Simplifica: ∛({potencia_html(n)})"
        candidatos = [n, n // 2, correcta + 2, correcta - 2]
        recuerda = RECUERDAS_RADICALES["medio"]

    else:
        a, b = random.randint(2, 6) * 2, random.randint(2, 6) * 2
        n = a + b
        correcta = n // 2
        enunciado = f"Simplifica: √({potencia_html(a)} · {potencia_html(b)})"
        candidatos = [a + b, (a // 2) + (b // 2) + 1, correcta + 3, correcta - 3]
        recuerda = RECUERDAS_RADICALES["dificil"]

    opciones_num, indice = armar_opciones(correcta, lambda: random.choice(candidatos))
    opciones = [potencia_html(o) for o in opciones_num]
    return {"enunciado": enunciado, "opciones": opciones, "indice_correcto": indice, "recuerda": recuerda}
