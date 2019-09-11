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
	resultado = requests.get('http://gateway:5005/gateway/'+num1+'/'+num2+'/'+op)
	return render_template('index.html', num1 = int(str(resultado.text)[3:-6]))

if __name__ == "__main__":  
  app.run(host="0.0.0.0", port=5000)
