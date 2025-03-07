from flask import Flask, request, jsonify, render_template

app = Flask(__name__)

# In-memory task list (no database yet)
tasks = []

@app.route('/hello/')
@app.route('/hello/<name>')
def hello(name=None):
    return render_template('hello.html', person=name)

# # Route: Get all tasks
# @app.route("/tasks", methods=["GET"])
# def get_tasks():
#     return jsonify(tasks)
#
# # Route: Add a task
# @app.route("/tasks", methods=["POST"])
# def add_task():
#     data = request.json
#     task = {"id": len(tasks) + 1, "name": data.get("name")}
#     tasks.append(task)
#     return jsonify(task), 201  # HTTP 201: Created
#
# # Route: Delete a task
# @app.route("/tasks/<int:task_id>", methods=["DELETE"])
# def delete_task(task_id):
#     global tasks
#     tasks = [task for task in tasks if task["id"] != task_id]
#     return jsonify({"message": "Task deleted!"})

if __name__ == "__main__":
    app.run(debug=True)