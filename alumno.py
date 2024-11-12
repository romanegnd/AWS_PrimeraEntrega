class Alumno : 
    def __init__ (self, id, nombres, apellidos, matricula, promedio): 
        #test on format
        if not isinstance(id, int):
            raise ValueError("ID debe ser un int")
        if not isinstance(nombres, str):
            raise ValueError("Nombres debe ser un str")
        if not isinstance(apellidos, str):
            raise ValueError("Apellidos debe ser un str")
        if not isinstance(matricula, str):
            raise ValueError("Número de Empleado debe ser ser un str que empieza con A")
        if not isinstance(promedio, (int, float)) or promedio < 0 or promedio > 100:
            raise ValueError("Horas de Clase debe ser un número entre 0 y 100")
        
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


