from abc import ABC, abstractmethod

class NivelState(ABC):
    @abstractmethod
    def matar_enemigo(self, mediator):
        raise NotImplementedError
    
    @abstractmethod
    def hablar_npc(self, mediator):
        raise NotImplementedError
    
    @abstractmethod
    def abrir_cofre(self, mediator):
        raise NotImplementedError
    
# ========= NIVELES =================

class NivelCombate(NivelState):
    def matar_enemigo(self, mediator):
        return "ENEMIGO_DERROTADO"

    def hablar_npc(self, mediator):
        return "ACCION_INVALIDA"

    def abrir_cofre(self, mediator):
        return "ACCION_INVALIDA"

class NivelInteraccion(NivelState):
    def matar_enemigo(self, mediator):
        return "ACCION_INVALIDA"

    def hablar_npc(self, mediator):
        return "NPC_HABLADO"

    def abrir_cofre(self, mediator):
        return "ACCION_INVALIDA"

class NivelRecompensa(NivelState):
    def matar_enemigo(self, mediator):
        return "ACCION_INVALIDA"

    def hablar_npc(self, mediator):
        return "ACCION_INVALIDA"

    def abrir_cofre(self, mediator):
        return "COFRE_ABIERTO"