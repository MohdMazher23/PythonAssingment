import csv
list_salary=[]
with open ("emp.csv",'r') as files:

    file=csv.reader(files)
    next(file)
    print("OUTPUT:")
    for line in file:
        salary=str(line[2])
        if salary!="" and int(salary)>3500:
            print(line)    


#OUTPUT
"""
python EmpSalryGreater.py
OUTPUT:
['101', 'Anna', '5500']
['', 'Jones', '4500']
['103', '', '6500']

"""
