import math

def funktion1(x, A, B):  # 2 parameter fkt
    ergebnis = A * math.sin(2 * math.pi * x) + B * math.cos(2 * math.pi * x)
    return ergebnis

# C ersetzt nur pi (nicht 2*pi!) -> standardwert für C ist also math.pi
def funktion2(x, A=20, B=17, C=math.pi):  # standardwerte direkt in der signatur
    ergebnis = A * math.sin(2 * C * x) + B * math.cos(2 * C * x)
    return ergebnis

A = 20
B = 17
C = 25

# fkt 1
print("Funktion 1 - Standardwerte:", funktion1(1, A, B))
print("Funktion 1 - ohne Standardwerte:", funktion1(2, 4, 3), "\n")

# fkt 2 - mit standardwerten (keine argumente für A, B, C nötig)
print("Funktion 2 - mit Standardwerten:", funktion2(7))
# fkt 2 - ohne standardwerte (eigene argumente übergeben)
print("Funktion 2 - ohne Standardwerte:", funktion2(11, 7, 6, 5))