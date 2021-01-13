import csv
with open("emp.csv",'r') as fp:
    data=csv.reader(fp)
    for line in data:
        for j in line[1]:
            if j[0]=='A':
                print(line)
                break


#OUTPUT
"""
python EmployeName.py
['101', 'Anna', '5500']
['104', 'Alice', '3500']


"""
