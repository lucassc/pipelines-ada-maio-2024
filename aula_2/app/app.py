from flask import Flask
import os

app = Flask(__name__)

my_env = os.getenv('AMBIENTE')
print(f'AMBIENTE={my_env}')

@app.route('/')
def home():
    return 'Hello, Docker!'

@app.route('/AMBIENTE')
def env():
    return f'AMBIENTE={my_env}'

@app.route('/STARTED')
def started():
    ## valido as dependências antes de iniciar o container
    return 'STARTED'

@app.route('/READY')
def ready():
    return health()

@app.route('/HEALTH')
def health():
    return 'OK'

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)