"""
Modulo de gestion de sesion y resultados.
Administra el progreso del estudiante: tema, dificultad, cantidad,
ejercicio actual, aciertos y errores; y calcula el resumen final.

El ejercicio en si (con la respuesta correcta) NO se guarda en la
sesion del navegador, sino en core/almacen.py. Aqui solo se guarda
su identificador ("ejercicio_id").
"""
from core import almacen


def iniciar(session, tema_index, cantidad, dificultad):
    almacen.eliminar(session.get("ejercicio_id"))
    session["tema_index"] = tema_index
    session["cantidad"] = cantidad
    session["dificultad"] = dificultad
    session["actual"] = 1
    session["aciertos"] = 0
    session["errores"] = 0
    session.pop("ejercicio_id", None)
    session.pop("esperando_siguiente", None)
    session.pop("ultimo_resultado", None)


def en_curso(session):
    return "tema_index" in session


def ejercicio_actual(session):
    """Devuelve el ejercicio actual desde el servidor, o None."""
    return almacen.obtener(session.get("ejercicio_id"))


def asignar_ejercicio(session, ejercicio):
    almacen.eliminar(session.get("ejercicio_id"))
    session["ejercicio_id"] = almacen.guardar(ejercicio)


def esperando_siguiente(session):
    return bool(session.get("esperando_siguiente"))


def registrar_resultado(session, acerto, respuesta_correcta):
    if acerto:
        session["aciertos"] += 1
    else:
        session["errores"] += 1
    session["esperando_siguiente"] = True
    # Ya respondida, mostrar la respuesta correcta no es un problema
    session["ultimo_resultado"] = {"correcto": acerto, "respuesta_correcta": respuesta_correcta}


def avanzar_si_corresponde(session):
    if session.get("esperando_siguiente"):
        session["actual"] += 1
        session["esperando_siguiente"] = False
        session.pop("ultimo_resultado", None)
        almacen.eliminar(session.pop("ejercicio_id", None))


def sesion_terminada(session):
    return session["actual"] > session["cantidad"]


def hay_respuestas(session):
    return session.get("aciertos", 0) + session.get("errores", 0) > 0


def calcular_resumen(session):
    aciertos = session.get("aciertos", 0)
    errores = session.get("errores", 0)
    total = aciertos + errores
    porcentaje = round((aciertos / total) * 100, 1) if total > 0 else 0
    return {"aciertos": aciertos, "errores": errores, "total": total, "porcentaje": porcentaje}
