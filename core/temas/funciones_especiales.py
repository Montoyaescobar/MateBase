"""Tema 5: Funciones exponenciales, logaritmicas y trigonometricas."""
import random
from core.formato import sup


BANCO_FACIL = [
    (f"2{sup('x')}", "exponencial"), (f"5{sup('x')}", "exponencial"),
    ("log(x)", "logaritmica"), ("ln(x)", "logaritmica"),
    ("sin(x)", "trigonometrica"), ("cos(x)", "trigonometrica"),
    (f"x{sup('2')}", "polinomica"), ("3x + 1", "lineal"),
]
BANCO_MEDIO = BANCO_FACIL + [
    (f"a{sup('x')} (a>0)", "exponencial"), ("log₂(x)", "logaritmica"),
    ("tan(x)", "trigonometrica"), ("1/x", "racional"),
]
BANCO_DIFICIL = BANCO_MEDIO + [
    (f"e{sup('x')}", "exponencial"), ("log₁₀(x)", "logaritmica"),
    ("sec(x)", "trigonometrica"), (f"x{sup('-2')}", "potencial"),
]

BANCOS = {"facil": BANCO_FACIL, "medio": BANCO_MEDIO, "dificil": BANCO_DIFICIL}




def generar(dificultad):
    from .mensajes import RECUERDAS_FUNCIONES
    banco = BANCOS[dificultad]
    tipo_pregunta = random.choice(["exponencial", "logaritmica", "trigonometrica"])
    correctas = [f for f, t in banco if t == tipo_pregunta]
    incorrectas = [f for f, t in banco if t != tipo_pregunta]

    correcta = random.choice(correctas)
    distractores = random.sample(incorrectas, 3)

    opciones = distractores + [correcta]
    random.shuffle(opciones)
    indice = opciones.index(correcta)

    enunciado = f"¿Cual de las siguientes es una funcion {tipo_pregunta}?"
    
    # Agregar el mensaje RECUERDA apropiado según el tipo de pregunta
    recuerda = RECUERDAS_FUNCIONES[tipo_pregunta]
    
    return {"enunciado": enunciado, "opciones": opciones, "indice_correcto": indice, "recuerda": recuerda}
