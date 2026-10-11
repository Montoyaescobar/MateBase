"""
Tema 3: Manejo de constantes y coeficientes (nivel Calculo II).

facil   -> sacar la constante de la integral, multiplicar coeficientes
    fraccionarios, distribuir una constante (con signos)
medio   -> reescribir en la forma c·xⁿ (lo que se hace antes de
    integrar), simplificar cocientes, sacar factor comun
dificil -> coeficiente al integrar (+ C), hallar la constante k de una
    antiderivada, ajustar dx en una sustitucion u = bx + c
"""
import math
import random
from fractions import Fraction

from core.formato import monomio, numero, polinomio, potencia, potencia_html, superindice
from core.formato import monomio_html, numero_html, polinomio_html  # HTML versions for display
from core.opciones import armar_opciones_texto


def _no_cero(minimo, maximo):
    return random.choice([n for n in range(minimo, maximo + 1) if n != 0])


# ---------- Facil ----------

def _sacar_constante():
    from .mensajes import RECUERDAS_CONSTANTES
    k, n = random.randint(2, 9), random.randint(2, 6)
    xn = potencia_html(n)
    correcta = f"{k}∫ {xn} dx"
    candidatos = [
        f"∫ {xn} dx",                       # se pierde la constante
        f"({numero_html(Fraction(1, k))})∫ {xn} dx",                # la invierte
        f"{k}{xn}∫ dx",                     # saca tambien la variable
        f"{k * n}∫ {potencia_html(n - 1)} dx",   # deriva en lugar de factorizar
    ]

    def respaldo():
        return f"{k + _no_cero(-2, 2)}∫ {xn} dx"

    enunciado = f"Saca la constante fuera de la integral: ∫ {k}{xn} dx"
    return {
        "enunciado": enunciado,
        "correcta": correcta,
        "candidatos": candidatos,
        "respaldo": respaldo,
        "opciones": [],  # Se llenará después por armar_opciones_texto
        "indice_correcto": 0,
        "recuerda": RECUERDAS_CONSTANTES["sacar_constante"]
    }


def _producto_fracciones():
    from .mensajes import RECUERDAS_CONSTANTES
    a, b = random.randint(1, 9), random.randint(2, 9)
    c, d = random.randint(1, 9), random.randint(2, 9)
    n = random.randint(1, 5)
    valor = Fraction(a, b) * Fraction(c, d)
    correcta = monomio_html(valor, n)
    candidatos = [
        monomio_html(Fraction(a + c, b + d), n),   # suma numeradores y denominadores
        monomio_html(Fraction(a * d, b * c), n),   # divide en vez de multiplicar
        monomio_html(Fraction(a * c, b + d), n),
        monomio_html(valor, n + 1),
    ]

    def respaldo():
        return monomio_html(valor + Fraction(_no_cero(-3, 3), random.randint(2, 4)), n)

    fraccion1 = Fraction(a, b)
    fraccion2 = Fraction(c, d)
    enunciado = f"Simplifica el coeficiente: ({numero_html(fraccion1)}) · ({numero_html(fraccion2)}){potencia_html(n)}"
    return {
        "enunciado": enunciado,
        "correcta": correcta,
        "candidatos": candidatos,
        "respaldo": respaldo,
        "opciones": [],  # Se llenará después por armar_opciones_texto
        "indice_correcto": 0,
        "recuerda": RECUERDAS_CONSTANTES["producto_fracciones"]
    }


def _distribuir():
    from .mensajes import RECUERDAS_CONSTANTES
    k = _no_cero(-6, 6)
    while abs(k) == 1:
        k = _no_cero(-6, 6)
    a, n, b = random.randint(1, 5), random.randint(2, 4), _no_cero(-9, 9)
    correcta = polinomio_html([(k * a, n), (k * b, 0)])
    candidatos = [
        polinomio_html([(k * a, n), (b, 0)]),        # solo multiplica el primer termino
        polinomio_html([(k * a, n), (-k * b, 0)]),   # error de signo
        polinomio_html([(k + a, n), (k + b, 0)]),    # suma en vez de multiplicar
        polinomio_html([(a, n), (k * b, 0)]),
    ]

    def respaldo():
        return polinomio_html([(k * a, n), (k * b + _no_cero(-3, 3), 0)])

    enunciado = f"Distribuye: {k}({polinomio_html([(a, n), (b, 0)])})"
    return {
        "enunciado": enunciado,
        "correcta": correcta,
        "candidatos": candidatos,
        "respaldo": respaldo,
        "opciones": [],  # Se llenará después por armar_opciones_texto
        "indice_correcto": 0,
        "recuerda": RECUERDAS_CONSTANTES["distribuir"]
    }


