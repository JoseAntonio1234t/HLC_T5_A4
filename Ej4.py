def suma_numeros(n):
    suma = 0
    for i in range(1, n + 1):
        suma += i
    return suma
print(suma_numeros(5))