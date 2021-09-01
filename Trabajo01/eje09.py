# Escribe un programa que pida un número entero entre uno y doce e imprima el número de días que tiene el mes correspondiente.
print("========================")
print("\tEJERCICIO 09")
print("========================")
print("Días de un mes seleccionado\n")
mes = int(input("Ingrese el el mes a validar los días: "))
if mes == 1 or mes==3 or mes==5 or mes==7 or mes==8 or mes==10 or mes==12:
    print(f"El {mes} mes posee 31 días")
elif mes == 4 or mes==6 or mes==9 or mes==11:
    print(f"El {mes} mes posee 30 días")
elif mes == 2:
    print(f"El {mes} mes posee 28 o 29 días")
else:
    print(f"El {mes} mes no existe")
    
