# app.py
from flask import Flask, jsonify, request
from schema import schema


def create_app():
    app = Flask(__name__)

    @app.route('/graphql', methods=['POST'])
    def graphql():
        data = request.get_json()
        query = data.get('query')
        result = schema.execute(query)
        if result.errors:
            return jsonify({'errors': [str(error) for error in result.errors]})
        return jsonify({'data': result.data})

    return app