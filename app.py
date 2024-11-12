from flask import Flask, jsonify, request
from alumno import Alumno
from profesor import Profesor


app = Flask(__name__)

"""
alumnos=[
    Alumno(1, "Manon", "Georges", "A001", 90), 
    Alumno(2, "Teddy", "Gesbert", "A002", 88.7), 
    Alumno(3, "Theo", "Buan", "A003", 8.4)
]

profesores = [
    Profesor(1, "E001", 'Juan', "Gomez", 40), 
    Profesor(2, "E002", "Jesus", "Hidalgo", 20), 
    Profesor(3, "E003", "Lucia", "Alvarez", 15)
]
"""
alumnos = []
profesores = []


#______________________________ALUMNOS
# GET /alumnos
@app.route('/alumnos', methods=['GET'])
def get_alumnos():
    return jsonify([alumno.to_dict() for alumno in alumnos]), 200

# GET /alumnos/{id}
@app.route('/alumnos/<int:id>', methods=['GET'])
def get_alumno_by_id(id):
    alumno = next((alumno for alumno in alumnos if alumno.id == id), None)
    if alumno is None:
        return jsonify({'error' : 'ID no encontrado'}), 404
    return jsonify(alumno.to_dict()), 200
    

# POST /alumnos
@app.route('/alumnos', methods=['POST'])
def add_alumno():
    try:
        data = request.get_json()
        if not 'id' in data or not 'nombres' in data or not 'apellidos' in data or not 'matricula' in data or not 'promedio' in data : 
            return jsonify('Los campos id, nombres, apellidos, matricula et promedio deben ser completos'), 400

        nuevo_alumno = Alumno(data['id'], data['nombres'], data['apellidos'], data['matricula'], data["promedio"])
        alumnos.append(nuevo_alumno)
        return jsonify(nuevo_alumno.to_dict()), 201
    except (KeyError, ValueError) as e:
        return jsonify({"error": str(e)}), 500

# PUT /alumnos/{id}
@app.route('/alumnos/<int:id>', methods=['PUT'])
def update_alumno(id):
    try: 
        alumno = next((alumno for alumno in alumnos if alumno.id == id), None)
        if alumno is None:
            return jsonify({'error' : 'ID no encontrado'}), 404

        data = request.get_json() # JSON of the request

        #tests
        if 'nombres' in data and not isinstance(data.get('nombres'), str):
            return jsonify({"error": "nombres must be a string"}), 400
        if 'apellidos' in data and not isinstance(data.get('apellidos'), str):
            return jsonify({"error": "apellidos must be a string"}), 400
        if 'promedio' in data and not isinstance(data.get('promedio'), float) or not (0.0 <= data.get('promedio') <= 100.0):
            return jsonify({"error": "promedio must be a float between 0.0 and 100.0"}), 400
        alumno.nombres = data.get('nombres', alumno.nombres)
        alumno.apellidos = data.get('apellidos', alumno.apellidos)
        alumno.promedio = data.get('promedio', alumno.promedio)
        return jsonify(alumno.to_dict()), 200
    except ValueError as e:
        return jsonify({"error": str(e)}), 400


# DELETE /alumnos/{id}
@app.route('/alumnos/<int:id>', methods=['DELETE'])
def delete_alumno(id):
    global alumnos
    alumno = next((alumno for alumno in alumnos if alumno.id == id), None)
    if alumno is None:
        return jsonify({"error": "ID no encontrado"}), 404
    
    alumnos = [alumno for alumno in alumnos if alumno.id != id]
    return jsonify({'message': 'Eliminación exitosa'}) , 200


#______________________________PROFESORES
#  GET /profesores
@app.route('/profesores', methods=['GET'])
def get_profesores():
    return jsonify([profesor.to_dict() for profesor in profesores]), 200

# GET /profesores/{id}
@app.route('/profesores/<int:id>', methods=['GET'])
def get_profesor_by_id(id):
    profesor = next((profesor for profesor in profesores if profesor.id == id), None)
    if profesor is None:
        return jsonify({'error' : 'ID no encontrado'}), 404
    return jsonify(profesor.to_dict()), 200
    
# POST /profesores
@app.route('/profesores', methods=['POST'])
def add_profesor():
    try:
        data = request.get_json()
        if not 'id' in data or not 'numeroEmpleado' in data or not 'nombres' in data or not 'apellidos' in data or not 'horasClase' in data : 
            return jsonify('Los campos id, numeroEmpleado, nombres, apellidos y horasClase deben ser completos'), 400
        
        nuevo_profesor = Profesor(data['id'], data['numeroEmpleado'], data['nombres'], data['apellidos'], data['horasClase'])
        profesores.append(nuevo_profesor)
        return jsonify(nuevo_profesor.to_dict()), 201
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# PUT /profesores/{id}
@app.route('/profesores/<int:id>', methods=['PUT'])
def update_profesor(id):
    try:
        profesor = next((profesor for profesor in profesores if profesor.id == id), None)
        if profesor is None:
            return jsonify({'error' : 'ID no encontrado'}), 404 

        data = request.get_json()

        if 'nombres' in data and not isinstance(data['nombres'], str):
            return jsonify({"error": "nombres must be a string"}), 400
        if 'apellidos' in data and not isinstance(data['apellidos'], str):
            return jsonify({"error": "apellidos must be a string"}), 400
        if 'horasClase' in data and not isinstance(data['horasClase'], (int, float)) or data['horasClase']<0 :  #peut etre un float ?????
            return jsonify({"error": "horasClase must be an integer"}), 400
        
        profesor.nombres = data.get('nombres', profesor.nombres)
        profesor.apellidos = data.get('apellidos', profesor.apellidos)
        profesor.horasClase = data.get('promedio', profesor.horasClase)
        return jsonify(profesor.to_dict()), 200

    except ValueError as e:
        return jsonify({"error": str(e)}), 400


# DELETE /profesores/{id}
@app.route('/profesores/<int:id>', methods=['DELETE'])
def delete_profesor(id):
    global profesores
    profesor = next((profesor for profesor in profesores if profesor.id == id), None)
    if profesor is None:
        return jsonify({"error": "ID no encontrado"}), 404
    
    profesores = [profesor for profesor in profesores if profesor.id != id]
    return jsonify({'message': 'Eliminación exitosa'}) , 200
    