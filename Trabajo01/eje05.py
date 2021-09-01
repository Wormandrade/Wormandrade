# Realiza un programa que reciba una cantidad de minutos y muestre por pantalla a cuantas horas y minutos corresponde
print("========================")
print("\tEJERCICIO 05")
print("========================")
print("Calculo de horas y minutos\n")
minutos = int(input("Ingrese la cantidad de minutos: "))
hora = minutos // 60
minu = minutos % 60
print(f"son {hora} horas y {minu} minutos")
