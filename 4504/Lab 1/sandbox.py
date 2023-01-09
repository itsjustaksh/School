j = 0
grade = 73
num_stu = 7

num = 0
while(grade > 0):
    if grade % 3:
        grade -= 1;
    
    else:
        grade -=4
        num += grade

print(True) if num < 300 else print(False)