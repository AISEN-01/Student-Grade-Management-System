def add_student():
    while True:
        try:
            user_input = int(input('Enter your ID: '))
            pass
            #if user_ID in student:
                #return False, 'already taken'
        except(ValueError):
            return False, 'invalid input'
        
        try:
            user_input = input('Enter your name: ')
            if not user_input.strip():
                return False, 'no input'
        except(ValueError):
            return False, 'invalid input'
    