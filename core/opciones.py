"""
Modulo de generacion de opciones de respuesta (seccion 10.4 de la propuesta).
Recibe la respuesta correcta y los distractores, y devuelve las 4
opciones ya mezcladas junto con el indice de la correcta.

Hay dos formas:
- armar_opciones(): para respuestas numericas simples (radicales).
- armar_opciones_texto(): para respuestas que son expresiones completas.
  Recibe distractores "pensados" (errores tipicos del estudiante) y una
  funcion de respaldo que genera variaciones si no alcanzan.
"""
import random

MAX_INTENTOS = 40


def armar_opciones(correcta, generador_distractor):
    """
    correcta: el valor numerico correcto.
    generador_distractor: una funcion que, cada vez que se llama,
        devuelve un posible distractor (puede repetir o ser invalido,
        aqui se filtra).
    """
    distractores = set()
    intentos = 0
    while len(distractores) < 3 and intentos < MAX_INTENTOS:
        d = generador_distractor()
        if d != correcta and d not in distractores and d >= 0:
            distractores.add(d)
        intentos += 1

    # Estrategia alternativa si no se lograron 3 distractores validos
    extra = 1
    while len(distractores) < 3:
        candidato = correcta + extra + 1
        if candidato != correcta and candidato not in distractores:
            distractores.add(candidato)
        extra += 1

    opciones = list(distractores) + [correcta]
    random.shuffle(opciones)
    indice_correcto = opciones.index(correcta)
    return opciones, indice_correcto


def armar_opciones_texto(correcta, candidatos, respaldo):
    """
    correcta: texto de la respuesta correcta.
    candidatos: lista de distractores basados en errores tipicos
        (pueden venir repetidos o iguales a la correcta; se filtran).
    respaldo: funcion sin argumentos que devuelve un distractor
        aleatorio; se usa solo si los candidatos no alcanzan.
    """
    disponibles = [c for c in dict.fromkeys(candidatos) if c != correcta]
    random.shuffle(disponibles)
    distractores = disponibles[:3]

    intentos = 0
    while len(distractores) < 3 and intentos < MAX_INTENTOS:
        d = respaldo()
        if d != correcta and d not in distractores:
            distractores.append(d)
        intentos += 1
    if len(distractores) < 3:
        raise RuntimeError(f"No se pudieron generar distractores para {correcta!r}")

    opciones = distractores + [correcta]
    random.shuffle(opciones)
    return opciones, opciones.index(correcta)
