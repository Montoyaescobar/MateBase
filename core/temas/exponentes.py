"""
Tema 1: Leyes de los exponentes y potencias.

facil   -> producto y cociente de potencias de igual base
medio   -> potencia de una potencia (con producto y con coeficiente)
dificil -> exponentes negativos

Los distractores representan errores tipicos: multiplicar en vez de
sumar exponentes, sumar en vez de multiplicar, olvidar elevar el
coeficiente, errores de signo, etc.
"""
import random

from core.formato import potencia, potencia_html, superindice
from core.opciones import armar_opciones_texto


INSTRUCCION = "Simplifica (escribe el resultado como una sola potencia):"


def _respaldo_exponente(correcto):
    def generar():
        return potencia_html(correcto + random.choice([-3, -2, -1, 1, 2, 3]))
    return generar


def _pregunta_de_exponente(expresion, correcto, candidatos):
    """Para preguntas cuya respuesta es x elevado a un exponente."""
    return (
        f"{INSTRUCCION} {expresion}",
        potencia_html(correcto),
        [potencia_html(c) for c in candidatos],
        _respaldo_exponente(correcto),
    )


# ---------- Facil: producto y cociente ----------

def _producto():
    from .mensajes import RECUERDAS_EXPONENTES
    a, b = random.randint(2, 9), random.randint(2, 9)
    r = a + b
    enunciado, correcta, candidatos, respaldo = _pregunta_de_exponente(
        f"{potencia_html(a)} · {potencia_html(b)}", r,
        [a * b, abs(a - b), r + 1, r - 1],
    )
    return {
        "enunciado": enunciado,
        "correcta": correcta,
        "candidatos": candidatos,
        "respaldo": respaldo,
        "opciones": [],  # Se llenará después por armar_opciones_texto
        "indice_correcto": 0,
        "recuerda": RECUERDAS_EXPONENTES["producto"]
    }


