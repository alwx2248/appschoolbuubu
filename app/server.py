from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

students = []

@app.route('/')
def index():
    return render_template('base.html')

@app.route('/add', methods=['GET', 'POST'])
def add_student():
    error = None
    name = ''
    surname = ''
    avg_grade = ''
    subjects = ''
    if request.method == 'POST':
        name = request.form.get('name', '')
        surname = request.form.get('surname', '')
        avg_grade_str = request.form.get('avg_grade', '')
        subjects_str = request.form.get('subjects', '')

        
        if not name[0].isupper() or not name.isalpha():
            error = 'Имя должно начинаться с заглавной буквы и содержать только буквы.'
        elif not surname[0].isupper() or not surname.isalpha():
            error = 'Фамилия должна начинаться с заглавной буквы и содержать только буквы.'
        else:
            
            try:
                avg_grade = float(avg_grade_str)
                subjects = int(subjects_str)
            except ValueError:
                error = 'Проверьте правильность введенных чисел и среднего балла.'

        if error:
            
            return render_template('add_student.html', error=error, name=name, surname=surname, avg_grade=avg_grade_str, subjects=subjects_str)
        else:
            students.append({
                'name': name,
                'surname': surname,
                'avg_grade': avg_grade,
                'subjects': subjects
            })
            return redirect(url_for('show_students'))

    
    return render_template('add_student.html', error=error, name=name, surname=surname, avg_grade=avg_grade, subjects=subjects)

@app.route('/students')
def show_students():
    return render_template('student_list.html', students=students)

@app.route('/delete/<int:index>', methods=['POST'])
def delete_student(index):
    if 0 <= index < len(students):
        students.pop(index)
    return redirect(url_for('show_students'))

if __name__ == '__main__':
    print("🚀 Сервер запущен! Открой http://127.0.0.1:5000")
    app.run(debug=True)