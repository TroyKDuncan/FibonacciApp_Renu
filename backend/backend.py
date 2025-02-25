from flask import Flask, jsonify, request
from flask_cors import CORS

app = Flask(__name__)
CORS(app)


def fibonacci(n):
    if n <= 0:
        return []
    elif n == 1:
        return [0]
    elif n == 2:
        return [0, 1]
    else:
        fib_sequence = [0, 1]
        for i in range(2, n):
            fib_sequence.append(fib_sequence[-1] + fib_sequence[-2])
        return fib_sequence


@app.route('/fibonacci', methods=['GET'])
def get_fibonacci():
    n = request.args.get('n', type=int)
    if n is None or n < 1:
        return jsonify({"error": "Please provide a positive integer."}), 400
    return jsonify({"sequence": fibonacci(n)})


if __name__ == '__main__':
    app.run(debug=True)
