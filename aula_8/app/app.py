"""
This function handles the root route and returns a greeting message.
"""
import os
from flask import Flask

app = Flask(__name__)

my_env = os.getenv('AMBIENTE')
my_version = os.getenv('VERSAO')
print(f'AMBIENTE={my_env}')

@app.route('/')
def home():
    """
    This function handles the root route and returns a greeting message.
    """
    return 'Hello, Docker!'

@app.route('/AMBIENTE')
def env():
    """ 
    This function returns the environment name.
    """
    return f'AMBIENTE={my_env}'

@app.route('/v2/AMBIENTE')
def env_v2():
    """ 
    This function returns the environment name.
    """
    if my_env != "":
        resultado = f'AMBIENTE={my_env}, VERSAO={my_version}'
    else:
        resultado = f'VERSAO={my_version}'

    return resultado

@app.route('/v3/AMBIENTE')
def env_v3():
    """ 
    This function returns the environment name.
    """
    if my_env != "":
        resultado = f'AMBIENTE={my_env}, VERSAO={my_version}'
    else:
        resultado = f'VERSAO={my_version}'
    return resultado

@app.route('/v4/AMBIENTE')
def env_v4():
    """ 
    This function returns the environment name.
    """
    if my_env != "":
        resultado = f'AMBIENTE={my_env}, VERSAO={my_version}'
    else:
        resultado = f'VERSAO={my_version}'

    return resultado

@app.route('/STARTED')
def started():
    """
    This function handles the '/STARTED' route and returns 
    a message indicating that the dependencies have been validated.
    """
    # Validate dependencies before starting the container
    return 'STARTED'

@app.route('/READY')
def ready():
    """
    This function handles the '/READY' route and returns the result of the 'health' function.
    """
    return health()

@app.route('/HEALTH')
def health():
    """
    This function handles the '/HEALTH' route and returns an 
    'OK' message indicating the health status.
    """
    return 'OK'

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
