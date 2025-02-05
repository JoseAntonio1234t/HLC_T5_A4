def potencia_recursiva(base, exponente):
    if exponente == 0 or exponente == 1:
         return 1
    return base * potencia_recursiva(base, exponente - 1)
base = int(input("Introduce la base "))
exponente = int(input("Introduce el exponente "))
     
 
print(potencia_recursiva(base, exponente))