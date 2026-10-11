"""
Modulo de seleccion y configuracion
Guarda la lista de temas disponibles y valida los parametros
que elige el estudiante: tema, cantidad y dificultad.
"""

TEMAS = [
    "Leyes de los exponentes y potencias",
    "Raices cuadradas y radicales",
    "Manejo de constantes y coeficientes",
    "Derivadas basicas",
    "Funciones exponenciales, logaritmicas y trigonometricas",
]

# Un simbolo representativo por tema, solo para la interfaz
ICONOS = ["xⁿ", "√x", "3x²", "dx", "ƒ(x)"]

DIFICULTADES = ["facil", "medio", "dificil"]

CANTIDAD_MINIMA = 10
CANTIDAD_MAXIMA = 30


def tema_valido(indice):
    return 0 <= indice < len(TEMAS) #!AQUI SELECCIONAMOS LOS TEMAS GRACIAS A ESTA FUNCION.


def cantidad_valida(cantidad):
    return CANTIDAD_MINIMA <= cantidad <= CANTIDAD_MAXIMA #!LA CONFIGURACION DE LA CANTIDAD DE EJERCICIOS


def dificultad_valida(dificultad):
    return dificultad in DIFICULTADES


def validar_configuracion(tema_index, cantidad, dificultad):
    """
    Revisa que los tres parametros sean validos.
    Devuelve (True, None) si todo esta bien, o (False, "mensaje") si no.
    """
    if not tema_valido(tema_index):
        return False, "El tema seleccionado no existe."
    if not cantidad_valida(cantidad):
        return False, f"La cantidad debe estar entre {CANTIDAD_MINIMA} y {CANTIDAD_MAXIMA}."
    if not dificultad_valida(dificultad):
        return False, "La dificultad debe ser facil, medio o dificil."
    return True, None
