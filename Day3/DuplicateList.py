list_value=[10,20,30,40,50,60,10,20,30,40,50]
list1=[]

print("LIST BEFORE ELIEMINATION\n",list_value)
for i in list_value:
    if i not in list1:
        list1.append(i)
print("list after elimination dublicate\n",list1)


#OUTPUT
"""
LIST BEFORE ELIEMINATION
 [10, 20, 30, 40, 50, 60, 10, 20, 30, 40, 50]
list after elimination dublicate
 [10, 20, 30, 40, 50, 60]

"""









