import numpy as np
import matplotlib.pyplot as plt

# messwerte: x-stellen und y-werte (b = rechte seite des gleichungssystems)
x_stellen = np.array([1, 5, 1, 2, 3, 4])
b = np.array([11, 4, 12, 11, 7, 6])   # rechte seite (nicht x!)

# A matrix korrekt aufbauen: nur x-stellen und 1er spalte (OHNE b als dritte spalte!)
A = np.array([
    [1, 1],
    [5, 1],
    [1, 1],
    [2, 1],
    [3, 1],
    [4, 1]
])

# lstsq korrekt aufrufen: A und b (nicht A und x!)
coeff, res, rank, s = np.linalg.lstsq(A, b, rcond=None)

# koeffizienten a1 und a0 extrahieren und ausgeben
a1 = coeff[0]
a0 = coeff[1]
print("a1:", a1)
print("a0:", a0)

# approximationsfehler pro messpunkt berechnen (nicht lstsq residuals verwenden!)
y_approx = a1 * x_stellen + a0          # geschätzte y-werte für jeden messpunkt
fehler = np.abs(y_approx - b)           # absoluter fehler pro messpunkt
print("Max abs Fehler:", np.max(fehler))

# plot: messpunkte als punkte + ausgleichspolynom im bereich [0, 6]
x_plot = np.arange(0, 6, 0.01)         # feines raster für smooth kurve
y_plot = a1 * x_plot + a0              # ausgleichspolynom

plt.plot(x_stellen, b, 'o', label='Messwerte')         # messwerte als punkte
plt.plot(x_plot, y_plot, label='Ausgleichspolynom')    # fitted polynomial
plt.grid(True)
plt.legend()
plt.show()