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
    


    
   