import math

def pole_trojkata(a, b, c):
    """Funkcja oblicza pole trójkąta o bokach a, b i c."""
    if a <= 0 or b <= 0 or c <= 0:
        raise ValueError("Boki trójkąta muszą być dodatnie.")
    if a + b <= c or a + c <= b or b + c <= a:
        raise ValueError("Podane długości nie tworzą trójkąta.")
    s = (a + b + c) / 2
    return math.sqrt(s * (s - a) * (s - b) * (s - c))