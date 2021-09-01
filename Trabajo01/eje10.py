#Escribe un programa que pida un nombre de usuario y una contraseña y si se ha introducido “pepe” y “passwd#” se indica “Has entrado al sistema”, sino se da un error.
print("========================")
print("\tEJERCICIO 10")
print("========================")
print("Credenciales\n")
usuario = "pepe"
passw = "passwd#"
nombre = ""
clave = ""
while (nombre != "pepe" and clave != "passwd#"):
    nombre = input("Ingrese el usuario: ")
    if nombre == usuario:
        print("\tusuario correcto")
        clave = input("Ingrese la clave: ")
        if clave == passw:
            print("\tCredenciales correctas, ingreso aceptado")
            break
        else:
            print("\tClave incorrecta, intente de nuevo por favor")
            nombre = ""
            #clave = ""
    else:
        print("\tUsuario incorrecto, intente de nuevo por favor")
print("Fin del proceso...")