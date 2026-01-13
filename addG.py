import os
import json

def add_grades():
    file_path = os.path.join(os.path.dirname(__file__), 'Studentdb.json')

    try:
        with open(file_path, 'r') as f:
            students = json.load(f)
    except (FileNotFoundError, json.JSONDecodeError):
        students = []

    if not students:
        return False, "there is no student yet"

    try:
        user_id = int(input('Enter student ID to add grades for: '))
    except ValueError:
        return False, 'invalid ID'

    student = next((s for s in students if s.get('ID') == user_id), None)
    if not student:
        return False, 'student not found'

    if 'Grade' not in student or not isinstance(student['Grade'], list):
        student['Grade'] = []

    try:
        num_grades = int(input(f"enter how many grades you want to add for {student.get('Name','')}: "))
    except ValueError:
        return False, 'invalid number'

    for i in range(num_grades):
        while True:
            try:
                new_grade = float(input(f'enter the grade {i + 1}: '))
                if 0 <= new_grade <= 100:
                    student['Grade'].append(new_grade)
                    break
                else:
                    print('  Invalid: Grade must be between 0 and 100.')
            except ValueError:
                print('  Invalid: Please enter a numeric value.')

    try:
        with open(file_path, 'w') as f:
            json.dump(students, f, indent=4)
    except OSError as e:
        return False, f"File error: {e}"

    return True, student