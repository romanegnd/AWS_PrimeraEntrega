class Alumno : 
    def __init__ (self, id, nombres, apellidos, matricula, promedio): 
        self.id = id
        self.nombres = nombres
        self.apellidos = apellidos
        self.matricula = matricula
        self.promedio = promedio

    def to_dict(self):
        """Convert Alumno to a dictionary => JSON."""
        return {
            "id": self.id,
            "nombres": self.nombres,
            "apellidos": self.apellidos,
            "matricula": self.matricula, 
            "promedio": self.promedio
        }
    
    def set_nombres(self, nuevos_nombres) : 
        self.nombres = nuevos_nombres
    
    def set_apellidos(self, nuevos_apellidos) : 
        self.apellidos = nuevos_apellidos

    def set_matricula(self, nueva_matricula) : 
        self.matricula = nueva_matricula

    def set_promedio(self, nuevo_promedio) : 
        self.promedio = nuevo_promedio