def _cociente():
    from .mensajes import RECUERDAS_EXPONENTES
    b = random.randint(2, 6)
    a = b + random.randint(2, 7)
    r = a - b
    candidatos = [a + b, b - a, r + 1, r - 1]  # b - a: error de signo
    if a % b == 0:
        candidatos.append(a // b)  # dividir exponentes
    enunciado, correcta, candidatos, respaldo = _pregunta_de_exponente(f"{potencia_html(a)} / {potencia_html(b)}", r, candidatos)
    return {
        "enunciado": enunciado,
        "correcta": correcta,
        "candidatos": candidatos,
        "respaldo": respaldo,
        "opciones": [],  # Se llenará después por armar_opciones_texto
        "indice_correcto": 0,
        "recuerda": RECUERDAS_EXPONENTES["cociente"]
    }


# ---------- Medio: potencia de potencia ----------

def _potencia_de_potencia():
    from .mensajes import RECUERDAS_EXPONENTES
    a, b = random.randint(2, 6), random.randint(2, 5)
    r = a * b
    candidatos = [a + b, r + 1, r - a]
    if a ** b <= 200:
        candidatos.append(a ** b)
    enunciado, correcta, candidatos, respaldo = _pregunta_de_exponente(f"({potencia_html(a)}){potencia_html(b, '')}", r, candidatos)
    return {
        "enunciado": enunciado,
        "correcta": correcta,
        "candidatos": candidatos,
        "respaldo": respaldo,
        "opciones": [],  # Se llenará después por armar_opciones_texto
        "indice_correcto": 0,
        "recuerda": RECUERDAS_EXPONENTES["potencia_de_potencia"]
    }


def _potencia_por_producto():
    from .mensajes import RECUERDAS_EXPONENTES
    a, b, c = random.randint(2, 5), random.randint(2, 4), random.randint(2, 6)
    r = a * b + c
    enunciado, correcta, candidatos, respaldo = _pregunta_de_exponente(
        f"({potencia_html(a)}){potencia_html(b, '')} · {potencia_html(c)}", r,
        [a * (b + c), a + b + c, a * b * c, r + 1],
    )
    return {
        "enunciado": enunciado,
        "correcta": correcta,
        "candidatos": candidatos,
        "respaldo": respaldo,
        "opciones": [],  # Se llenará después por armar_opciones_texto
        "indice_correcto": 0,
        "recuerda": RECUERDAS_EXPONENTES["potencia_por_producto"]
    }


def _coeficiente_elevado():
    from .mensajes import RECUERDAS_EXPONENTES
    k, a, b = random.randint(2, 3), random.randint(2, 5), random.randint(2, 3)
    correcta = f"{k ** b}{potencia_html(a * b)}"
    candidatos = [
        f"{k}{potencia_html(a * b)}",          # olvido elevar el coeficiente
        f"{k * b}{potencia_html(a * b)}",      # multiplico coeficiente por b
        f"{k ** b}{potencia_html(a + b)}",     # sumo exponentes
        f"{k * b}{potencia_html(a + b)}",
    ]

    def respaldo():
        return f"{k ** b + random.choice([-2, -1, 1, 2])}{potencia_html(a * b)}"

    enunciado = f"Simplifica: ({k}{potencia_html(a)}){potencia_html(b, '')}"
    return {
        "enunciado": enunciado,
        "correcta": correcta,
        "candidatos": candidatos,
        "respaldo": respaldo,
        "opciones": [],  # Se llenará después por armar_opciones_texto
        "indice_correcto": 0,
        "recuerda": RECUERDAS_EXPONENTES["coeficiente_elevado"]
    }


# ---------- Dificil: exponentes negativos ----------

def _cociente_negativo():
    from .mensajes import RECUERDAS_EXPONENTES
    a = random.randint(2, 6)
    b = a + random.randint(2, 6)
    r = a - b  # negativo
    enunciado, correcta, candidatos, respaldo = _pregunta_de_exponente(
        f"{potencia_html(a)} / {potencia_html(b)}", r,
        [b - a, a + b, r - 1, r + 1],
    )
    return {
        "enunciado": enunciado,
        "correcta": correcta,
        "candidatos": candidatos,
        "respaldo": respaldo,
        "opciones": [],  # Se llenará después por armar_opciones_texto
        "indice_correcto": 0,
        "recuerda": RECUERDAS_EXPONENTES["cociente_negativo"]
    }


def _potencia_negativa():
    from .mensajes import RECUERDAS_EXPONENTES
    a, b = random.randint(2, 6), random.randint(2, 4)
    r = -a * b
    enunciado, correcta, candidatos, respaldo = _pregunta_de_exponente(
        f"({potencia_html(-a)}){potencia_html(b, '')}", r,
        [a * b, -a + b, -a - b, r + 1],
    )
    return {
        "enunciado": enunciado,
        "correcta": correcta,
        "candidatos": candidatos,
        "respaldo": respaldo,
        "opciones": [],  # Se llenará después por armar_opciones_texto
        "indice_correcto": 0,
        "recuerda": RECUERDAS_EXPONENTES["potencia_negativa"]
    }


def _producto_negativo():
    from .mensajes import RECUERDAS_EXPONENTES
    a = random.randint(3, 9)
    b = random.choice([n for n in range(2, 9) if n != a])
    r = b - a
    enunciado, correcta, candidatos, respaldo = _pregunta_de_exponente(
        f"{potencia_html(-a)} · {potencia_html(b)}", r,
        [-(a + b), a + b, -a * b, a - b],
    )
    return {
        "enunciado": enunciado,
        "correcta": correcta,
        "candidatos": candidatos,
        "respaldo": respaldo,
        "opciones": [],  # Se llenará después por armar_opciones_texto
        "indice_correcto": 0,
        "recuerda": RECUERDAS_EXPONENTES["producto_negativo"]
    }


def _combinado():
    from .mensajes import RECUERDAS_EXPONENTES
    a, b = random.randint(2, 3), random.randint(2, 3)
    c = a * b + random.randint(1, 5)
    r = a * b - c  # negativo
    enunciado, correcta, candidatos, respaldo = _pregunta_de_exponente(
        f"({potencia_html(a)}){potencia_html(b, '')} / {potencia_html(c)}", r,
        [a + b - c, a * b + c, c - a * b, a * (b - c)],
    )
    return {
        "enunciado": enunciado,
        "correcta": correcta,
        "candidatos": candidatos,
        "respaldo": respaldo,
        "opciones": [],  # Se llenará después por armar_opciones_texto
        "indice_correcto": 0,
        "recuerda": RECUERDAS_EXPONENTES["combinado"]
    }


def _sin_negativos():
    from .mensajes import RECUERDAS_EXPONENTES
    k, n = random.randint(2, 9), random.randint(2, 6)
    correcta = f"{k}/{potencia_html(n)}"
    candidatos = [
        f"1/({k}{potencia_html(n)})",   # paso el coeficiente al denominador
        f"-{k}{potencia_html(n)}",      # confundio exponente negativo con signo
        f"{k}{potencia_html(n)}",
        f"-{k}/{potencia_html(n)}",
    ]

    def respaldo():
        return f"{k}/{potencia_html(n + random.choice([-1, 1, 2]))}"

    enunciado = f"Escribe sin exponentes negativos: {k}{potencia_html(-n)}"
    return {
        "enunciado": enunciado,
        "correcta": correcta,
        "candidatos": candidatos,
        "respaldo": respaldo,
        "opciones": [],  # Se llenará después por armar_opciones_texto
        "indice_correcto": 0,
        "recuerda": RECUERDAS_EXPONENTES["sin_negativos"]
    }


PLANTILLAS = {
    "facil": [_producto, _cociente],
    "medio": [_potencia_de_potencia, _potencia_por_producto, _coeficiente_elevado],
    "dificil": [_cociente_negativo, _potencia_negativa, _producto_negativo,
                _combinado, _sin_negativos],
}


def generar(dificultad):
    ejercicio = random.choice(PLANTILLAS[dificultad])()
    enunciado = ejercicio["enunciado"]
    correcta = ejercicio["correcta"]
    candidatos = ejercicio["candidatos"]
    respaldo = ejercicio["respaldo"]
    recuerda = ejercicio["recuerda"]
    opciones, indice = armar_opciones_texto(correcta, candidatos, respaldo)
    return {"enunciado": enunciado, "opciones": opciones, "indice_correcto": indice, "recuerda": recuerda}
