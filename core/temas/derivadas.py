"""
Tema 4: Derivadas basicas. Se pide siempre la derivada completa.

  facil   -> un monomio c·xⁿ (a veces con una constante sumada)
  medio   -> polinomios de 3 o 4 terminos con coeficientes negativos
  dificil -> exponentes negativos (c/xⁿ) y raices (√x)

Una funcion se representa como lista de terminos (coeficiente, exponente).
Los distractores aplican errores tipicos sobre esa lista: olvidar
multiplicar por el exponente, no restar 1 al exponente, conservar la
constante, sumar 1 en vez de restar, perder el signo negativo, etc.
"""
import random
from fractions import Fraction

from core.formato import polinomio, polinomio_html
from core.opciones import armar_opciones_texto



def _no_cero(minimo, maximo):
    return random.choice([n for n in range(minimo, maximo + 1) if n != 0])


# ---------- Derivada correcta y errores tipicos ----------

def derivar(terminos):
    return [(c * n, n - 1) for c, n in terminos if n != 0]


def _olvida_multiplicar(terminos):
    return [(c, n - 1) for c, n in terminos if n != 0]


def _no_resta_exponente(terminos):
    return [(c * n, n) for c, n in terminos if n != 0]


def _conserva_constante(terminos):
    return derivar(terminos) + [(c, n) for c, n in terminos if n == 0]


def _suma_al_exponente(terminos):
    return [(c * n, n + 1) for c, n in terminos if n != 0]


def _un_termino_sin_multiplicar(terminos):
    variables = [i for i, (_, n) in enumerate(terminos) if n not in (0, 1)]
    if not variables:
        return derivar(terminos)
    elegido = random.choice(variables)
    return [(c if i == elegido else c * n, n - 1)
            for i, (c, n) in enumerate(terminos) if n != 0]


def _pierde_signo(terminos):
    """Cambia el signo de un termino; prefiere los de exponente negativo."""
    d = derivar(terminos)
    # Solo es un error creible si hay signos negativos en juego
    if not d or all(c > 0 and n >= 0 for c, n in terminos):
        return d
    negativos = [i for i, (_, n) in enumerate(d) if n < 0]
    i = random.choice(negativos) if negativos else random.randrange(len(d))
    return [(-c if j == i else c, n) for j, (c, n) in enumerate(d)]


ERRORES = [_olvida_multiplicar, _no_resta_exponente, _conserva_constante,
           _suma_al_exponente, _un_termino_sin_multiplicar, _pierde_signo]


# ---------- Funciones segun la dificultad ----------

def _funcion_facil():
    c = random.choice([1, 2, 3, 4, 5, 6, 7, 8, 9])
    terminos = [(c, random.randint(2, 7))]
    if random.random() < 0.5:
        terminos.append((random.randint(1, 9), 0))
    return terminos


def _funcion_media():
    exponentes = sorted(random.sample(range(1, 7), 3), reverse=True)
    terminos = [(random.randint(2, 9), exponentes[0])]
    terminos += [(_no_cero(-9, 9), n) for n in exponentes[1:]]
    if random.random() < 0.5:
        terminos.append((_no_cero(-9, 9), 0))
    return terminos


def _funcion_dificil():
    plantilla = random.choice(["potencia_y_negativo", "raiz", "negativo"])
    if plantilla == "potencia_y_negativo":
        # a·xⁿ + b/xᵐ
        return [(_no_cero(-9, 9), random.randint(2, 5)),
                (_no_cero(-9, 9), -random.randint(1, 3))]
    if plantilla == "raiz":
        # a√x + b·xⁿ (+ constante)
        terminos = [(random.randint(2, 9), Fraction(1, 2)),
                    (_no_cero(-9, 9), random.randint(2, 4))]
        if random.random() < 0.5:
            terminos.append((_no_cero(-9, 9), 0))
        return terminos
    # a/xⁿ + constante
    return [(random.randint(2, 9), -random.randint(1, 4)), (_no_cero(-9, 9), 0)]


FUNCIONES = {"facil": _funcion_facil, "medio": _funcion_media, "dificil": _funcion_dificil}


def generar(dificultad):
    from .mensajes import RECUERDAS_DERIVADAS
    fraccion = dificultad == "dificil"  # escribir x⁻ⁿ como 1/xⁿ
    terminos = FUNCIONES[dificultad]()
    derivada = derivar(terminos)

    correcta = polinomio_html(derivada, fraccion)
    candidatos = [polinomio_html(error(terminos), fraccion) for error in ERRORES]

    def respaldo():
        d = list(derivada)
        i = random.randrange(len(d))
        c, n = d[i]
        if random.random() < 0.5:
            d[i] = (c + _no_cero(-3, 3), n)
        else:
            d[i] = (c, n + random.choice([-1, 1]))
        return polinomio_html(d, fraccion)

    opciones, indice = armar_opciones_texto(correcta, candidatos, respaldo)
    enunciado = f"Deriva f(x) = {polinomio_html(terminos, fraccion)}. ¿Cuál es f'(x)?"
    
    # Determinar el mensaje RECUERDA apropiado
    if dificultad == "facil":
        recuerda = RECUERDAS_DERIVADAS["facil"]
    elif dificultad == "medio":
        recuerda = RECUERDAS_DERIVADAS["medio"]
    else:  # dificil
        # Verificar si hay exponentes negativos o racionales en la función original
        tiene_negativo = any(n < 0 for _, n in terminos)
        tiene_racional = any(isinstance(n, Fraction) and n < 0 for _, n in terminos)
        if tiene_negativo or tiene_racional:
            recuerda = RECUERDAS_DERIVADAS["dificil_negativo"]
        else:
            recuerda = RECUERDAS_DERIVADAS["dificil_raiz"]
    
    return {"enunciado": enunciado, "opciones": opciones, "indice_correcto": indice, "recuerda": recuerda}
