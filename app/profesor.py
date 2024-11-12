class Profesor : 
    def __init__ (self, id, numeroEmpleado, nombres, apellidos, horasClase):

        #test on format
        if not isinstance(id, int):
            raise ValueError("ID debe ser un int")
        if not nombres or not isinstance(nombres, str):
            raise ValueError("Nombres debe ser un str")
        if not apellidos or not isinstance(apellidos, str):
            raise ValueError("Apellidos debe ser un str")
        if not numeroEmpleado or not isinstance(numeroEmpleado, int):
            raise ValueError("Número de Empleado debe ser ser un int")
        if not isinstance(horasClase, (int, float)) or horasClase < 0:
            raise ValueError("Horas de Clase debe ser un número positivo")


        self.id = id
        self.numeroEmpleado = numeroEmpleado
        self.nombres = nombres
        self.apellidos = apellidos
        self.horasClase = horasClase

    def to_dict(self):
        """Convert Profesor to a dictionary."""
        return {
            "id": self.id,
            "numeroEmpleado": self.numeroEmpleado,
            "nombres": self.nombres,
            "apellidos": self.apellidos,
            "horasClase": self.horasClase
        }



    

