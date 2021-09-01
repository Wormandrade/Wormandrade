#Programa que lea un carácter por teclado y compruebe si es una letra mayúscula
print("========================")
print("\tEJERCICIO 12")
print("========================")
print("Validación de Letras Mayúsculas\n")
letras = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "Ñ", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
aux = 0
valida = False
while aux != 1:
    letra = input("Ingrese la letra a validar: ")
    aux = len(letra)
    if aux >= 2:
        print("\tDigitar solo una letra")
    elif aux == 1:
        for dato in letras:
            if dato == letra:
                valida = True
        if valida:
            print(f"\t{letra} Es una letra en mayúscula")
        else:
            print(f"\t{letra} No es una letra en mayúscula")
else:
    print("Fin del Proceso..")