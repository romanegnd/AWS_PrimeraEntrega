class Profesor : 
    def __init__ (self, id, numeroEmpleado, nombres, apellidos, horasClase):
        self.id = id
        self.numeroEmpleado = numeroEmpleado
        self.nombres = nombres
        self.apellidos = apellidos
        self.horasClase = horasClase

    def to_dict(self):
        """Convert Profesor to a dictionary => JSON."""
        return {
            "id": self.id,
            "numeroEmpleado": self.numeroEmpleado,
            "nombres": self.nombres,
            "apellidos": self.apellidos,
            "horasClase": self.horasClase
        }

    def set_numeroEmpleado(self, nuevo_numeroEmpleado) : 
        self.numeroEmpleado = nuevo_numeroEmpleado

    def set_nombres(self, nuevos_nombres) : 
        self.nombres = nuevos_nombres
    
    def set_apellidos(self, nuevos_apellidos) : 
        self.apellidos = nuevos_apellidos

    def set_horasClase(self, nuevas_horasClase) : 
        self.horasClase = nuevas_horasClase
    



    

