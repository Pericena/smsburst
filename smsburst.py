import os, re
import webbrowser as web
import subprocess as subp
import platform
from time import sleep

if platform.python_version() >= '3':
    pass
else:
    print('Soporta con python3 :)')
    exit()

if os.path.exists('/usr/'):
    print('Ejecutando en Linux...')
    sleep(1.5)
    def conexion_flask():
        tam_archivo = os.path.getsize('logs.log')
        if tam_archivo > 0:
            os.system('rm logs.log')
        else:
            pass
        print('Iniciando Servidor Flask...')
        sleep(5)
        url_flask = open('logs.log','w')
        subproceso = subp.Popen(['python3', 'main.py'], stderr=url_flask, stdout=url_flask)
        url_flask.close()

        print("Obteniendo enlaces...")
        sleep(3)
        url = open('logs.log','r')
        for linea in url:
            linea = linea.rstrip()
            if re.search('http:', linea):
                linea = linea.split(' ')
                url_flask = linea[4]
                print('Enlace Flask: '+url_flask)
        url.close()
        web.open(url_flask)
        input('Enter para cancelar el servidor...\n')
        subproceso.terminate()
    conexion_flask()

elif os.path.exists(r'C:\Users'):
    print('Ejecutando en Windows...')
    sleep(1.5)
    def conexion_flask():
        tam_archivo = os.path.getsize('logs.log')
        if tam_archivo > 0:
            os.system('rm logs.log')
        else:
            pass
        print('Iniciando Servidor Flask...')
        sleep(5)
        url_flask = open('logs.log','w')
        subproceso = subp.Popen(['python3', 'main.py'], stderr=url_flask, stdout=url_flask)
        url_flask.close()

        print("Obteniendo enlaces...")
        sleep(3)
        url = open('logs.log','r')
        for linea in url:
            linea = linea.rstrip()
            if re.search('http:', linea):
                linea = linea.split(' ')
                url_flask = linea[4]
                print('Enlace Flask: '+url_flask)
        url.close()
        web.open(url_flask)
        input('Enter para cancelar el servidor...\n')
        subproceso.terminate()
    conexion_flask()
elif os.path.exists('/data/data/com.termux/files/home'):
    print('Ejecutando en Termux...')
    sleep(1.5)
    def conexion_flask():
        tam_archivo = os.path.getsize('logs.log')
        if tam_archivo > 0:
            os.system('rm logs.log')
        else:
            pass
        print('Iniciando Servidor Flask...')
        sleep(5)
        url_flask = open('logs.log','w')
        subproceso = subp.Popen(['python3', 'main.py'], stderr=url_flask, stdout=url_flask)
        url_flask.close()

        print("Obteniendo enlace...")
        sleep(3)
        url = open('logs.log','r')
        for linea in url:
            linea = linea.rstrip()
            if re.search('http:', linea):
                linea = linea.split(' ')
                url_flask = linea[4]
                print('Enlace Flask: '+url_flask)
        url.close()
        os.system('termux-open '+url_flask)        
        input('Enter para cancelar el servidor...\n')
        subproceso.terminate()
    conexion_flask()