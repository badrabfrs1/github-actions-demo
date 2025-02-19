import os
from flask import Flask, render_template

app = Flask(__name__, template_folder="templates")  # Assure-toi que Flask sait où chercher les templates

@app.route("/")
def home():
    return render_template("index.html")

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))  # Récupère le port de Railway
    app.run(host="0.0.0.0", port=port)
