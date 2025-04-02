from flask import Flask, render_template, redirect, url_for, session
from solver import obtener_una_solucion, obtener_soluciones
import time

app = Flask(__name__)
app.secret_key = "reinas2024"  # Necesario para usar session

# Generar todas las soluciones una vez
soluciones, estados_totales = obtener_soluciones()

@app.route("/")
def index():
    # Solución individual simple
    inicio = time.time()
    solucion, estados = obtener_una_solucion()
    fin = time.time()
    tiempo = round(fin - inicio, 6)
    return render_template("tablero.html", solucion=solucion, index=1, total=1, estados=estados)

@app.route("/soluciones")
def ver_solucion():
    if "index" not in session:
        session["index"] = 0

    index = session["index"]
    solucion = soluciones[index]

    return render_template("tablero.html", solucion=solucion, index=index+1, total=len(soluciones), estados=estados_totales)

@app.route("/siguiente")
def siguiente():
    session["index"] = (session.get("index", 0) + 1) % len(soluciones)
    return redirect(url_for("ver_solucion"))

@app.route("/jugar")
def jugar():
    return render_template("jugar.html")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)