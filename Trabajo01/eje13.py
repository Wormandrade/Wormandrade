# Pedir un número por teclado y mostrar la tabla de multiplicar
print("========================")
print("\tEJERCICIO 13")
print("========================")
print("Tablas de multiplicar\n")
num = int(input("Digite el número de la tabla de multiplicar: "))
for factor in range(1, 16):
    print(f"{num} * {factor} = ", factor*num)
