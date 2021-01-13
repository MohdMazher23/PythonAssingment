import csv
with open("emp.csv",'r') as fp:
    data=csv.reader(fp)
    for line in data:
        if line[0]!='' and line[1]!="" and line[2]!="":
            print(line)


#OUTPUT

"""
python EmpDetails.py
['id', 'name', 'sal']
['101', 'Anna', '5500']
['104', 'Alice', '3500']


"""