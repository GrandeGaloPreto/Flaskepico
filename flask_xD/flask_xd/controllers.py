from flask import Blueprint, render_template, request, redirect, url_for
from models import tarefas, addTarefas

tarefa_controller = Blueprint('tarefa', __name__)

@tarefa_controller.route('/')
def index():
    return render_template('index.html', tarefas=tarefas)

@tarefa_controller.route('/add', methods=['POST'])
def add():
    descricao = request.form['descricao']
    addTarefas(descricao)
    return redirect(url_for('tarefa.index'))