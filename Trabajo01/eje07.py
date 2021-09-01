# Realiza un programa que pida dos números ‘a’ y ‘b’ e indique si su suma es positiva, negativa o cero.
print("========================")
print("\tEJERCICIO 07")
print("========================")
print("Validacion de Suma de 2 números\n")
num_a = float(input("Ingrese el número a: "))
num_b = float(input("Ingrese el número a: "))
suma = num_a + num_b
if suma < 0:
    print(f"La suma de los 2 número es negativa: {suma}")
elif suma == 0:
    print(f"La suma de los 2 número es: 0")
else:
    print(f"La suma de los 2 número es positiva: {suma}")