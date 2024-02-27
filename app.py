# app.py
from flask import Flask, jsonify, request
from schema import schema


app = Flask(__name__)

@app.route('/graphql', methods=['POST'])
def graphql():
    data = request.get_json()
    query = data.get('query')
    result = schema.execute(query)
    return jsonify(result.data)

if __name__ == '__main__':
    app.run(debug=True)