"""
Formato de expresiones matematicas para la interfaz.
Convierte coeficientes y exponentes (enteros o fracciones) en texto
legible: 6x⁴, (3/2)x², -5/x³, 3/(2√x), etc.

Los polinomios se escriben siempre en forma canonica (terminos
semejantes reducidos y ordenados de mayor a menor exponente), asi dos
expresiones con el mismo valor producen exactamente el mismo texto.
Esto permite detectar distractores repetidos comparando cadenas.
"""
from fractions import Fraction

_SUPERINDICES = str.maketrans("0123456789-", "⁰¹²³⁴⁵⁶⁷⁸⁹⁻")


def superindice(n):
    return str(n).translate(_SUPERINDICES)


# ========== Funciones de formato lógico (mantener para compatibilidad interna) ==========

def numero(c):
    """3 -> '3', 3/2 -> '3/2', -1/4 -> '-1/4'."""
    c = Fraction(c)
    return str(c.numerator) if c.denominator == 1 else f"{c.numerator}/{c.denominator}"


def coeficiente(c):
    """Coeficiente delante de una variable: 1 -> '', -1 -> '-', 3/2 -> '(3/2)'."""
    c = Fraction(c)
    if c == 1:
        return ""
    if c == -1:
        return "-"
    if c.denominator == 1:
        return str(c.numerator)
    texto = f"({abs(c.numerator)}/{c.denominator})"
    return "-" + texto if c < 0 else texto


def potencia(n, var="x"):
    """x elevado a n: 0 -> '1', 1 -> 'x', 4 -> 'x⁴', -3 -> 'x⁻³', 1/2 -> '√x'."""
    n = Fraction(n)
    if n == 0:
        return "1"
    if n == 1:
        return var
    if n == Fraction(1, 2):
        return f"√{var}"
    if n == Fraction(3, 2):
        return f"{var}√{var}"
    if n.denominator == 1:
        return var + superindice(n.numerator)
    return f"{var}^({numero(n)})"


def monomio(c, n, fraccion=False):
    """
    c·xⁿ como texto. Con fraccion=True los exponentes negativos se
    escriben como division: 5x⁻³ -> '5/x³', (3/2)x^(-1/2) -> '3/(2√x)'.
    """
    c, n = Fraction(c), Fraction(n)
    if c == 0:
        return "0"
    if n == 0:
        return numero(c)
    if fraccion and n < 0:
        signo = "-" if c < 0 else ""
        p, q = abs(c).numerator, abs(c).denominator
        base = potencia(-n)
        denominador = base if q == 1 else f"({q}{base})"
        return f"{signo}{p}/{denominador}"
    return coeficiente(c) + potencia(n)


def polinomio(terminos, fraccion=False):
    """
    terminos: lista de (coeficiente, exponente).
    Reduce terminos semejantes y ordena de mayor a menor exponente.
    """
    acumulado = {}
    for c, n in terminos:
        n = Fraction(n)
        acumulado[n] = acumulado.get(n, 0) + Fraction(c)

    partes = []
    for n in sorted(acumulado, reverse=True):
        c = acumulado[n]
        if c == 0:
            continue
        texto = monomio(abs(c), n, fraccion)
        if not partes:
            partes.append(("-" if c < 0 else "") + texto)
        else:
            partes.append((" - " if c < 0 else " + ") + texto)
    return "".join(partes) or "0"


# ========== Funciones de formato HTML para display ==========

def numero_html(c):
    """Devuelve fracción en formato HTML vertical: 1/2 -> <span class="frac"><span class="num">1</span><span class="den">2</span></span>"""
    c = Fraction(c)
    if c.denominator == 1:
        return str(c.numerator)
    return f'<span class="frac"><span class="num">{c.numerator}</span><span class="den">{c.denominator}</span></span>'


def frac(num, den):
    """Genera HTML de fracción vertical: frac(1, 2) -> <span class="frac"><span class="num">1</span><span class="den">2</span></span>"""
    return f'<span class="frac"><span class="num">{num}</span><span class="den">{den}</span></span>'


def sup(exp):
    """Genera HTML de superíndice: sup('n') -> <sup>n</sup>"""
    return f'<sup>{exp}</sup>'


def sub(exp):
    """Genera HTML de subíndice: sub('a') -> <sub>a</sub>"""
    return f'<sub>{exp}</sub>'


