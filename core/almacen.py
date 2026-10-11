"""
Almacen de ejercicios en el servidor.
El ejercicio actual (con su respuesta correcta) se guarda aqui, en la
memoria del servidor. En la cookie del navegador solo queda un
identificador aleatorio, asi el estudiante no puede ver la respuesta.

Nota: al ser memoria del proceso, los ejercicios se pierden si se
reinicia el servidor (la app simplemente genera uno nuevo).
"""
import threading
import time
import uuid

# Ejercicios abandonados se borran despues de este tiempo (segundos)
TIEMPO_EXPIRACION = 2 * 60 * 60

_ejercicios = {}
_candado = threading.Lock() #!PREPARAMOS un almacén de ejercicios en memoria y un candado para protegerlo.


def _limpiar_expirados(ahora):
    vencidos = [k for k, (_, t) in _ejercicios.items() if ahora - t > TIEMPO_EXPIRACION]
    for k in vencidos:   #!“recorre cada ejercicio, con su clave k y su hora t, y guarda la clave si ya pasaron más de 2 horas desde que se creó”
        del _ejercicios[k] #!ESTA FUNCION FUNCIONA COMO UN RECOLECTOR DE BASURA PARA LIMPIAR EJERCICIOS QUE SE QUEDAN PENDIENTES


def guardar(ejercicio):
    """Guarda el ejercicio y devuelve su identificador."""
    ahora = time.time()
    ejercicio_id = uuid.uuid4().hex
    with _candado:
        _limpiar_expirados(ahora)
        _ejercicios[ejercicio_id] = (ejercicio, ahora)
    return ejercicio_id


def obtener(ejercicio_id):
    """Devuelve el ejercicio o None si no existe (o ya expiro)."""
    if not ejercicio_id:
        return None
    with _candado:
        dato = _ejercicios.get(ejercicio_id)
    return dato[0] if dato else None


def eliminar(ejercicio_id):
    if not ejercicio_id:
        return
    with _candado:
        _ejercicios.pop(ejercicio_id, None)
