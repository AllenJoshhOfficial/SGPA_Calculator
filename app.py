from flask import Flask, render_template, request

app = Flask(__name__)

# Define grade options and subjects globally
grade_options = ['O', 'A+', 'A', 'B+', 'B', 'C', 'U']
subjects = ['Probablity & Statistics for Data Science - II',
             'Data Structure and Algorithmn - II',
               'Computer Architecture',
                 'Advanced Python Programming',
                   'Operating Systems', 
                   'Digital Logic Design', 
                   'Data Structure and Algorithmn - II Laboratory']

def default_grade(grade):
    grades = {'O': 10, 'A+': 9, 'A': 8, 'B+': 7, 'B': 6, 'C': 5, 'U': 0}
    return grades.get(grade, None)

@app.route('/')
def index():
    return render_template('index.html', subjects=subjects, grade_options=grade_options)

@app.route('/calculate_sgpa', methods=['POST'])
def calculate_sgpa():
    try:
        grades = {subject: request.form[subject] for subject in subjects}
        grades = {subject: default_grade(grade.upper()) for subject, grade in grades.items()}

        gpa = sum([4 * grades['Probablity & Statistics for Data Science - II'], 3 * grades['Data Structure and Algorithmn - II'], 3 * grades['Computer Architecture'], 3 * grades['Advanced Python Programming'], 4 * grades['Digital Logic Design'], 4 * grades['Operating Systems'], 1 * grades['Data Structure and Algorithmn - II Laboratory']])
        sgpa = gpa / 22
        rounded_sgpa = round(sgpa, 3)

        confetti_effect = sgpa > 6  # Set to True if SGPA is greater than 6

        return render_template('result.html', sgpa=rounded_sgpa, confetti_effect=confetti_effect)

    except Exception as e:
        return render_template('error.html', error=str(e))

if __name__ == '__main__':
    app.run(debug=False,host='0.0.0.0')

