import json
class LeerJSON:
    def __init__(self, file):
        self.file = file

    def leer(self):
        with open(self.file, "r", encoding="utf-8") as archivo:
            datos = json.load(archivo)
        
        for mision in datos['misiones']:
            print(f"Misión: {mision['titulo'].capitalize()}")
            print(f"Descripción: {mision['descripcion'].capitalize()}\n")
            print("Pasos:")
            for idx, paso in enumerate(mision['pasos'], 1):
                print(f"{idx}- [{paso['tipo'].title()}] {paso['objetivo']}")
            
        return datos

if __name__ == "__main__":
    lectura = LeerJSON("misiones.json")
    lectura.leer()