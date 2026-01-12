class Jugador:
    def __init__(self, mediator):
        self.mediator = mediator

    def mejorar(self):
        print("Aplicando mejoras de nivel al jugador...")

class Enemigo:
    def __init__(self, mediator):
        self.mediator = mediator

    def muere(self):
        self.mediator.matar_enemigo()

class NPC:
    def __init__(self, mediator):
        self.mediator = mediator

    def hablar(self):
        self.mediator.hablar_npc()

class Cofre:
    def __init__(self, mediator):
        self.mediator = mediator

    def abrir(self):
        self.mediator.abrir_cofre()