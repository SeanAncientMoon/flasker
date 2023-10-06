from flask import Flask
import os

app = Flask(__name__)

@app.route('/list_env_variables')
def list_env_variables():
    env_variables = {key: value for key, value in os.environ.items()}
    return env_variables

if __name__ == '__main__':
    app.run()
