class Persona(object):
    def __init__(self):
        self.nombres = ''
        self.edad = 0

    def setNombres(self, n):
        self.nombres = n

    def setEdad(self, n):
        self.edad = n

    def getEdad(self):
        return self.edad

    def getNombre(self):
        return self.nombres

    def presentarDatos(self):
        c = '%s - %s' % (self.getEdad(), self.getNombre())
        return c


class Estudiante(Persona):

    def __init__(self):
        super(Estudiante, self).__init__()
        self.nota = 0

    def  setNota(self,n):
        self.nota = n

    def getNota(self):
        return self.nota

    def presentar_datos(self):
        c = '%s - %s -%s' % (self.nombres, self.edad, self.nota)
        c = '%s - %s' % (super(Estudiante, self).presentarDatos(),
                         self.nota)
        return c
