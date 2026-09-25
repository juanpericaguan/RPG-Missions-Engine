import json
class LeerJSON:
    def __init__(self, file):
        self.file = file

    def leer(self):
        with open(self.file, "r", encoding="utf-8") as archivo:
            datos = json.load(archivo)
            
        return datos


if __name__ == "__main__":
    lectura = LeerJSON("misiones.json")
    lectura.leer()