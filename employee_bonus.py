import csv

EmployeePay = open('EmployeePay.csv', 'r')
Employee_file = csv.reader(EmployeePay, delimiter = ',')

next(Employee_file)

for record in Employee_file:
    base_salary = float(record[3])
    bonus = base_salary * float(record[4])
    total_salary = base_salary + bonus

    print('ID:', record[0])
    print('EmpFName:', record[1])
    print('EmpLName:', record[2])
    print('Base Salary:', base_salary)
    print('Bonus:', bonus)
    print('Total Salary:', total_salary)
    input()

EmployeePay.close()
    
# Customer IDTotal
# 250 5255.24
# 251 26634.88
# 252 625.53
# 253 28735.62
# 254 43095.65
# 255 38747.02
# 256 95202.77
# 257 19802.72
# 258 14795.87
# 259 32874.75
# 260 29710.26
# 261 18098.01


    
   