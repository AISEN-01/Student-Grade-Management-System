import os
import json

def add_student():
# define the file path
    file = os.path.join(os.path.dirname(__file__), 'Studentdb.json')

#load existing data first
    try:
        with open(file, 'r') as fstudent:
            data = json.load(fstudent)
    except(FileNotFoundError, json.JSONDecodeError, PermissionError, OSError):
        data = []
#input and validation
    try:
        user_ID = int(input('Enter your ID: '))
        if any(s['ID'] == user_ID for s in data):
            return False, 'The ID is already taken  '

        user_name = input('Enter your name: ').strip()
        if not user_name:
            return False, 'no input'
    except(ValueError):
        return False, 'invalid input'
    
  #create record  
    Students = {'ID': user_ID, 'Name': user_name, 'Grade': []}
    data.append(Students)

#save back the file 
    try:
        with open(file, 'w') as fstudent:
            json.dump(data, fstudent, indent=4)
        return True, Students
    except OSError as e:
        return False, f"File error: {e}"
    