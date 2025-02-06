def suma_numeros(n):
    if n == 0:
        return 0
    return n%10 + suma_numeros(int(n/10))
print(suma_numeros(1234))