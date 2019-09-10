from flask import Flask
from flask_restful import Resource, Api

app = Flask(__name__)
api = Api(app)

class Mult(Resource):
    def get(self, num1, num2):
        return str(int(num1)*int(num2))

api.add_resource(Mult, '/multiplicacion/<num1>/<num2>')

if __name__ == "__main__":  
  app.run(host="0.0.0.0", port=5003)