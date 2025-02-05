def factorial_iterativo(n):
     resultado = 1
     for i in range(2, n + 1):
         resultado *= i
     return resultado
 
def factorial_recursivo(n):
     if n == 0 or n == 1:
         return 1
     else:
         return n * factorial_recursivo(n - 1)
     

print(factorial_iterativo(5)),print((factorial_recursivo(6)))