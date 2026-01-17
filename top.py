import os, json
from calc_grades import calcu_grades

def show_top_student():
    file_path = os.path.join(os.path.dirname(__file__), 'Studentdb.json')

    try:
        with open(file_path, 'r') as f:
            students = json.load(f)
    except(json.JSONDecodeError, FileNotFoundError):
            students = []

    if not students:
         return False, "there is no students yet"

    highest = -1
    top_student = "None"

    for student in students:
        if not student['Grade']:
            continue
        
        result = calcu_grades(student["Grade"])

        if result > highest:
            highest = result
            top_student = student["Name"]

    return True, f"the top student is {top_student} with the average of {highest}"