# Escribir un programa que lea un año indicar si es bisiesto.
# Nota: un año es bisiesto si es un número divisible por 4, pero no si es divisible por 100, excepto que también sea divisible por 400.
print("========================")
print("\tEJERCICIO 11")
print("========================")
print("Año Bisisesto\n")
anio = int(input("Ingrese el año a validar: "))
if anio % 4 != 0:
	print(f"\t{anio} No es un año bisiesto")
elif anio % 4 == 0 and anio % 100 == 0 and anio % 400 != 0: 
	print(f"\t{anio} No es una año bisiesto")
elif anio % 4 == 0 and anio % 100 != 0: 
	print(f"\t{anio} Es un año bisiesto")
elif anio % 4 == 0 and anio % 100 == 0 and anio % 400 == 0: 
	print(f"\t{anio} Es un año bisiesto")
