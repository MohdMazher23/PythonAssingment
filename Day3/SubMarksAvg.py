list_marks=[]
total_marks=0
count=1
for i in range(1,7):

    print("ENTER ",i,"SUBJECT MARKS ")
    marks=int(input())
    list_marks.append(marks)
for j in list_marks:
    print(count,"SUBJECT MARK= ",j)
    total_marks+=j
    count+=1

print("THE TOTAL MARKS IS= ",total_marks)
average=total_marks/len(list_marks)
print("AVERAGE= ",round(average,2))

#OUTPUT
"""
ENTER  1 SUBJECT MARKS
70
ENTER  2 SUBJECT MARKS
80
ENTER  3 SUBJECT MARKS
90
ENTER  4 SUBJECT MARKS
8
ENTER  5 SUBJECT MARKS
70
ENTER  6 SUBJECT MARKS
68
1 SUBJECT MARK=  70
2 SUBJECT MARK=  80
3 SUBJECT MARK=  90
4 SUBJECT MARK=  8
5 SUBJECT MARK=  70
6 SUBJECT MARK=  68
THE TOTAL MARKS IS=  386
AVERAGE=  64.33
"""

