from Apoyo import Apoyo
from Docente import Docente
from DocenteInvestigador import DocenteInvestigador
from Investigador import Investigador
class MenuDirector:
    __opciones={}
    def __init__(self):
        self.__opciones={
            1:self.opcion1,
            2:self.opcion2,
            3:self.opcion3,
            4:self.opcion4,
            5:self.salir
        }
    def lanzarMenu(self,manejadorPersonal):
        #Menu opciones
        i=len(self.__opciones)
        opcion=0
        while(i!=opcion):
            print('Menu:')
            print('-Ingrese 1 para modificar el sueldo básico de un agente.')
            print('-Ingrese 2 para modificar el porcentaje que se paga por cargo a un docente.')
            print('-Ingrese 3 el porcentaje que se paga por categoría a un personal de apoyo.')
            print('-Ingrese 4 para modificar el importe extra que se paga a un docente investigador.')
            print('-Ingrese 5 para salir.')
            opcion=self.cargarNumeroEntero('Ingrese opcion:\n')
            ejecutar=self.__opciones.get(opcion,self.error)
            if opcion>0 and opcion<5:
                ejecutar(manejadorPersonal)
            else:
                ejecutar()
    def opcion1(self,manejadorPersonal):
        manejadorPersonal.listadoOrdenadoSegunCarrera('')
        dni=input('Ingrese DNI:\n')
        nuevoBasico=self.cargarFlotante('Ingrese nuevo sueldo basico:\n')
        manejadorPersonal.modificarBasico(dni,nuevoBasico)
    def opcion2(self,manejadorPersonal):
        dni=input('Ingrese DNI:\n')
        nuevoPorcentaje=self.cargarFlotante('Ingrese el nuevo porcentaje del docente:\n')
        manejadorPersonal.modificarPorcentajeporcargo(dni,nuevoPorcentaje)
    def opcion3(self,manejadorPersonal):
        dni=input('Ingrese DNI:\n')
        nuevoPorcentaje=self.cargarFlotante('Ingrese el nuevo porcentaje del personal de apoyo:\n')
        manejadorPersonal.modificarPorcentajeporcategoría(dni,nuevoPorcentaje)
    def opcion4(self,manejadorPersonal):
        dni=input('Ingrese DNI:\n')
        nuevoImporteExtra=self.cargarFlotante('Ingrese el nuevo importe extra:\n')
        manejadorPersonal.modificarImporteExtra(dni, nuevoImporteExtra)
    def cargarNumeroEntero(self,mensaje='Ingrese valor:'):
        numero=None
        bandera=True
        while bandera:
            try:
                numero=int(input(mensaje))
            except ValueError:
                print('ERROR: Se debe ingresar un numero entero.')
            else:
                bandera=False
        return numero
    def cargarFlotante(self,mensaje='Ingrese valor:'):
        numero=None
        bandera=True
        while bandera:
            try:
                numero=int(input(mensaje))
            except ValueError:
                print('ERROR: Se admiten numeros enteros y punto ,por ejemplo:500 o 500.50')
            else:
                bandera=False
        return numero
    def error(self):
        #Mensaje cuando ingresa opcion incorrecta
        print('Opción incorrecta')
    def salir(self):
        #Mensaje cuando decide salir
        print('Se cerro el menú')