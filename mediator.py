from components import Jugador, Enemigo, NPC, Cofre
from states import NivelCombate, NivelInteraccion, NivelRecompensa

class MediatorMision:
    TIPOS_VALIDOS = {"combatir", "interaccion", "recompensa"}

    def __init__(self, pasos):
        self._validar_pasos(pasos)

        self.pasos = pasos
        self.indice = 0
        self.state = self._crear_estado_actual()
        self.terminada = False


        self.jugador = Jugador(self)
        self.enemigo = Enemigo(self)
        self.npc = NPC(self)
        self.cofre = Cofre(self)
        self.TIPO_A_OBJETIVO = {
            "combatir": self.enemigo.muere,
            "interaccion": self.npc.hablar,
            "recompensa": self.cofre.abrir
        }

        self.RESULTADO_A_ACCION = {
            "ENEMIGO_DERROTADO": self._accion_enemigo_derrotado,
            "NPC_HABLADO": self._accion_npc_hablado,
            "COFRE_ABIERTO": self._accion_abrir_cofre,
            "ACCION_INVALIDA": self._accion_invalida
        }

    def _validar_pasos(self, pasos):
        for idx, paso in enumerate(pasos):
            if "tipo" not in paso:
                raise ValueError(f"Paso {idx} no tiene clave 'tipo'")
            
            if paso['tipo'] not in self.TIPOS_VALIDOS:
                raise ValueError(
                    f"Tipo de paso inválido en paso {idx}: {paso['tipo']}"
                )

    def _crear_estado_actual(self):
        TIPO_A_ESTADO = {
            "combatir": NivelCombate,
            "interaccion": NivelInteraccion,
            "recompensa": NivelRecompensa
        }

        tipo = self.pasos[self.indice]['tipo']
        return TIPO_A_ESTADO[tipo]()
    
    def avanzar(self):
        self.indice += 1
        if self.indice < len(self.pasos):
            self.state = self._crear_estado_actual()
            self.ejecutar_paso_actual()
        else:
            print("Misión finalizada.")
            self.terminada = True

    def ejecutar_paso_actual(self):
        tipo = self.pasos[self.indice]['tipo']
        self.TIPO_A_OBJETIVO[tipo]()

    def _accion_enemigo_derrotado(self):
        print("Enemigo derrotado... avanzando al siguiente nivel.")
        self.avanzar()

    def _accion_npc_hablado(self):
        print("Acercandose a hablar con el npc...")
        self.avanzar()

    def _accion_abrir_cofre(self):
        print("COFRE ABIERTO... Has completado la misión.")
        self.jugador.mejorar()
        self.avanzar()

    def _accion_invalida(self):
        print("Acción no permitida en este estado.")

    def matar_enemigo(self):
        resultado = self.state.matar_enemigo(self)
        self.RESULTADO_A_ACCION[resultado]()

    def hablar_npc(self):
        resultado = self.state.hablar_npc(self)
        self.RESULTADO_A_ACCION[resultado]()

    def abrir_cofre(self):
        resultado = self.state.abrir_cofre(self)
        self.RESULTADO_A_ACCION[resultado]()
        