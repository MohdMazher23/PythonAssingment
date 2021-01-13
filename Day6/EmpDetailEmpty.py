import csv
with open("emp.csv",'r') as fp:
    data=csv.reader(fp)
    for line in data:
        if line[0]=='' or line[1]=='' or line[2]=='':
            print(line)


#OUTPUT
"""
['', 'Jones', '4500']
['102', 'Smith', '']
['103', '', '6500']

"""