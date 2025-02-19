import os
from flask import Flask, render_template

# Définir Flask en utilisant 'assets/' comme dossier statique
app = Flask(__name__, static_url_path='/assets', static_folder="assets", template_folder="templates")

@app.route("/")
def home():
    return render_template("index.html")

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)