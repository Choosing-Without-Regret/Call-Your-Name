from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        ideal_self = request.form['ideal_self']
        return render_template('goal_form.html', ideal_self=ideal_self)
    return render_template('index.html')

@app.route('/process_goal', methods=['POST'])
def process_goal():
    if request.method == 'POST':
        goal = request.form['goal']
        ideal_self = request.form['ideal_self']
        return render_template('subgoal_form.html', goal=goal, ideal_self=ideal_self)
    return render_template('index.html')

@app.route('/process_subgoal', methods=['POST'])
def process_subgoal():
    if request.method == 'POST':
        subgoal = request.form['subgoal']
        goal = request.form['goal']
        ideal_self = request.form['ideal_self']
        return render_template('near_goal_form.html', goal=goal, subgoal=subgoal, ideal_self=ideal_self)
    return render_template('index.html')

@app.route('/process_near_goal', methods=['POST'])
def process_near_goal():
    if request.method == 'POST':
        near_goal = request.form['near_goal']
        goal = request.form['goal']
        subgoal = request.form['subgoal']
        ideal_self = request.form['ideal_self']
        return render_template('result2.html', goal=goal, subgoal=subgoal, near_goal=near_goal, ideal_self=ideal_self)
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
