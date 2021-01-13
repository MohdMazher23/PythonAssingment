import csv
#open a csv file using with operation 
with open ("emp.csv",'r') as fp:

    read=csv.reader(fp)
    data=list(read)
    
    for line in data:
        #checking the salary coloum is empty
        if line[2]=='':
            #if it is empty then printing the row
            print(line)
    

#OUTPUT
"""
python EmpSalaryEmpty.py
['102', 'Smith', '']

"""

"""
CSV FILE
id	name	sal
101	Anna	5500
	Jones	4500
102	Smith	
103		6500
104	Alice	3500

"""