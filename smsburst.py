from flask import Flask, render_template, request
import requests as req
import time
app = Flask(__name__)

@app.route('/')
def index():

    return render_template('index.html')

@app.route('/response', methods=['POST'])
def resultado():

    cel = request.form['celular']
    texto = request.form['mensaje']


    resp = req.post('https://textbelt.com/text', {
        'phone': '{}'.format(cel),
        'message': '{}'.format(texto),
        'key': 'textbelt',
        })

    resp_end = resp.json()
    fecha = time.strftime('%d/%m/%Y')
    hora = time.strftime('%I:%M:%S %p')

    return render_template('resultado.html',
            cel = cel,
            mensaje = texto,
            respuesta = resp_end['success'],
            fecha = fecha,
            hora = hora,
            )

if __name__ == '__main__':
    app.run(debug=True)