# ---------- Medio ----------

def _reescribir_potencia():
    from .mensajes import RECUERDAS_CONSTANTES
    b = random.randint(2, 9)
    a = random.choice([x for x in range(1, 10) if x != b])
    n = random.randint(1, 5)
    valor = Fraction(a, b)
    correcta = monomio_html(valor, -n)
    candidatos = [
        monomio_html(valor, n),                 # olvida el signo del exponente
        monomio_html(Fraction(b, a), -n),       # invierte la fraccion
        monomio_html(a * b, -n),
        monomio_html(valor, -n + 1),
    ]

    def respaldo():
        return monomio_html(valor, -n + random.choice([-2, -1, 2]))

    enunciado = f'Reescribe en la forma c·xⁿ (para poder integrar): <span class="frac"><span class="num">{numero_html(a)}</span><span class="den">{b}{potencia_html(n)}</span></span>'
    return {
        "enunciado": enunciado,
        "correcta": correcta,
        "candidatos": candidatos,
        "respaldo": respaldo,
        "opciones": [],  # Se llenará después por armar_opciones_texto
        "indice_correcto": 0,
        "recuerda": RECUERDAS_CONSTANTES["reescribir_potencia"]
    }


def _cociente_monomios():
    from .mensajes import RECUERDAS_CONSTANTES
    a, b = random.randint(2, 12), random.randint(2, 6)
    while a == b:
        b = random.randint(2, 6)
    m, n = random.sample(range(1, 8), 2)
    valor = Fraction(a, b)
    correcta = monomio_html(valor, m - n)
    candidatos = [
        monomio_html(valor, m + n),             # suma exponentes
        monomio_html(Fraction(b, a), m - n),    # invierte el coeficiente
        monomio_html(a - b, m - n),             # resta coeficientes
        monomio_html(valor, n - m),             # resta al reves
    ]

    def respaldo():
        return monomio_html(valor, m - n + _no_cero(-2, 2))

    enunciado = f"Simplifica: ({a}{potencia_html(m)}) / ({b}{potencia_html(n)})"
    return {
        "enunciado": enunciado,
        "correcta": correcta,
        "candidatos": candidatos,
        "respaldo": respaldo,
        "opciones": [],  # Se llenará después por armar_opciones_texto
        "indice_correcto": 0,
        "recuerda": RECUERDAS_CONSTANTES["cociente_monomios"]
    }


def _factor_comun():
    from .mensajes import RECUERDAS_CONSTANTES
    g = random.randint(2, 5)
    while True:
        c1, c2, c3 = random.randint(1, 5), _no_cero(-5, 5), _no_cero(-9, 9)
        if math.gcd(math.gcd(c1, c2), c3) == 1:
            break
    n = random.randint(2, 5)
    m = random.randint(1, n - 1)
    original = [(g * c1, n), (g * c2, m), (g * c3, 0)]
    correcta = f"{g}({polinomio_html([(c1, n), (c2, m), (c3, 0)])})"
    candidatos = [
        f"{g}({polinomio_html([(c1, n), (g * c2, m), (g * c3, 0)])})",   # solo divide el primero
        f"{g}({polinomio_html([(c1, n), (-c2, m), (c3, 0)])})",           # error de signo
        f"{g}({polinomio_html([(c1, n), (c2, m), (g * c3, 0)])})",        # olvida la constante
        f"{g * c1}({polinomio_html([(1, n), (c2, m), (c3, 0)])})",
    ]

    def respaldo():
        return f"{g}({polinomio_html([(c1, n), (c2, m), (c3 + _no_cero(-3, 3), 0)])})"

    enunciado = f"Saca el máximo factor común numérico: {polinomio_html(original)}"
    return {
        "enunciado": enunciado,
        "correcta": correcta,
        "candidatos": candidatos,
        "respaldo": respaldo,
        "opciones": [],  # Se llenará después por armar_opciones_texto
        "indice_correcto": 0,
        "recuerda": RECUERDAS_CONSTANTES["factor_comun"]
    }


