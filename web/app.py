import web
import requests
import os  # Importar os para acceder a las variables de entorno

urls = ("/", "index")
app = web.application(urls, globals())
render = web.template.render('templates/')

class index:
    def GET(self):
        api_url = 'https://api-rest-4-71ba.onrender.com/nombre'
        response = requests.get(api_url)
        if response.status_code == 200:
            data = response.json()
            nombre = data.get('nombre', 'desconocido')
            return render.index(nombre)
        else:
            return "Error al consumir la API: " + str(response.status_code)

if __name__ == "__main__":
    # Obtener el puerto de la variable de entorno PORT, Render la asigna automáticamente
    port = int(os.environ.get('PORT', 8080))  # 8080 es el valor por defecto si no está PORT
    web.httpserver.runsimple(app.wsgifunc(), ('0.0.0.0', port))
