from flask import Flask, jsonify, request
from alumno import Alumno
from profesor import Profesor


app = Flask(__name__)


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
    data = request.get_json()
    try:
        nuevo_alumno = Alumno(data['id'], data['nombres'], data['apellidos'], data['matricula'], data["promedio"])
        alumnos.append(nuevo_alumno)
        return jsonify(nuevo_alumno.to_dict()), 201
    except (KeyError, ValueError) as e:
        return jsonify({"error": str(e)}), 400

# PUT /alumnos/{id}
@app.route('/alumnos/<int:id>', methods=['PUT'])
def update_alumno(id):
    data = request.get_json() # JSON of the request
    alumno = next((alumno for alumno in alumnos if alumno.id == id), None)
    if alumno is None:
        return jsonify({'error' : 'ID no encontrado'}), 404
    try: 
        #tests
        if 'nombres' in data and (not data['nombres'] or not isinstance(data['nombres'], str)):
            return jsonify({"error": "Nombres invalidos"}), 400
        if 'apellidos' in data and (not data['apellidos'] or not isinstance(data['apellidos'], str)):
            return jsonify({"error": "Apellidos invalidos"}), 400
        if 'promedio' in data and (not isinstance(data['promedio'], (int, float)) or data['promedio'] < 0 or data['promedio'] > 10):
            return jsonify({"error": "promedio invalido"}), 400
        
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
    return jsonify({'message': 'Eliminacion exitosa'}) , 200


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
    data = request.get_json()
    try:
        nuevo_profesor = Profesor(data['id'], data['numeroEmpleado'], data['nombres'], data['apellidos'], data['horasClase'])
        profesores.append(nuevo_profesor)
        return jsonify(nuevo_profesor.to_dict()), 201
    except (KeyError, ValueError) as e:
        return jsonify({'error': str(e)}), 400

# PUT /profesores/{id}
@app.route('/profesores/<int:id>', methods=['PUT'])
def update_profesor(id):
    data = request.get_json()
    profesor = next((profesor for profesor in profesores if profesor.id == id), None)
    if profesor is None:
        return jsonify({'error' : 'ID no encontrado'}), 404 
    try:
        if 'nombres' in data and (not data['nombres'] or not isinstance(data['nombres'], str)):
            return jsonify({"error": "nombres invalidos"}), 400
        if 'apellidos' in data and (not data['apellidos'] or not isinstance(data['apellidos'], str)):
            return jsonify({"error": "apellidos invalidos"}), 400
        if 'horasClase' in data and (not isinstance(data['horasClase'], (int, float)) or data['horasClase'] < 0) : 
            return jsonify({"error": "horasClase invalidas"}), 400
        
        profesor.nombres = data.get('nombres', profesor.nombres)
        profesor.apellidos = data.get('apellidos', profesor.apellidos)
        profesor.horasClase = data.get('horasClase', profesor.horasClase)
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
    return jsonify({'message': 'Eliminacion exitosa'}) , 200


if __name__ == '__main__':
    app.run(debug=True)