from flask import *
import requests

app = Flask(__name__)

@app.route("/")
def index():
  return render_template('index.html', num1 = 0)

@app.route("/suma", methods=['POST'])
def suma():
	num1 = request.form['num1']
	num2 = request.form['num2']
	resultado = requests.get('http://localhost:5001/suma/'+num1+'/'+num2)
	return render_template('index.html', num1 = int(str(resultado.text)[1:-2])) 

@app.route("/resta", methods=['POST'])
def resta():
	num1 = request.form['num1']
	num2 = request.form['num2']
	resultado = requests.get('http://localhost:5002/resta/'+num1+'/'+num2)
	return render_template('index.html', num1 = int(str(resultado.text)[1:-2])) 

@app.route("/mult", methods=['POST'])
def mult():
	num1 = request.form['num1']
	num2 = request.form['num2']
	resultado = requests.get('http://serv_mult:5003/multiplicacion/'+num1+'/'+num2)
	return render_template('index.html', num1 = int(str(resultado.text)[1:-2])) 

@app.route("/div", methods=['POST'])
def div():
	num1 = request.form['num1']
	num2 = request.form['num2']
	resultado = requests.get('http://localhost:5004/division/'+num1+'/'+num2)
	return render_template('index.html', num1 = int(str(resultado.text)[1:-2])) 

if __name__ == "__main__":  
  app.run(host="0.0.0.0", port=5000)