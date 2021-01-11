while True:
    student_name=input("Enter The Name Of Student: ")
    student_roll_no=input("Enter The Roll No of Student: ")
    subjects=[]
    count=0
    print("ENTER MARKS BTW 1-100 ONLY ")
    for i in range(1,7):
        
        print(i ,"Subject Marks")
    
        sub=int(input("Enter the subject Marks: "))

        
        if sub<40:
            subjects.append(sub)
            count+=1
            
            
        
        else:
            subjects.append(sub)


    print("\n\n")
    print("NAME =",student_name.upper())
    print("Roll No =",student_roll_no)
    Total_marks=0
    for i in subjects:
        Total_marks+=i

    print("The total Marks of a student is:=",Total_marks)
    print("STUDENT",student_name," HAS FAILED IN ",count,"SUBJECTS")
    no_sub=len(subjects)
    average=round(Total_marks/no_sub,2)
    
    print("Average         GRADE")

    
    if average>80 and average<101:
        print(average,"            ","A")
    elif average>60 and average<80:
        print(average,"             ","B")
    elif average>50 and average<59:
        print(average,"             ","C")
    elif average>40 and average<49:
        print(average,"             ","D")
    elif average<40:
        print(average,"           ","PROMOTED")
    u_input=input("TYPE YES TO ADD ANOTHER STUDENT MARKS NO TO EXIT ")
    if u_input!='yes':
        break





#output
"""
NAME = MAZHER
Roll No = 90908
The total Marks of a student is:= 430
STUDENT MAZHER  HAS FAILED IN  0 SUBJECTS
Average         GRADE
71.67               B
TYPE YES TO ADD ANOTHER STUDENT MARKS NO TO EXIT yes
Enter The Name Of Student: xyz
Enter The Roll No of Student: 1234
ENTER MARKS BTW 1-100 ONLY
1 Subject Marks
Enter the subject Marks: 60
2 Subject Marks
Enter the subject Marks: 40
3 Subject Marks
Enter the subject Marks: 30
4 Subject Marks
Enter the subject Marks: 30
5 Subject Marks
Enter the subject Marks: 50
6 Subject Marks
Enter the subject Marks: 60



NAME = XYZ
Roll No = 1234
The total Marks of a student is:= 270
STUDENT xyz  HAS FAILED IN  2 SUBJECTS
Average         GRADE
45.0               D
TYPE YES TO ADD ANOTHER STUDENT MARKS NO TO EXIT yes
Enter The Name Of Student: jhon
Enter The Roll No of Student: 3456
ENTER MARKS BTW 1-100 ONLY
1 Subject Marks
Enter the subject Marks: 50
2 Subject Marks
Enter the subject Marks: 30
3 Subject Marks
Enter the subject Marks: 30
4 Subject Marks
Enter the subject Marks: 30
5 Subject Marks
Enter the subject Marks: 40
6 Subject Marks
Enter the subject Marks: 40



NAME = JHON
Roll No = 3456
The total Marks of a student is:= 220
STUDENT jhon  HAS FAILED IN  3 SUBJECTS
Average         GRADE
36.67             PROMOTED
TYPE YES TO ADD ANOTHER STUDENT MARKS NO TO EXIT no
"""


    