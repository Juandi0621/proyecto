from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)


# Página de inicio
@app.route("/")
def index():
    return render_template("index.html")


# Página "Quiénes somos"
@app.route("/somos")
def quienes_somos():
    return render_template("somos.html")


# Página "Contenido"
@app.route("/contenido")
def contenido():
    return render_template("contenido.html")


# Página de contacto con formulario
@app.route("/contacto", methods=["GET", "POST"])
def contacto():
    if request.method == "POST":
        nombre = request.form.get("nombre")
        email = request.form.get("email")
        asunto = request.form.get("asunto")
        mensaje = request.form.get("mensaje")

        # Aquí puedes guardar en BD, enviar correo, etc.
        print("📩 Nuevo mensaje recibido:")
        print(f"Nombre: {nombre}")
        print(f"Correo: {email}")
        print(f"Asunto: {asunto}")
        print(f"Mensaje: {mensaje}")

        # Redirige al contacto después de enviar el formulario
        return redirect(url_for("contacto"))

    return render_template("contacto.html")


if __name__ == "__main__":
    app.run(debug=True)
