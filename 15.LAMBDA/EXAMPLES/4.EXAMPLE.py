# Use lambda with map() to increase each salary by 10%.
salary = [20000, 30000, 40000]
new_salary = list(map(lambda x : x*1.1 , salary))
for a,b in zip(salary,new_salary):
    print(f'Old salary : {a} , New Salary : {b}')
    