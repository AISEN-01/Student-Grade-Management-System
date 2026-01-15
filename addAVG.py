import os
import json
from calc_grades import calcu_grades

def user_Compute():
    user_ID = int(input("enter your ID: "))

    file_path = os.path.join(os.path.dirname(__file__), 'Studentdb.json')

    try:
        with open(file_path, 'r') as f:
            students = json.load(f)
    except(json.JSONDecodeError, FileNotFoundError):
        students = []

    student = next((s for s in students if s['ID'] == user_ID), None)

    if not student:
        return False, "Stop: Student not found."
    
    if not student['Grade']:
        return False, "Inform: This student has no grades yet."
    
    result = calcu_grades(student["Grade"])

    return True, result