def potencia_html(n, var="x"):
    """Versión HTML de potencia(): x elevado a n con <sup> tags."""
    n = Fraction(n)
    if n == 0:
        return "1"
    if n == 1:
        return var
    if n == Fraction(1, 2):
        return f"√{var}"
    if n == Fraction(3, 2):
        return f"{var}√{var}"
    if n.denominator == 1:
        return var + sup(str(n.numerator))
    return f"{var}{sup(f'({numero(n)})')}"


def coeficiente_html(c):
    """Versión HTML de coeficiente() para display."""
    c = Fraction(c)
    if c == 1:
        return ""
    if c == -1:
        return "-"
    if c.denominator == 1:
        return str(c.numerator)
    texto = f'<span class="frac"><span class="num">{abs(c.numerator)}</span><span class="den">{c.denominator}</span></span>'
    return "-" + texto if c < 0 else texto


def monomio_html(c, n, fraccion=False):
    """Versión HTML de monomio() para display."""
    c, n = Fraction(c), Fraction(n)
    if c == 0:
        return "0"
    if n == 0:
        return numero_html(c)
    if fraccion and n < 0:
        signo = "-" if c < 0 else ""
        p, q = abs(c).numerator, abs(c).denominator
        base = potencia_html(-n)
        denominador = base if q == 1 else f"({q}{base})"
        return f"{signo}{p}/{denominador}"
    return coeficiente_html(c) + potencia_html(n)


def polinomio_html(terminos, fraccion=False):
    """Versión HTML de polinomio() para display."""
    acumulado = {}
    for c, n in terminos:
        n = Fraction(n)
        acumulado[n] = acumulado.get(n, 0) + Fraction(c)

    partes = []
    for n in sorted(acumulado, reverse=True):
        c = acumulado[n]
        if c == 0:
            continue
        texto = monomio_html(abs(c), n, fraccion)
        if not partes:
            partes.append(("-" if c < 0 else "") + texto)
        else:
            partes.append((" - " if c < 0 else " + ") + texto)
    return "".join(partes) or "0"


def numero(c):
    """3 -> '3', 3/2 -> '3/2', -1/4 -> '-1/4'."""
    c = Fraction(c)
    return str(c.numerator) if c.denominator == 1 else f"{c.numerator}/{c.denominator}"


def coeficiente(c):
    """Coeficiente delante de una variable: 1 -> '', -1 -> '-', 3/2 -> '(3/2)'."""
    c = Fraction(c)
    if c == 1:
        return ""
    if c == -1:
        return "-"
    if c.denominator == 1:
        return str(c.numerator)
    texto = f"({abs(c.numerator)}/{c.denominator})"
    return "-" + texto if c < 0 else texto


def potencia(n, var="x"):
    """x elevado a n: 0 -> '1', 1 -> 'x', 4 -> 'x⁴', -3 -> 'x⁻³', 1/2 -> '√x'."""
    n = Fraction(n)
    if n == 0:
        return "1"
    if n == 1:
        return var
    if n == Fraction(1, 2):
        return f"√{var}"
    if n == Fraction(3, 2):
        return f"{var}√{var}"
    if n.denominator == 1:
        return var + superindice(n.numerator)
    return f"{var}^({numero(n)})"


def monomio(c, n, fraccion=False):
    """
    c·xⁿ como texto. Con fraccion=True los exponentes negativos se
    escriben como division: 5x⁻³ -> '5/x³', (3/2)x^(-1/2) -> '3/(2√x)'.
    """
    c, n = Fraction(c), Fraction(n)
    if c == 0:
        return "0"
    if n == 0:
        return numero(c)
    if fraccion and n < 0:
        signo = "-" if c < 0 else ""
        p, q = abs(c).numerator, abs(c).denominator
        base = potencia(-n)
        denominador = base if q == 1 else f"({q}{base})"
        return f"{signo}{p}/{denominador}"
    return coeficiente(c) + potencia(n)


def polinomio(terminos, fraccion=False):
    """
    terminos: lista de (coeficiente, exponente).
    Reduce terminos semejantes y ordena de mayor a menor exponente.
    """
    acumulado = {}
    for c, n in terminos:
        n = Fraction(n)
        acumulado[n] = acumulado.get(n, 0) + Fraction(c)

    partes = []
    for n in sorted(acumulado, reverse=True):
        c = acumulado[n]
        if c == 0:
            continue
        texto = monomio(abs(c), n, fraccion)
        if not partes:
            partes.append(("-" if c < 0 else "") + texto)
        else:
            partes.append((" - " if c < 0 else " + ") + texto)
    return "".join(partes) or "0"
