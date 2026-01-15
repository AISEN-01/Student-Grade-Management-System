from showm import show_menu
from add import add_student
from addG import add_grades
from addAVG import user_Compute
while True:
    show_menu()
    user_input = int(input("What you want to do?"))
    if user_input == 1:
        add_student()
    elif user_input == 2:
        add_grades()
    elif user_input == 3:
        success, message = user_Compute()
        print(message)
    elif user_input == 4:
        break
    else:
        print('invalid input')


