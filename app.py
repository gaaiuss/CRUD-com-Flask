from flask import Flask

app = Flask(__name__)
tasks = []

@app.route('/')
def home():
    return {"message": "Bem-vindo à API To-Do List!"}

@app.route('/tasks', methods=['GET'])
def get_tasks():
    return {"tasks": tasks}, 200

@app.route('/tasks', methods=['POST'])
def create_task():
    # Implemente lógica para adicionar uma tarefa
    pass

if __name__ == '__main__':
    app.run(debug=True)
