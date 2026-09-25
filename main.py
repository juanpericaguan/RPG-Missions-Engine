from json_loader import LeerJSON
from mediator import MediatorMision


if __name__ == "__main__":
    lector = LeerJSON('misiones.json')
    misiones = lector.leer()
    detalles_mision = misiones['misiones'][0]

    pasos = misiones['misiones'][0]['pasos']

    mediator = MediatorMision(pasos)

    def main():
        traduccion_de_accion = {
            "1": "combatir",
            "2": "interaccion",
            "3": "recompensa"
        }

        while True:
            print("\n=========================================================")
            print("                 SISTEMA DE MISIONES                     ")
            print("=========================================================")

            print("Mision disponible:")
            print(f"    - {detalles_mision['titulo']}")
            print("Descripción:")
            print(f"    - {detalles_mision['descripcion']}")
            print(f"Nivel recomendado: {detalles_mision['nivel_recomendado']}")

            print("\n¿DESEA INCIAR LA MISIÓN?")
            print("1- Si.")
            print("2- No.\n")

            desicion_incial = input("Decida: ¿1 o 2?: ").strip()
            match desicion_incial:
                case "1":
                    if mediator.terminada:
                        print("Esta misión ya fue completada...")
                        print("¿DESEA REALIZAR LA MISIÓN UNA VEZ MÁS?")

                        accion = input("Escriba 'si' para empezar. Caso contrario pulse cualquier otra tecla: ").strip().lower()
                        if accion != "si":
                            print("Volviendo al menú principal...")
                        else:
                            mediator.reiniciar_mision()

                    while not mediator.terminada:
                        print("\n=========================================================")
                        print(f"             {detalles_mision['titulo']}                         ")
                        print("=========================================================\n")

                        print("Objetivo actual:")
                        print(f"    - {pasos[mediator.indice]['objetivo']}\n")

                        print("¿Qué desea hacer?")
                        print("1. Combate")
                        print("2. Interactuar con aldeano")
                        print("3. Abrir cofre")
                        print("0. Salir")

                        opcion_a_ejecutar = input("Elija un número para la acción que desee realizar: ").strip()
                        if opcion_a_ejecutar == "0":
                            print("SALIENDO DE LA MISIÓN...\n")
                            break

                        elif opcion_a_ejecutar not in traduccion_de_accion:
                            print("Opción inválida. Intente nuevamente.")
                            continue

                        eleccion = traduccion_de_accion[opcion_a_ejecutar] 
                        mediator.eleccion_usuario(eleccion)
                    
                case "2":
                    print("Saliendo del sistema...")
                    break

                case _:
                    print("Opción inválida. Ingrese una opción válida.")


    main()

