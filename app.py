"""
Modulo principal (seccion 10.1 de la propuesta).
Controla el flujo general: recibe las peticiones del navegador (rutas),
coordina los modulos de configuracion, generacion, evaluacion y sesion,
y le entrega las paginas HTML al estudiante.

Flujo de un ejercicio (patron POST -> redirect -> GET, para que recargar
la pagina nunca registre una respuesta dos veces):
    GET  /practica   muestra la pregunta (o la retroalimentacion si ya se respondio)
    POST /practica   registra la respuesta y redirige a GET /practica
    POST /siguiente  pasa al siguiente ejercicio y redirige a GET /practica
"""
import os
import secrets

from flask import Flask, render_template, request, redirect, url_for, session

from core import configuracion, sesion, evaluacion
from core.temas import generar_ejercicio

app = Flask(__name__)
# La clave se toma de una variable de entorno. Si no existe, se genera una
# aleatoria en cada arranque (las sesiones abiertas se pierden al reiniciar).
app.secret_key = os.environ.get("MATEBASE_SECRET_KEY") or secrets.token_hex(32)


def _a_entero(valor):
    """Convierte un dato del formulario a entero; devuelve None si no se puede."""
    try:
        return int(valor)
    except (TypeError, ValueError):
        return None


def _pagina_inicio(error=None):
    return render_template(
        "index.html",
        temas=configuracion.TEMAS,
        iconos=configuracion.ICONOS,
        cantidad_min=configuracion.CANTIDAD_MINIMA,
        cantidad_max=configuracion.CANTIDAD_MAXIMA,
        error=error,
    )


@app.route("/")
def index():
    return _pagina_inicio()


@app.route("/configurar", methods=["POST"])
def configurar():
    tema_index = _a_entero(request.form.get("tema"))
    cantidad = _a_entero(request.form.get("cantidad"))
    dificultad = request.form.get("dificultad", "")

    if tema_index is None:
        return _pagina_inicio("Selecciona un tema valido.")
    if cantidad is None:
        return _pagina_inicio("La cantidad de ejercicios debe ser un numero entero.")

    es_valido, mensaje = configuracion.validar_configuracion(tema_index, cantidad, dificultad)
    if not es_valido:
        return _pagina_inicio(mensaje)

    sesion.iniciar(session, tema_index, cantidad, dificultad)
    return redirect(url_for("practica"))


@app.route("/practica", methods=["GET", "POST"])
def practica():
    if not sesion.en_curso(session):
        return redirect(url_for("index"))
    if sesion.sesion_terminada(session):
        return redirect(url_for("resultados"))

    if request.method == "POST":
        return _registrar_respuesta()

    ejercicio = sesion.ejercicio_actual(session)

    if sesion.esperando_siguiente(session):
        # Ya se respondio: se vuelve a mostrar la retroalimentacion (recargar es seguro)
        if ejercicio is None:
            # El servidor se reinicio y se perdio el ejercicio: pasar al siguiente
            sesion.avanzar_si_corresponde(session)
            return redirect(url_for("practica"))
        resultado = session["ultimo_resultado"]
    else:
        if ejercicio is None:
            ejercicio = generar_ejercicio(session["tema_index"], session["dificultad"])
            sesion.asignar_ejercicio(session, ejercicio)
        resultado = None

    return render_template(
        "practica.html",
        ejercicio=ejercicio,
        ejercicio_id=session["ejercicio_id"],
        resultado=resultado,
        actual=session["actual"],
        cantidad=session["cantidad"],
        tema=configuracion.TEMAS[session["tema_index"]],
        dificultad=session["dificultad"],
    )

#! Esta función se ejecuta cuando el usuario envía su respuesta a un ejercicio de opción múltiple. 
#! Revisa que todo sea válido, califica la respuesta, guarda el resultado y vuelve a mostrar la página de práctica.
def _registrar_respuesta():
    ejercicio = sesion.ejercicio_actual(session)

    # Respuesta repetida (recarga, doble clic, boton "atras"), o el ejercicio
    # ya no existe: no se registra nada, solo se vuelve a la pagina actual.
    if (
        ejercicio is None
        or sesion.esperando_siguiente(session)
        or request.form.get("ejercicio_id") != session.get("ejercicio_id")
    ):
        return redirect(url_for("practica"))

    seleccion = _a_entero(request.form.get("opcion"))
    if seleccion is None or not 0 <= seleccion < len(ejercicio["opciones"]):
        return redirect(url_for("practica"))

    acerto = evaluacion.verificar_respuesta(seleccion, ejercicio["indice_correcto"])
    respuesta_correcta = ejercicio["opciones"][ejercicio["indice_correcto"]]
    sesion.registrar_resultado(session, acerto, respuesta_correcta)
    return redirect(url_for("practica"))


@app.route("/siguiente", methods=["POST"])
def siguiente():
    if not sesion.en_curso(session):
        return redirect(url_for("index"))
    sesion.avanzar_si_corresponde(session)
    return redirect(url_for("practica"))


@app.route("/resultados")
def resultados():
    if not sesion.en_curso(session) or not sesion.hay_respuestas(session):
        return redirect(url_for("index"))
    resumen = sesion.calcular_resumen(session)
    return render_template("resultados.html", **resumen)


if __name__ == "__main__":
    app.run(debug=True)
