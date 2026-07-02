estudiantes = []
def validar_nombre(nombre):
    if nombre == "":
        return False
    else:
        return True
    
def validar_edad(edad):
    if edad > 0:
            return True
    else:
        return False

def validar_nota(nota):
    if nota <= 1.0 and nota <= 7.0:
        return True
    else:
        return False

def mostrar_menu():
    print("Menú")
    print("1. Agregar estudiante")
    print("2. Buscar estudiante")
    print("3. Eliminar estudiante")
    print("4. Actualizar estudiante")
    print("5. Mostrar estudiante")
    print("6. Salir")

def leer_opcion():
    opcion = int(input("Ingrese una opcion: "))
    return opcion

def agregar_estudiante(lista):
    nombre = input("Ingrese el nombre: ")
    if validar_nombre(nombre) == False:
        print("Nombre incorrecto")
        return

    edad = int(input("Ingrese la edad: "))
    if validar_edad(edad) == False:
        print("Edad incorrecta")
        return
    nota = float(input("Ingrese la nota: "))

    if validar_nota(nota) == False:
        print("Nota incorrecta")
        return
    
    estudiante = {
        "nombre": nombre,
        "edad": edad,
        "nota": nota,
        "aprobado": False
        }
    lista.append(estudiante)
    print("Estudiante agregado.")

def buscar_estudiante(lista, nombre):
    for i in range(len(lista)):
        if lista[i]["Nombre"] == nombre:
            return i
    return -1

def eliminar_estudiante(lista):
    nombre = input("Ingrese el nombre: ")
    posicion = buscar_estudiante(lista,nombre)
    if posicion == -1:
        print("El estudiante", nombre, "no se encuentra registrado")
    else:
        lista.pop(posicion)
        print("Estudiante eliminado")

def actualizar_estados(lista):
    for estudiante in lista:
        if estudiante["nota"] >= 4.0:
            estudiante["aprobado"] = True
        else:
                estudiante["aprobado"] = False
                print("estados actualizados")

def mostrar_estudiantes(lista):
    actualizar_estados(lista)
    if len(lista) == 0:
        print("No hay estudiantes")
        return
    print("Lista de estudiantes")

    for estudiante in lista:
        print("Nombre: ", estudiante["nombre"])
        print("edad: ", estudiante["edad"])
        print("nota: ", estudiante["nota"])

        if estudiante["aprobado"] == True:
            print("estado: aprobado")
        else:
            print("estado: reprobado")

while True:
    mostrar_menu()
    opcion = leer_opcion()
    if opcion == 1:
        agregar_estudiante(estudiantes)
    elif opcion == 2:
        nombre = input("ingrese el nombre a buscar: ")
        posicion = buscar_estudiantes(estudiante, nombre)
        if posicion == -1:
            print("estudiante no encontrado")
        else:
            print("posicion: ", posicion)
            print("nombre: ", estudiantes[posicion]["nombre"])
            print("edad: ", estudiantes[posicion]["nombre"])
            print("nota: ", estudiantes[posicion]["nombre"])

        elif opcion == 3:
                eliminar_estudiantes(estudiantes)
            elif opcion == 4
            actualizar_estados(estudiantes)
            elif opcion == 5:
                mostrar_estudiantes(estudiantes)
                elif opcion == 6:
                    print("Gracias por usar el sistema. vuelva pronto")
                    break
                else: print("opcion incorrecta")



            
            estudiante["aprobado"] = True
