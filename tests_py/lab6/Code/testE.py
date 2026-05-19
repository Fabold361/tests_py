# keine externen bibliotheken erlaubt (kein numpy etc.)

def reverse(values):
    # prüfen ob liste gerade anzahl an elementen hat
    if len(values) % 2 != 0:
        raise ValueError("Error: List must have an even amount of numbers!")

    # inversionsalgorithmus: paarweises vertauschen von außen nach innen
    for i in range(len(values) // 2):   # nur bis zur mitte iterieren
        j = len(values) - 1 - i         # gegenüberliegender index

        # swap: erstes mit letztem, zweites mit vorletztem, ...
        temp = values[i]
        values[i] = values[j]
        values[j] = temp

    return values


# liste anlegen
insert = [10, 20, 30, 40, 50, 60]

print("Original:  ", insert)
result = reverse(insert)
print("Reversed:  ", result)