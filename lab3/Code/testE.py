import math

# tk1
def func(x):
    if x < -0.5:
        f = 2 * x**2 + x
        f_prime = 4 * x + 1
    else:
        f = math.exp(x)
        f_prime = math.exp(x)
    return (f, f_prime)

# tk2 - seq ist eine liste von x-werten (nicht eine zahl!)
def func_vec(seq):
    results = []
    for x in seq:           # direkt über die elemente der liste iterieren
        values = func(x)    # func für jeden x-wert aus der liste aufrufen
        results.append(values)
    print("Output func_vec:\n", "Length of seq:", len(seq))
    return results

# Output func
print("Output of func:")
print(func(-2))         # x < -0.5
print(func(2), "\n")    # x >= -0.5

# Output func_vec - sequenzen verschiedener länge als listen übergeben
print(func_vec([-5, -4, -3, -2, -1, 0, 1, 2, 3, 4]))   # 10 elemente
print(func_vec([-5, -4, -3, -2, -1]))                   # 5 elemente