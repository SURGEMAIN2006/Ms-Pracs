
from flask import Flask, request, jsonify

app = Flask(__name__)
todos = []
next_id = 1

@app.route('/')
def home():
    return "Welcome to To-Do API"

@app.route('/todos', methods=['GET', 'POST'])
def manage_todos():
    global next_id

    if request.method == 'POST':
        data = request.get_json()
        if not data or not data.get('task'):
            return jsonify({'error': 'Task required'}), 400

        todo = {
            'id': next_id,
            'task': data['task'],
            'status': data.get('status', 'pending')
        }
        todos.append(todo)
        next_id += 1
        return jsonify(todo), 201

    return jsonify(todos)

@app.route('/todos/<int:id>', methods=['GET', 'PUT', 'DELETE'])
def manage_todo(id):
    global todos
    todo = next((t for t in todos if t['id'] == id), None)

    if not todo:
        return jsonify({'error': 'Not found'}), 404

    if request.method == 'GET':
        return jsonify(todo)

    if request.method == 'PUT':
        data = request.get_json()
        todo.update(data)
        return jsonify(todo)

    todos.remove(todo)
    return jsonify({'message': 'Deleted successfully'})

if __name__ == '__main__':
    app.run(debug=True)
