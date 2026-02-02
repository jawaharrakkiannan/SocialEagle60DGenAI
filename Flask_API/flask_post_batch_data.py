from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route("/calculate", methods=["POST"])
def calculate_batch():
    data = request.get_json()

    if not data or "calculations" not in data:
        return jsonify({"error": "calculations list required"}), 400

    results = []

    for item in data["calculations"]:
        try:
            a = item.get("a")
            b = item.get("b")
            op = item.get("op")

            if a is None or b is None or op is None:
                results.append({"error": "missing fields", "input": item})
                continue

            if op == "add":
                result = a + b
            elif op == "sub":
                result = a - b
            elif op == "mul":
                result = a * b
            elif op == "div":
                if b == 0:
                    results.append({"error": "division by zero", "input": item})
                    continue
                result = a / b
            else:
                results.append({"error": "invalid operation", "input": item})
                continue

            results.append({
                "a": a,
                "b": b,
                "operation": op,
                "result": result
            })

        except Exception:
            results.append({"error": "invalid input types", "input": item})

    return jsonify({
        "count": len(results),
        "results": results
    })

if __name__ == "__main__":
    app.run(debug=True)



'''
inside Postman, set the request type to POST and the URL to:
http://localhost:5000/calculate

{
  "calculations": [
    { "a": 10, "b": 5, "op": "add" },
    { "a": 20, "b": 4, "op": "mul" },
    { "a": 15, "b": 3, "op": "div" }
  ]
}



'''