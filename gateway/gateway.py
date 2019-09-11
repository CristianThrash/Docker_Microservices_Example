from flask import Flask
from flask_restful import Resource, Api
import requests
app = Flask(__name__)
api = Api(app)

class Gate(Resource):
	def get(self, num1, num2, op):
		if(op=='+'):
			resultado = requests.get('http://serv_suma:5001/suma/'+num1+'/'+num2)
		elif(op=='-'):
			resultado = requests.get('http://serv_resta:5002/resta/'+num1+'/'+num2)
		elif(op=='*'):
			resultado = requests.get('http://serv_mult:5003/multiplicacion/'+num1+'/'+num2)
		elif(op=='%'):
			resultado = requests.get('http://serv_div:5004/division/'+num1+'/'+num2)
		return resultado.text

api.add_resource(Gate, '/gateway/<num1>/<num2>/<op>')
if __name__ == "__main__":  
  app.run(host="0.0.0.0", port=5005)

