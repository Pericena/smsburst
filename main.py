
import os, platform
import webbrowser as web
import subprocess as subp
from time import sleep


if platform.python_version() >= '3':
    pass
else:
    print('Soporta con python3 :)')
    exit()

if os.path.exists('/usr/'):
    print('Ejecutando en Linux...')
    sleep(1.5)
    print('Iniciando Servidor Flask...')
    sleep(2)
    os.system('python3 smsburst.py')

elif os.path.exists(r'C:\Users'):
    print('Ejecutando en Windows...')
    sleep(1.5)
    print('Iniciando Servidor Flask...')
    sleep(2)
    os.system('python smsburst.py')
    
elif os.path.exists('/data/data/com.termux/files/home'):
    print('Ejecutando en Termux...')
    sleep(1.5)
    print('Iniciando Servidor Flask...')
    sleep(2)
    os.system('python3 smsburst.py')
