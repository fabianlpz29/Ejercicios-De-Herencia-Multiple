from Estudiante import Estudiante #importacion de la clase estudiante
from Materia import Materia #importacion de la clase materia 
from Materia import materia #importacion del objeto materia de la clase Msteria
from Estudiante import alumno #importacion del objeto alumno de la clase Estudiante

class Nota(Estudiante,Materia): #clase

    def __init__(self,notaLaboratorio, notaParcial): #constructor de la clase
        self.notaLaboratorio =  notaLaboratorio #nota de laboratorio
        self.notaParcial = notaParcial #nota de parcial
    
    def Calificar(self):
        return 'El alumno {}, obtuvo un {} en su nota de laboratorio y obtuvo un {} en la nota de parcial en la materia de {}'.format(alumno.nombreEstudiante,self.notaLaboratorio,self.notaParcial,materia.nombreMateria)
    
notas =  Nota(7,8) #objeto de la clase

print(notas.Calificar())

