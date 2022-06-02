from zope.interface import implementer
from DocenteInvestigador import DocenteInvestigador
from IDirector import IDirector
from ITesorero import ITesorero
from Investigador import Investigador
from Lista import Lista
from Personal import Personal
@implementer(ITesorero)
@implementer(IDirector)
class ManejadorPersonal:
    __lista=None
    def __init__(self):
        self.__lista=Lista()
    def insertarPersonal(self,personal,posicion):
        if isinstance(personal,Personal):
            try:
                self.__lista.insertarElemento(personal,posicion)
            except IndexError:
                print('La posicion ingresada no es correcta.')
            else:
                print('Se inserto correctamente el personal')
        else:
            print('No se pudo añadir un personal a la lista, tipo de dato incorrecto.')
    def agregarPersonal(self,personal):
        if isinstance(personal,Personal):
            self.__lista.agregarElemento(personal)
        else:
            print('No se pudo añadir un personal a la lista, tipo de dato incorrecto.')
    def mostrarPersonal(self,posicion):
        try:
            self.__lista.mostrarElemento(posicion)
        except IndexError:
            print('La posicion ingresada no coincide con ningun personal en la lista.')
    def cantidadPorAreaInvestigacion(self,areaInvestigacion):
        docenteInvestigador=0
        investigador=0
        for personal in self.__lista:
            if type(personal)==Investigador or type(personal)==DocenteInvestigador:
                if personal.getAreaInvestigacion()==areaInvestigacion:
                    if type(personal)==Investigador:
                        investigador+=1
                    else:
                        docenteInvestigador+=1
        print('La cantidad de Docente Investigador es:{}  y la cantidad de Investigador es:{} para el area:{}'.format(docenteInvestigador,investigador,areaInvestigacion))
    def listadoPorCategoriaInvestigacion(self,categoria):
        total=0
        print('{:^20} {:^20} {:^15}'.format('Apellido','Nombre','Importe extra'))
        for personal in self.__lista:
            if type(personal)==DocenteInvestigador:
                if personal.getCategoriaIncentivo()==categoria:
                    print('{:^20} {:^20} {:^15}'.format(personal.getApellido(),personal.getNombre(),personal.getImporteExtra()))
                    total+=personal.getImporteExtra()
        print('Total de dinero a solicitar:',total)
    def listadoOrdenadoSegunCarrera(self,carrera):
        self.__lista.ordenarPorNombre()
        for personal in self.__lista:
            if type(personal)==DocenteInvestigador and personal.getCarrera()==carrera:
                print('Docente investigador:')
                personal.mostrarDatos()
    def listadoOrdenadoApellido(self):
        self.__lista.ordenarPorApellido()
        for personal in self.__lista:
            personal.mostrarDatosYSueldo()
    def toJSON(self):
        d=dict(
            __class__=self.__class__.__name__,
            personal=[personal.toJSON() for personal in self.__lista]
        )
        return d
    def guardarArchivo(self,objectEncoder):
        diccionario=self.toJSON()
        objectEncoder.guardarJSONArchivo(diccionario,'personal.json')
    def gastosSueldoPorEmpleado(self,dni):
        resultado=self.__lista.calcularSueldoEmpleado(dni)
        if resultado==None:
            print('No se encontro el empleado.')
        else:
            print('El sueldo del empleado es:',resultado)
    def modificarBasico(self,dni, nuevoBasico):
        resultado=self.__lista.modificarBasico(dni,nuevoBasico)
        if resultado==-1:
            print('No se encontro el empleado.')
        else:
            print('Se modifico el sueldo basico.')
    def modificarPorcentajeporcargo(self,dni, nuevoPorcentaje):
        resultado=self.__lista.modificarPorcentajeCargo(dni,nuevoPorcentaje)
        if resultado==-1:
            print('No se encontro el empleado.')
        elif resultado==-2:
            print('El dni no corresponde a un docente.')
        else:
            print('Se modifico el porcentaje por cargo.')
    def modificarPorcentajeporcategoría(self,dni, nuevoPorcentaje):
        resultado=self.__lista.modificarPorcentajeCategoria(dni,nuevoPorcentaje)
        if resultado==-1:
            print('No se encontro el empleado.')
        elif resultado==-2:
            print('El dni no corresponde a un personal de apoyo.')
        else:
            print('Se modifico el porcentaje por categoria.')
    def modificarImporteExtra(self,dni, nuevoImporteExtra):
        resultado=self.__lista.modificarImporteExtra(dni,nuevoImporteExtra)
        if resultado==-1:
            print('No se encontro el empleado.')
        elif resultado==-2:
            print('El dni no corresponde a un docente investigador.')
        else:
            print('Se modifico el importe extra.')