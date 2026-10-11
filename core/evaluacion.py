"""
Modulo de evaluacion y verificacion.
Compara la opcion elegida por el estudiante contra la respuesta
correcta registrada, sin importar en que letra haya quedado.
"""


def verificar_respuesta(indice_seleccionado, indice_correcto):
    """Devuelve True si el estudiante acerto, False si no."""
    return indice_seleccionado == indice_correcto
