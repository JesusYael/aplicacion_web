import web
import requests

urls = ("/", "index")
app = web.application(urls, globals())
render = web.template.render('templates/')

class index:
    def GET(self):

        api_url = 'https://api-rest-4-71ba.onrender.com/nombre'
        # Realizar la petición GET a tu API local
        response = requests.get(api_url)

        # Verificamos que la respuesta sea exitosa (código 200)
        if response.status_code == 200:
            data = response.json()  # Obtenemos la respuesta en formato JSON
            # Asumiendo que tu API retorna un JSON con clave 'mensaje' y 'valor'
            nombre = data.get('nombre', 'desconocido')

            # Pasamos los datos a la plantilla
            return render.index(nombre)
        else:
            return "Error al consumir la API: " + str(response.status_code)


if __name__ == "__main__":
    app.run()