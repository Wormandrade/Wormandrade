#Crea una aplicación que permita adivinar un número. 
# En primer lugar la aplicación solicita un número entero por teclado. 
# A continuación va pidiendo números y va respondiendo si el número a adivinar es mayor o menor que el introducido. 
# El programa termina cuando se acierta el número.
print("========================")
print("\tEJERCICIO 15")
print("========================")
print("Encontrar el número\n")
num_buscado = 77
aux_num = 0
while aux_num != num_buscado:
    aux_num = int(input("Ingrese el número a validar: "))
    if aux_num == num_buscado:
        print("Felicitaciones, el número ingresado es correcto..")
    else:
        print("\tIntente de nuevo, por favor..")
else:
    print("----Final del juego---")
        
