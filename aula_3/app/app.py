"""
This function handles the root route and returns a greeting message.
"""
import os
from flask import Flask

app = Flask(__name__)

my_env = os.getenv('AMBIENTE')
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
