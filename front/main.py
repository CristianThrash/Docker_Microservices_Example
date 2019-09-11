from flask import *
import requests

app = Flask(__name__)

@app.route("/")
def index():
  return render_template('index.html', num1 = 0)

@app.route("/operacion", methods=['POST'])
def operacion():
	num1 = request.form['num1']
	num2 = request.form['num2']
	op = request.form['operacion']
	if(op=='+'):
		resultado = requests.get('http://serv_suma:5001/suma/'+num1+'/'+num2)
	elif(op=='-'):
		resultado = requests.get('http://serv_resta:5002/resta/'+num1+'/'+num2)
	elif(op=='*'):
		resultado = requests.get('http://serv_mult:5003/multiplicacion/'+num1+'/'+num2)
	elif(op=='/'):
		resultado = requests.get('http://serv_div:5004/division/'+num1+'/'+num2)

	return render_template('index.html', num1 = int(str(resultado.text)[1:-2])) 

if __name__ == "__main__":  
  app.run(host="0.0.0.0", port=5000)
