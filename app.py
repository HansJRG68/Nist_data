from flask import Flask, request, jsonify
import nistchempy as nist

app = Flask(__name__)

@app.route('/chem')
def chem():
    name = request.args.get('name')

    if not name:
        return jsonify({"error": "No name provided"})

    results = nist.search(name)

    if not results:
        return jsonify({"error": "Not found"})

    c = results[0]

    return jsonify({
        "name": c.name,
        "formula": c.formula,
        "cas": c.cas
    })
