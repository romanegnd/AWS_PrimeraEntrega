class Alumno : 
    def __init__ (self, id, nombres, apellidos, matricula, promedio): 
        #test on format
        if not isinstance(id, int):
            raise ValueError("ID debe ser un int")
        if not nombres or not isinstance(nombres, str):
            raise ValueError("Nombres debe ser un str")
        if not apellidos or not isinstance(apellidos, str):
            raise ValueError("Apellidos debe ser un str")
        if not matricula or not isinstance(matricula, str):
            raise ValueError("Número de Empleado debe ser ser un str que empieza con A")
        if not isinstance(promedio, (int, float)) or promedio < 0 or promedio > 10:
            raise ValueError("Horas de Clase debe ser un número entre 0 y 10")
    
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

