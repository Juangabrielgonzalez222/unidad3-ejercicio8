from Personal import Personal
class Apoyo(Personal):
    __categoria=0
    __porcentaje=None
    def __init__(self, cuil='', apellido='', nombre='', sueldoBasico=0, antiguedad=0,categoria=0):
        super().__init__(cuil, apellido, nombre, sueldoBasico, antiguedad)
        self.__categoria=categoria
        self.__porcentaje=None
    def toJSON(self):
        d = dict(
            __class__=self.__class__.__name__,
            __atributos__=dict(super().toJSON(),categoria=self.__categoria))
        return d
    def calcularSueldo(self):
        resultado=0
        if self.__porcentaje==None:
            porcentaje=0
            if self.__categoria>0 and self.__categoria<11:
                porcentaje+=10
            elif self.__categoria>10 and self.__categoria<21:
                porcentaje+=20
            elif self.__categoria>20 and self.__categoria<23:
                porcentaje+=30
            resultado=self.getSueldoBasico()+self.calcularPorAntiguedad()+((self.getSueldoBasico()*porcentaje)/100)
        else:
            resultado=self.getSueldoBasico()+self.calcularPorAntiguedad()+self.__porcentaje
        return resultado
    def setPorcentaje(self,porcentaje):
        self.__porcentaje=porcentaje
    def tipoAgente(self):
        return 'Apoyo'