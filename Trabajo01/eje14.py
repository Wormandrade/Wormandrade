# Crea una aplicación que pida un número y calcule su factorial 
# (El factorial de un número es el producto de todos los enteros entre 1 y el propio número y se representa por el número seguido de un signo de exclamación. 
# Por ejemplo 5! = 1x2x3x4x5=120
print("========================")
print("\tEJERCICIO 14")
print("========================")
print("Calcular Factorial de un número\n")
num = int(input("Digite el número a calcular: "))
aux = 1
for factor in range(1, num+1):
    aux = factor * aux
print(f"El factorial de {num} es:", aux)