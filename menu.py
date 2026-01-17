from showm import show_menu
from add import add_student
from addG import add_grades
from addAVG import user_Compute
from top import show_top_student
while True:
    show_menu()
    user_input = int(input("What you want to do?"))
    if user_input == 1:
        success, message = add_student()
        print(message)
    elif user_input == 2:
        success, message = add_grades()
        print(message)
    elif user_input == 3:
        success, message = user_Compute()
        print(message)
    elif user_input == 4:
        success, message = show_top_student()
        print(message)
    elif user_input == 5:
        break
    else:
        print('invalid input')


