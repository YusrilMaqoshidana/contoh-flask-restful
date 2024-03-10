# import library
from flask import Flask, request
from flask_restful import Resource, Api
from flask_cors import CORS

# Inisiasi object flask
app = Flask(__name__)

# Inisiasi object flask_restful
api = Api(app)

# Inisiasi object flask_cors
CORS(app)

class TypeResource(Resource):
    def get(self):
        response = {'name': 'Moh. Yusril Maqoshidana',
                    'email': '222410102064@mail.unej.ac.id'}
        return response

# Setup resource
api.add_resource(TypeResource, "/", methods=["GET"])

if __name__ == "__main__":
    app.run(debug=True, port=5000)
