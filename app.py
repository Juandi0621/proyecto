from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)


# Página de inicio
@app.route("/")
def index():
    return render_template("index.html")


# Página "Quiénes somos"
@app.route("/somos")
def somos():
    return render_template("somos.html")


# Página "Contenido"
@app.route("/contenido")
def contenido():
    return render_template("contenido.html")


# Página de contacto
@app.route("/contacto", methods=["GET", "POST"])
def contacto():
    if request.method == "POST":
        # Capturar datos del formulario si existe en contacto.html
        nombre = request.form.get("nombre")
        email = request.form.get("email")
        asunto = request.form.get("asunto")
        mensaje = request.form.get("mensaje")
        # Procesar los datos (guardar en BD, enviar correo, etc.)
        print("📩 Nuevo mensaje recibido:")
        print(f"Nombre: {nombre}")
        print(f"Correo: {email}")
        print(f"Asunto: {asunto}")
        print(f"Mensaje: {mensaje}")
        # Redirigir después de procesar
        return redirect(url_for("contacto"))
    return render_template("contacto.html")


# Manejo de errores 404
@app.errorhandler(404)
def page_not_found(e):
    return render_template("index.html"), 404


if __name__ == "__main__":
    app.run(debug=True, port=5000)
