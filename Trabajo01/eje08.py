#Escribe un programa que lea un número e indique si es par o impar.
print("========================")
print("\tEJERCICIO 08")
print("========================")
print("Validacion de número par o impar\n")
num = int(input("Ingrese el valor a comparar: "))
if num % 2 == 0:
    print(f"El número {num} es par")
else:
    print(f"El número {num} es impar")