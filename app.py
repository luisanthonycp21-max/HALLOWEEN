from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def home():
    nombre_invitado = None
    if request.method == "POST":
        nombre_invitado = request.form.get("nombre")
    
    return render_template("index.html", nombre=nombre_invitado)

if __name__ == "__main__":
    app.run(import os

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5001))
    app.run(host='0.0.0.0', port=port))  # <--- Aquí cambiamos al puerto 5001
