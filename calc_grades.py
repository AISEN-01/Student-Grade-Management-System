def calcu_grades(g_list):
    if not g_list:
        return 0.0
    
    total = sum(g_list)
    count = len(g_list)
    average = total/count

    return average