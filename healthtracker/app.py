from flask import Flask, request, jsonify

app = Flask(__name__)
todos = []

@app.route('/todos', methods=['POST'])
def add_todo():
    data = request.get_json()
    todo = {
        'id': len(todos) + 1,
        'task': data['task'],
        'status': data.get('status', 'pending')
    }
    todos.append(todo)
    return jsonify(todo)

@app.route('/todos', methods=['GET'])
def get_todos():
    return jsonify(todos)

if __name__ == '__main__':
    app.run(debug=True, port=5000)