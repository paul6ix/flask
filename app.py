from flask import Flask, jsonify, request
from flask_restful import Api, Resource

# intailizing flask library
app = Flask(__name__)
# initializing flask restful service and connecting to flask
api = Api(app)


class Add(Resource):
    def post(self):
        data = request.get_json()
        x = int(data['x'])
        y = int(data['y'])
        sum = x + y

        response = {
            "message": sum,
            "StatusCode": 200,

        }
        return jsonify(response)


api.add_resource(Add, '/add')

# @app.route('/ad', methods=['POST'])
# def add():
#     datadict = request.get_json()
#     x = datadict['x']
#     y = datadict['y']
#     z = x + y
#
#     response_data = {
#         "z": z
#     }
#
#     return jsonify(response_data), 200



if __name__ == "__main__":
    app.run()
