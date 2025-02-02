from flask import Flask
from controllers import tarefa_controller


app = Flask(__name__)
app.register_blueprint(tarefa_controller)

if __name__ == '__main__':
    app.run(debug=True)
