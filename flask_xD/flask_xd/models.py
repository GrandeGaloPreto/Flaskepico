class Tarefa:
    def __init__(self, id_tarefa, descricao, concluido=False):
        self.id_tarefa = id_tarefa
        self.descricao = descricao
        self.concluido = concluido

tarefas = []

def addTarefas(descricao):
    id = len(tarefas) + 1
    nova_tarefa = Tarefa(id, descricao)
    tarefas.append(nova_tarefa)
