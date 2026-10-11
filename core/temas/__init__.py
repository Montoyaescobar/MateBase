"""
Modulo de generacion de ejercicios.
Reune los 5 generadores (uno por archivo/tema) y expone una sola
funcion generar_ejercicio() para que app.py no tenga que saber
cual archivo corresponde a cada tema.
"""
from . import mensajes
from . import exponentes
from . import radicales
from . import constantes
from . import derivadas
from . import funciones_especiales

GENERADORES = [
    exponentes.generar,
    radicales.generar,
    constantes.generar,
    derivadas.generar,
    funciones_especiales.generar,
]


def generar_ejercicio(tema_index, dificultad):
    return GENERADORES[tema_index](dificultad)
