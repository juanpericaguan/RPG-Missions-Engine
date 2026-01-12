import json_loader
import mediator


if __name__ == "__main__":
    lector = json_loader.LeerJSON('misiones.json')
    misiones = lector.leer()

    pasos = misiones['misiones'][0]['pasos']

    mediator = mediator.MediatorMision(pasos)
    while not mediator.terminada:
        mediator.ejecutar_paso_actual()

