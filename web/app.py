import web
import requests
import os

urls = ("/", "index")
app = web.application(urls, globals())
render = web.template.render('templates/')

class index:
    def GET(self):
        try:
            api_url = 'https://api-rest-4-71ba.onrender.com/nombre'
            response = requests.get(api_url)

            if response.status_code == 200:
                data = response.json()
                nombre = data.get('nombre', 'desconocido')
                return render.index(nombre)
            else:
                return f"Error al consumir la API: {response.status_code}"
        except Exception as e:
            return f"Error: {str(e)}"



if __name__ == "__main__":
    app.run(port=int(os.environ.get("PORT", 8080)))
