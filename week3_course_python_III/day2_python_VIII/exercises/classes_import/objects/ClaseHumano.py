class humano:
    def __init__(self, nombre, armadura, nivel, ataque, ojos=2, piernas=2, dientes=32,salud=100):
        self.ojos=ojos
        self.piernas=piernas
        self.dientes=dientes
        self.nombre=nombre
        self.armadura=armadura
        self.nivel=nivel
        self.ataque=ataque
        self.salud=salud
    def atacar_humano(self,orco):
        orco.salud=orco.salud-(self.ataque-orco.armadura)
        print(orco.salud)
        return(orco.salud)
    def no_vivo_humano(self):
        if self.salud<=0:
            return(True)
        else:
            return(False)
    def todos_atributos_humano(self):
        print(f"ojos:{self.ojos} | piernas: {self.piernas} | dientes:{self.dientes} |\
            nombre:{self.nombre}  | armadura:{self.armadura} | nivel:{self.nivel} |\
                ataque:{self.ataque} | salud:{self.salud}")