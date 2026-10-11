"""
Mensajes de ayuda RECUERDA para cada tipo de ejercicio.
Cada mensaje sigue el formato: "RECUERDA: [fórmula]. [explicación breve]."
"""

# Mensajes para Exponentes
RECUERDAS_EXPONENTES = {
    "producto": "RECUERDA: a^m · a^n = a^(m+n). Al multiplicar potencias de la misma base, se suman los exponentes.",
    "cociente": "RECUERDA: a^m / a^n = a^(m-n). Al dividir potencias de la misma base, se restan los exponentes.",
    "potencia_de_potencia": "RECUERDA: (a^m)^n = a^(m·n). Al elevar una potencia a otra potencia, se multiplican los exponentes.",
    "potencia_por_producto": "RECUERDA: (a^m)^n · a^p = a^(m·n+p). Primero resuelva la potencia de potencia, luego multiplique sumando exponentes.",
    "coeficiente_elevado": "RECUERDA: (k·a^m)^n = k^n · a^(m·n). El coeficiente se eleva a la potencia y los exponentes se multiplican.",
    "cociente_negativo": "RECUERDA: a^m / a^n = a^(m-n). Si m < n, el resultado será un exponente negativo.",
    "potencia_negativa": "RECUERDA: (-a)^m = (-1)^m · a^m. Un número negativo elevado a potencia par da positivo, a impar da negativo.",
    "producto_negativo": "RECUERDA: (-a)^m · b^n = (-1)^m · a^m · b^n. El signo depende si el exponente de la base negativa es par o impar.",
    "combinado": "RECUERDA: (a^m)^n / a^p = a^(m·n-p). Combine las reglas: potencia de puissance puis cociente.",
    "sin_negativos": "RECUERDA: a^(-n) = 1/(a^n). Un exponente negativo se convierte en positivo al pasar al denominador."
}

# Mensajes para Radicales
RECUERDAS_RADICALES = {
    "facil": "RECUERDA: √(a²) = a (si a ≥ 0). La raíz cuadrada de un número perfecto es su raíz.",
    "medio": "RECUERDA: ³√(a³) = a. La raíz cúbica de un número perfecto es su raíz.",
    "dificil": "RECUERDA: √(a² · b²) = √a² · √b² = a · b. La raíz de un producto es el producto de las raíces."
}

# Mensajes para Constantes
RECUERDAS_CONSTANTES = {
    "sacar_constante": "RECUERDA: k · ∫ f(x) dx = ∫ k·f(x) dx. Una constante multiplicadora se puede sacar fuera de la integral.",
    "producto_fracciones": "RECUERDA: (a/b) · (c/d) = (a·c)/(b·d). Para multiplicar fracciones, multiplique numeradores entre sí y denominadores entre sí.",
    "distribuir": "RECUERDA: k · (x^n + b) = k·x^n + k·b. La distributividad: multiplicar el término fuera del paréntesis por cada término dentro.",
    "reescribir_potencia": "RECUERDA: 1/(x^n) = x^(-n). Un término en el denominador con exponente positivo se vuelve negativo al pasar al numerador.",
    "cociente_monomios": "RECUERDA: (x^m)/(x^n) = x^(m-n). Al dividir potencias de la misma base, se restan los exponentes.",
    "factor_comun": "RECUERDA: g·(a+b+c) = g·a + g·b + g·c. El factor común se distribuye a cada término dentro del paréntesis.",
    "coeficiente_integral": "RECUERDA: ∫ x^n dx = (1/(n+1))·x^(n+1) + C. Para integrar x^n, sumar 1 al exponente y dividir por el nuevo exponente.",
    "hallar_k": "RECUERDA: d/dx [k·x^n] = k·n·x^(n-1). La derivada de k·x^n es k·n·x^(n-1). Iguale esto al resultado dado y despeje k.",
    "ajuste_sustitucion": "RECUERDA: Si u = bx + c, entonces du = b·dx, por lo tanto dx = du/b. Derive u respecto a x y despeje dx."
}

# Mensajes para Derivadas
RECUERDAS_DERIVADAS = {
    "facil": "RECUERDA: d/dx [x^n] = n·x^(n-1). La regla de la potencia: bajar el exponente como coeficiente y reducir el exponente en 1.",
    "medio": "RECUERDA: d/dx [f(x)+g(x)] = f'(x)+g'(x). La derivada de una suma es la suma de las derivadas (linealidad).",
    "dificil_negativo": "RECUERDA: d/dx [x^(-n)] = -n·x^(-n-1). Aplique la regla de la potencia: el exponente negativo se resta 1 y mantiene su signo.",
    "dificil_raiz": "RECUERDA: d/dx [x^(1/2)] = (1/2)·x^(-1/2) = 1/(2√x). La raíz cuadrada es x^(1/2), aplique la regla de la potencia."
}

# Mensajes para Funciones Especiales
RECUERDAS_FUNCIONES = {
    "exponencial": "RECUERDA: d/dx [a^x] = a^x · ln(a). La derivada de a^x es proporcional a sí misma, con factor ln(a).",
    "logaritmica": "RECUERDA: d/dx [log_a(x)] = 1/(x·ln(a)). La derivada del logaritmo es 1 dividido por x veces el logaritmo de la base.",
    "trigonometrica": "RECUERDA: d/dx [sin(x)] = cos(x) y d/dx [cos(x)] = -sin(x). Estas son las derivadas básicas que debe memorizar.",
    "polinomica": "RECUERDA: d/dx [x^n] = n·x^(n-1). Igual que la regla de la potencia vista en derivadas básicas.",
    "lineal": "RECUERDA: d/dx [ax+b] = a. La derivada de una función lineal es su pendiente (coeficiente de x).",
    "racional": "RECUERDA: d/dx [x^n] = n·x^(n-1) para cualquier n real, incluidos negativos y fraccionarios."
}