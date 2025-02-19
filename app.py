from flask import Flask, request, jsonify
import os

app = Flask(__name__)

@app.route("/")
def home():
    return "Hello, Railway! 🚀"

@app.route("/add", methods=["GET"])
def add_numbers():
    a = request.args.get("a", type=int)
    b = request.args.get("b", type=int)
    if a is None or b is None:
        return jsonify({"error": "Missing parameters a or b"}), 400
    return jsonify({"result": a + b})

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))  # Utilise Railway PORT
    app.run(host="0.0.0.0", port=port)
