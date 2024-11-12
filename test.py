import requests

response = requests.get("http://127.0.0.1:5000/alumnos")
try:
    json_data = response.json()  # essaie de convertir la réponse en JSON
    print("La réponse est un JSON :", json_data)
except ValueError:
    print("La réponse n'est pas un JSON.")