# ---------- Dificil ----------

def _coeficiente_integral():
    from .mensajes import RECUERDAS_CONSTANTES
    a, n = random.randint(1, 9), random.randint(1, 6)
    correcta = f"{monomio_html(Fraction(a, n + 1), n + 1)} + C"
    candidatos = [
        f"{monomio_html(Fraction(a, n), n + 1)} + C",       # divide entre n y no n+1
        f"{monomio_html(a * (n + 1), n + 1)} + C",          # multiplica en vez de dividir
        monomio_html(Fraction(a, n + 1), n + 1),            # olvida la constante C
        f"{monomio_html(a * n, n - 1)} + C",                # deriva en vez de integrar
    ]

    def respaldo():
        divisor = random.choice([d for d in range(2, n + 5) if d != n + 1])
        return f"{monomio_html(Fraction(a, divisor), n + 1)} + C"

    enunciado = f"Calcula: ∫ {monomio_html(a, n)} dx"
    return {
        "enunciado": enunciado,
        "correcta": correcta,
        "candidatos": candidatos,
        "respaldo": respaldo,
        "opciones": [],  # Se llenará después por armar_opciones_texto
        "indice_correcto": 0,
        "recuerda": RECUERDAS_CONSTANTES["coeficiente_integral"]
    }


def _hallar_k():
    from .mensajes import RECUERDAS_CONSTANTES
    n, m = random.randint(2, 6), random.randint(1, 12)
    k = Fraction(m, n)
    correcta = numero_html(k)
    candidatos = [numero_html(m * n), numero_html(Fraction(m, n - 1)),
                  numero_html(Fraction(m, n + 1)), numero_html(m)]

    def respaldo():
        return numero_html(k + Fraction(_no_cero(-2, 2), random.randint(1, 3)))

    enunciado = (f"¿Qué constante k cumple que la derivada de k·{potencia_html(n)} "
                 f"sea {monomio_html(m, n - 1)}?")
    return {
        "enunciado": enunciado,
        "correcta": correcta,
        "candidatos": candidatos,
        "respaldo": respaldo,
        "opciones": [],  # Se llenará después por armar_opciones_texto
        "indice_correcto": 0,
        "recuerda": RECUERDAS_CONSTANTES["hallar_k"]
    }


def _ajuste_sustitucion():
    from .mensajes import RECUERDAS_CONSTANTES
    b, c, n = random.randint(2, 9), _no_cero(-9, 9), random.randint(2, 8)
    u = polinomio([(b, 1), (c, 0)])
    correcta = f'<span class="frac"><span class="num">du</span><span class="den">{b}</span></span>'
    candidatos = [f"{b} du", "du", f'<span class="frac"><span class="num">du</span><span class="den">({u})</span></span>', f'<span class="frac"><span class="num">du</span><span class="den">{n}</span></span>']

    def respaldo():
        divisor = random.choice([d for d in range(2, 12) if d != b])
        return f'<span class="frac"><span class="num">du</span><span class="den">{divisor}</span></span>'

    enunciado = f"En ∫ ({u}){potencia_html(n, '')} dx se usa u = {u}. ¿A qué es igual dx?"
    return {
        "enunciado": enunciado,
        "correcta": correcta,
        "candidatos": candidatos,
        "respaldo": respaldo,
        "opciones": [],  # Se llenará después por armar_opciones_texto
        "indice_correcto": 0,
        "recuerda": RECUERDAS_CONSTANTES["ajuste_sustitucion"]
    }


PLANTILLAS = {
    "facil": [_sacar_constante, _producto_fracciones, _distribuir],
    "medio": [_reescribir_potencia, _cociente_monomios, _factor_comun],
    "dificil": [_coeficiente_integral, _hallar_k, _ajuste_sustitucion],
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
