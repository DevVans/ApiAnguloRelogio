from flask import Flask
from controller import getClockAngle, getQueries

app = Flask(__name__)

@app.route('/')
def index():
	return "Use http://[::]:[port]/rest/relogio/[hour]/[minute] para obter o angulo <br> porta 8080 <br> Use http://[::]:[port]/queries para ver todas as consultas"

@app.route('/rest/<string:petition>/<int:hour>/')
@app.route('/rest/<string:petition>/<int:hour>/<int:minute>')
def rest(petition, hour,minute=0):
	print(petition)
	if petition == 'relogio':
		print(f'hora:{hour}, minuto:{minute}')
		return getClockAngle(hour,minute)

@app.route('/queries')
def queries():
	return getQueries()

if __name__=='__main__':
	app.run(host='0.0.0.0',debug=True)