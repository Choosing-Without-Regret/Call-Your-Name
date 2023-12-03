from flask import Flask, render_template, request, redirect, url_for
import sqlite3

app = Flask(__name__)


def create_table():
    conn = sqlite3.connect('todo.db')
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS todos
                 (id INTEGER PRIMARY KEY AUTOINCREMENT, task TEXT, completed BOOLEAN)''')
    
   
    conn.commit()
    conn.close()

create_table()


@app.route('/')
def index():
    conn = sqlite3.connect('todo.db')
    c = conn.cursor()
    c.execute("SELECT * FROM todos")
    todos = c.fetchall()
    conn.close()
    return render_template('index.html', todos=todos)


@app.route('/add', methods=['POST'])
def add():
    task = request.form['task']
    conn = sqlite3.connect('todo.db')
    c = conn.cursor()
    c.execute("INSERT INTO todos (task, completed) VALUES (?, ?)", (task, False))
    conn.commit()
    conn.close()
    return redirect(url_for('index'))

@app.route('/delete/<int:task_id>', methods=['POST'])
def delete(task_id):
    conn = sqlite3.connect('todo.db')
    c = conn.cursor()
    c.execute("DELETE FROM todos WHERE id=?", (task_id,))
    conn.commit()
    conn.close()
    return redirect(url_for('index'))



@app.route('/edit/<int:task_id>', methods=['GET'])
def edit(task_id):
    conn = sqlite3.connect('todo.db')
    c = conn.cursor()
    c.execute("SELECT * FROM todos WHERE id=?", (task_id,))
    todo = c.fetchone()
    conn.close()
    return render_template('edit.html', todo=todo)

@app.route('/update/<int:task_id>', methods=['POST'])
def update(task_id):
    edited_task = request.form['edited_task']
    conn = sqlite3.connect('todo.db')
    c = conn.cursor()
    c.execute("UPDATE todos SET task=? WHERE id=?", (edited_task, task_id))
    conn.commit()
    conn.close()
    return redirect(url_for('index'))
    

if __name__ == '__main__':
    app.run(debug=True)