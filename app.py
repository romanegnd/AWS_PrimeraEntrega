from flask import Flask, jsonify, request, abort
from alumno import Alumno
from profesor import Profesor


app = Flask(__name__)

alumnos=[
    Alumno(1, "Manon", "Georges", "A001", 90), 
    Alumno(2, "Teddy", "Gesbert", "A002", 88.7), 
    Alumno(3, "Théo", "Buan", "A003", 8.4)
]

profesores = [
    Profesor(1, "E001", 'Juan', "Gomez", 40), 
    Profesor(2, "E002", "Jesus", "Hidalgo", 20), 
    Profesor(3, "E003", "Lucia", "Alvarez", 15)
]

#______________________________ALUMNOS
# GET /alumnos
@app.route('/alumnos', methods=['GET'])
def get_alumnos():
    try:
        return jsonify([alumno.to_dict() for alumno in alumnos]), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# GET /alumnos/{id}
@app.route('/alumnos/<int:id>', methods=['GET'])
def get_alumno_by_id(id):
    try:
        alumno = next((alumno for alumno in alumnos if alumno.id == id), None)
        if alumno is None:
            abort(404, description="ID no encontrado")
        return jsonify(alumno.to_dict()), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# POST /alumnos
@app.route('/alumnos', methods=['POST'])
def add_alumno():
    try:
        data = request.get_json()
        #tests on formats :
        if (not 'id' in data) or (not isinstance(data.get('id'), int)):
            return jsonify({"error": "id must exist and be a integer"}), 400
        if (not 'nombres' in data) or (not isinstance(data.get('nombres'), str)):
            return jsonify({"error": "nombres must exist and be a string"}), 400
        if (not 'apellidos' in data) or (not isinstance(data.get('apellidos'), str)):
            return jsonify({"error": "apellidos must exist and be a string"}), 400
        if (not 'matricula' in data) or (not isinstance(data.get('matricula'), str)) or data['matricula'][0]!='A' :
            return jsonify({"error": "matricula must exist and be a string"}), 400
        if (not 'promedio' in data) or not isinstance(data.get('promedio'), float) or not (0.0 <= data.get('promedio') <= 100.0):
            return jsonify({"error": "promedio must exist and be a float between 0.0 and 100.0"}), 400

        nuevo_alumno = Alumno(data['id'], data['nombres'], data['apellidos'], data['matricula'], data["promedio"])
        alumnos.append(nuevo_alumno)
        return jsonify(nuevo_alumno.to_dict()), 201
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# PUT /alumnos/{id}
@app.route('/alumnos/<int:id>', methods=['PUT'])
def update_alumno(id):
    try: 
        alumno = next((alumno for alumno in alumnos if alumno.id == id), None)
        if alumno is None:
            abort(404, description="ID no encontrado")

        data = request.get_json() # JSON of the request

        if 'id' in data:
            if not isinstance(data.get('id'), int):
                return jsonify({"error": "id must be a int"}), 400
            alumno.set_nombres(data['id'])

        if 'nombres' in data:
            if not isinstance(data.get('nombres'), str):
                return jsonify({"error": "nombres must be a string"}), 400
            alumno.set_nombres(data['nombres'])

        if 'apellidos' in data:
            if not isinstance(data.get('apellidos'), str):
                return jsonify({"error": "apellidos must be a string"}), 400
            alumno.set_apellidos(data['apellidos'])

        if 'matricula' in data:
            if not isinstance(data.get('matricula'), str) or data['matricula'][0]!='A':
                return jsonify({"error": "matricula must be a string"}), 400
            alumno.set_matricula(data['matricula'])

        if 'promedio' in data:
            if not isinstance(data.get('promedio'), float) or not (0.0 <= data.get('promedio') <= 100.0):
                return jsonify({"error": "promedio must be a float between 0.0 and 100.0"}), 400
            alumno.set_promedio(data['promedio'])
    
    except Exception as e:
        return jsonify({"error": str(e)}), 500


