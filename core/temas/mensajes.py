"""
Mensajes de ayuda RECUERDA para cada tipo de ejercicio.
Cada mensaje sigue el formato: "RECUERDA: [fórmula]. [explicación breve]."
"""
from core.formato import frac, sup, sub


# Mensajes para Exponentes
RECUERDAS_EXPONENTES = {
    "producto": f"RECUERDA: a{sup('m')} · a{sup('n')} = a{sup('m+n')}. Al multiplicar potencias de la misma base, se suman los exponentes.",
    "cociente": f"RECUERDA: a{sup('m')} / a{sup('n')} = a{sup('m-n')}. Al dividir potencias de la misma base, se restan los exponentes.",
    "potencia_de_potencia": f"RECUERDA: (a{sup('m')}){sup('n')} = a{sup('m·n')}. Al elevar una potencia a otra potencia, se multiplican los exponentes.",
    "potencia_por_producto": f"RECUERDA: (a{sup('m')}){sup('n')} · a{sup('p')} = a{sup('m·n+p')}. Primero resuelve la potencia de potencia, luego multiplica sumando exponentes.",
    "coeficiente_elevado": f"RECUERDA: (k·a{sup('m')}){sup('n')} = k{sup('n')} · a{sup('m·n')}. El coeficiente se eleva a la potencia y los exponentes se multiplican.",
    "cociente_negativo": f"RECUERDA: a{sup('m')} / a{sup('n')} = a{sup('m-n')}. Si m < n, el resultado será un exponente negativo.",
    "potencia_negativa": f"RECUERDA: (-a){sup('m')} = (-1){sup('m')} · a{sup('m')}. Un número negativo elevado a potencia par da positivo, a impar da negativo.",
    "producto_negativo": f"RECUERDA: (-a){sup('m')} · b{sup('n')} = (-1){sup('m')} · a{sup('m')} · b{sup('n')}. El signo depende si el exponente de la base negativa es par o impar.",
    "combinado": f"RECUERDA: (a{sup('m')}){sup('n')} / a{sup('p')} = a{sup('m·n-p')}. Combina las reglas: potencia de potencia y luego cociente.",
    "sin_negativos": f"RECUERDA: a{sup('-n')} = {frac('1', 'a' + sup('n'))}. Un exponente negativo se convierte en positivo al pasar al denominador."
}

# Mensajes para Radicales
RECUERDAS_RADICALES = {
    "facil": f"RECUERDA: √(a{sup('2')}) = a (si a ≥ 0). La raíz cuadrada de un número perfecto es su raíz.",
    "medio": f"RECUERDA: ³√(a{sup('3')}) = a. La raíz cúbica de un número perfecto es su raíz.",
    "dificil": f"RECUERDA: √(a{sup('2')} · b{sup('2')}) = √a{sup('2')} · √b{sup('2')} = a · b. La raíz de un producto es el producto de las raíces."
}

# Mensajes para Constantes
RECUERDAS_CONSTANTES = {
    "sacar_constante": "RECUERDA: k · ∫ f(x) dx = ∫ k·f(x) dx. Una constante multiplicadora se puede sacar fuera de la integral.",
    "producto_fracciones": f"RECUERDA: {frac('a', 'b')} · {frac('c', 'd')} = {frac('a·c', 'b·d')}. Para multiplicar fracciones, multiplica numeradores entre sí y denominadores entre sí.",
    "distribuir": f"RECUERDA: k · (x{sup('n')} + b) = k·x{sup('n')} + k·b. La distributividad: multiplica el término fuera del paréntesis por cada término dentro.",
    "reescribir_potencia": f"RECUERDA: {frac('1', 'x' + sup('n'))} = x{sup('-n')}. Un término en el denominador con exponente positivo se vuelve negativo al pasar al numerador.",
    "cociente_monomios": f"RECUERDA: (x{sup('m')})/(x{sup('n')}) = x{sup('m-n')}. Al dividir potencias de la misma base, se restan los exponentes.",
    "factor_comun": "RECUERDA: g·(a+b+c) = g·a + g·b + g·c. El factor común se distribuye a cada término dentro del paréntesis.",
    "coeficiente_integral": f"RECUERDA: ∫ x{sup('n')} dx = {frac('1', 'n+1')}·x{sup('n+1')} + C. Para integrar x{sup('n')}, suma 1 al exponente y divide por el nuevo exponente.",
    "hallar_k": f"RECUERDA: d/dx [k·x{sup('n')}] = k·n·x{sup('n-1')}. La derivada de k·x{sup('n')} es k·n·x{sup('n-1')}. Iguala esto al resultado dado y despeja k.",
    "ajuste_sustitucion": f"RECUERDA: Si u = bx + c, entonces du = b·dx, por lo tanto dx = {frac('du', 'b')}. Deriva u respecto a x y despeja dx."
}

# Mensajes para Derivadas
RECUERDAS_DERIVADAS = {
    "facil": f"RECUERDA: d/dx [x{sup('n')}] = n·x{sup('n-1')}. La regla de la potencia: baja el exponente como coeficiente y reduce el exponente en 1.",
    "medio": "RECUERDA: d/dx [f(x)+g(x)] = f'(x)+g'(x). La derivada de una suma es la suma de las derivadas (linealidad).",
    "dificil_negativo": f"RECUERDA: d/dx [x{sup('-n')}] = -n·x{sup('-n-1')}. Aplica la regla de la potencia: el exponente negativo se resta 1 y mantiene su signo.",
    "dificil_raiz": f"RECUERDA: d/dx [x{sup('1/2')}] = {frac('1', '2')}·x{sup('-1/2')} = {frac('1', '2√x')}. La raíz cuadrada es x{sup('1/2')}, aplica la regla de la potencia."
}

# Mensajes para Funciones Especiales
RECUERDAS_FUNCIONES = {
    "exponencial": f"RECUERDA: d/dx [a{sup('x')}] = a{sup('x')} · ln(a). La derivada de a{sup('x')} es proporcional a sí misma, con factor ln(a).",
    "logaritmica": f"RECUERDA: d/dx [log{sub('a')}(x)] = {frac('1', 'x·ln(a)')}. La derivada del logaritmo es 1 dividido por x veces el logaritmo de la base.",
    "trigonometrica": "RECUERDA: d/dx [sin(x)] = cos(x) y d/dx [cos(x)] = -sin(x). Estas son las derivadas básicas que debes memorizar.",
    "polinomica": f"RECUERDA: d/dx [x{sup('n')}] = n·x{sup('n-1')}. Igual que la regla de la potencia vista en derivadas básicas.",
    "lineal": "RECUERDA: d/dx [ax+b] = a. La derivada de una función lineal es su pendiente (coeficiente de x).",
    "racional": f"RECUERDA: d/dx [x{sup('n')}] = n·x{sup('n-1')} para cualquier n real, incluidos negativos y fraccionarios."
}