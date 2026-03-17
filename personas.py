personas = []

def ingresar_persona():
    print("\n--- INGRESO DE PERSONA ---")
    nombre = input("Nombre: ")
    edad = int(input("Edad: "))
    nota = float(input("Nota: "))

    personas.append([nombre, edad, nota])
    print("✓ Persona agregada correctamente\n")



def mostrar_lista_original():
    if not personas:
        print("no hay personas en la lista")
        return
    print("listado original")
    print(f"{'nombre':<20} {'edad':<10} {'nota':<10}")
    print("-" * 50)
    for persona in personas:
        print(f"{persona[0]:<20}\t\t{persona[1]:<10}\t\t{persona[2]:<10}")
    print()

def mostrar_lista_ordenada():
    if not personas:
        print("no hay personas en la lista")
        return
    print("\n--- LISTADO ORDENADO POR NOTA (MAYOR A MENOR) ---")
    print(f"{'nombre':<20} {'edad':<10} {'nota':<10}")
    print("-" * 50)
    personas_ordenadas = sorted(personas, key=lambda x: x[2], reverse=True)

    for persona in personas_ordenadas:
        print(f"{persona[0]:<20}\t\t{persona[1]:<10}\t\t{persona[2]:<10}")
    print()

def calcular_promedio():
    if not personas:
        print("no hay personas en la lista")
        return

    promedio = sum(persona[2] for persona in personas) / len(personas)
    print("\n--- PROMEDIO DE NOTAS ---")
    print(f"El promedio de las notas es: {promedio:.2f}\n")


while True:
    print("\n=== MENÚ PRINCIPAL ===")
    print("1. Agregar persona")
    print("2. Ver lista original")
    print("3. Ver lista ordenada por nota")
    print("4. Calcular promedio")
    print("5. Finalizar")
    opcion = input("Selecciona una opción (1-5): ")

    if opcion == "1":
        ingresar_persona()
    elif opcion == "2":
        mostrar_lista_original()
    elif opcion == "3":
        mostrar_lista_ordenada()
    elif opcion == "4":
        calcular_promedio()
    elif opcion == "5":
        print("adios")
        break
    else:
        print("opcion invalida")