# DELETE /alumnos/{id}
@app.route('/alumnos/<int:id>', methods=['DELETE'])
def delete_alumno(id):
    try:
        global alumnos
        alumno = next((alumno for alumno in alumnos if alumno.id == id), None)
        if alumno is None:
            return jsonify({"error": "ID no encontrado"}), 404
    
        alumnos = [alumno for alumno in alumnos if alumno.id != id]
        return 'Eliminación exitosa', 204
    except Exception as e:
        return jsonify({"error": str(e)}), 500


#______________________________PROFESORES
#  GET /profesores
@app.route('/profesores', methods=['GET'])
def get_profesores():
    try:
        return jsonify([profesor.to_dict() for profesor in profesores]), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# GET /profesores/{id}
@app.route('/profesores/<int:id>', methods=['GET'])
def get_profesor_by_id(id):
    try:
        profesor = next((profesor for profesor in profesores if profesor.id == id), None)
        if profesor is None:
            abort(404, description="ID no encontrado")
        return jsonify(profesor.to_dict()), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500
    
# POST /profesores
@app.route('/profesores', methods=['POST'])
def add_profesor():
    try:
        data = request.get_json()
        #Checks that the data is in the correct format
        if (not 'id' in data) or (not isinstance(data.get('id'), int)):
            return jsonify({"error": "id must exist and be a integer"}), 400
        if (not 'numeroEmpleado' in data) or (not isinstance(data.get('numeroEmpleado'), int)) or data['numeroEmpleado']<0:  #peut etre un float ?????
            return jsonify({"error": "numeroEmpleado must exist and be an integer"}), 400
        if (not 'nombres' in data) or (not isinstance(data.get('nombres'), str)):
            return jsonify({"error": "nombres must exist and be a string"}), 400
        if (not 'apellidos' in data) or (not isinstance(data.get('apellidos'), str)):
            return jsonify({"error": "apellidos must exist and be a string"}), 400
        if (not 'horasClase' in data) or (not isinstance(data.get('horasClase'), int)) or data['horasClase']<0 :  #peut etre un float ?????
            return jsonify({"error": "horasClase must exist and be an integer"}), 400
        
        nuevo_profesor = Profesor(data['id'], data['nombres'], data['apellidos'], data['horasClase'])
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
            abort(404, description="ID no encontrado") 

        data = request.get_json()

        if 'id' in data:
            if not isinstance(data.get('id'), int):
                return jsonify({"error": "id must be a int"}), 400
            profesor.set_nombres(data['id'])

        if 'numeroEmpleado' in data:
            if not isinstance(data['numeroEmpleado'], int) or data['numeroEmpleado']<0 :  #peut etre un float ?????
                return jsonify({"error": "numeroEmpleado must be an integer"}), 400
            profesor.set_numeroEmpleado(data['numeroEmpleado'])

        if 'nombres' in data:
            if not isinstance(data['nombres'], str):
                return jsonify({"error": "nombres must be a string"}), 400
            profesor.set_nombres(data['nombres'])

        if 'apellidos' in data:
            if not isinstance(data['apellidos'], str):
                return jsonify({"error": "apellidos must be a string"}), 400
            profesor.set_apellidos(data['apellidos'])

        if 'horasClase' in data:
            if not isinstance(data['horasClase'], int) or data['horasClase']<0 :  #peut etre un float ?????
                return jsonify({"error": "horasClase must be an integer"}), 400
            profesor.set_horasClase(data['horasClase'])

        return jsonify(profesor.to_dict()), 200
    
    except Exception as e:
        return jsonify({"error": str(e)}), 500


# DELETE /profesores/{id}
@app.route('/profesores/<int:id>', methods=['DELETE'])
def delete_profesor(id):
    try:
        global profesores
        profesor = next((profesor for profesor in profesores if profesor.id == id), None)
        if profesor is None:
            return jsonify({"error": "ID no encontrado"}), 404
    
        profesores = [profesor for profesor in profesores if profesor.id != id]
        return 'Eliminación exitosa', 204
    except Exception as e:
        return jsonify({"error": str(e)}), 500
    