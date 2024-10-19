from flask import Flask, render_template, request, redirect, url_for, flash
from blockchain_script import write_block, block_check
from student_list import add_student, get_all_students

app = Flask(__name__)
app.secret_key = 'your_secret_key_here'  # Replace with a real secret key

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        student = request.form['student']
        lesson = request.form['lesson']
        mark = request.form['mark']
        date = request.form['date']
        
        add_student(student)
        result = write_block(student, lesson, mark, date)
        flash(result, 'success')
        return redirect(url_for('index'))
    
    return render_template('index.html')

@app.route('/check', methods=['GET'])
def check_integrity():
    students = get_all_students()
    results = {}
    for student in students:
        results[student] = block_check(student)
    return render_template('check.html', results=results)

if __name__ == '__main__':
    app.run(debug=True)