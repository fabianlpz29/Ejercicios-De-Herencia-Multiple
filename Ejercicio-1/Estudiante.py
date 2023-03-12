class Estudiante: #Clase
    pass

    def __init__(self, nombreEstudiante, carreraEstudiante):#Constructor de la clase estudiante
        self.nombreEstudiante = nombreEstudiante #nombre del estudiante
        self.carreraEstudiante = carreraEstudiante #nombre de la carrera del estudiante

alumno = Estudiante("fabian","ing. en desarrollo software") #objeto de la clase estudiante