from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route("/calculate", methods=["POST"])
def calculate():
    data = request.get_json()

    if not data:
        return jsonify({"error": "JSON body required"}), 400

    a = data.get("a")
    b = data.get("b")
    op = data.get("op")

    if a is None or b is None or op is None:
        return jsonify({"error": "Missing a, b, or op"}), 400

    try:
        if op == "add":
            result = a + b
        elif op == "sub":
            result = a - b
        elif op == "mul":
            result = a * b
        elif op == "div":
            if b == 0:
                return jsonify({"error": "Division by zero"}), 400
            result = a / b
        else:
            return jsonify({"error": "Invalid operation"}), 400

        return jsonify({
            "a": a,
            "b": b,
            "operation": op,
            "result": result
        })

    except Exception:
        return jsonify({"error": "Invalid input types"}), 400

if __name__ == "__main__":
    app.run(debug=True)


'''
inside Postman, set the request type to POST and the URL to:
http://localhost:5000/calculate

{
  "a": 10,
  "b": 5,
  "op": "mul"
}


'''