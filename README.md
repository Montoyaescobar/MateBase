# MateBase

Aplicacion educativa en Python (Flask) para el fortalecimiento de
conocimientos previos al calculo integral. Universidad Autonoma del
Cauca - Calculo II.

## Como correrla

```
pip install -r requirements.txt
python app.py
```

Abrir en el navegador: http://127.0.0.1:5000

Opcional: definir la variable de entorno `MATEBASE_SECRET_KEY` con una
clave secreta propia. Si no se define, se genera una aleatoria en cada
arranque (las sesiones abiertas se pierden al reiniciar el servidor).

## Seguridad de las respuestas

El ejercicio actual (con su respuesta correcta) se guarda en la memoria
del servidor (`core/almacen.py`). En la cookie del navegador solo queda
un identificador aleatorio, asi que el estudiante no puede ver la
respuesta. Las respuestas siguen el patron POST -> redirect -> GET, por lo
que recargar la pagina nunca registra una respuesta dos veces.

## Estructura del proyecto

El codigo esta organizado siguiendo los 7 modulos descritos en la
propuesta de software (seccion 10):

| Carpeta / archivo              | Modulo de la propuesta                  |
|---------------------------------|------------------------------------------|
| `app.py`                        | 10.1 Modulo principal                    |
| `core/configuracion.py`         | 10.2 Seleccion y configuracion           |
| `core/temas/*.py`               | 10.3 Generacion de ejercicios            |
| `core/opciones.py`              | 10.4 Generacion de opciones de respuesta |
| `core/evaluacion.py`            | 10.5 Evaluacion y verificacion           |
| `core/sesion.py`                | 10.6 Gestion de sesion y resultados      |
| `core/almacen.py`               | 10.6 Ejercicios guardados en el servidor |
| `templates/`, `static/`         | 10.7 Interfaz de usuario                 |

Cada tema matematico (exponentes, radicales, constantes, derivadas,
funciones especiales) vive en su propio archivo dentro de
`core/temas/`, para poder agregar temas nuevos sin tocar el resto
del sistema (RNF-06, escalabilidad).
