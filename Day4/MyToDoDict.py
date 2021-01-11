Task_dict={ }
while True:

    print("""My To DO App
    ===============
    1.Add Task
    2.View Task
    3.Exit""")
    user_input=int(input("\n Chose operation: "))

    if user_input==1:
        task_name=input("ENTER TASK NAME: ").title()
        task_date=input("Enter Date: ")
        Task_dict[task_name]=task_date

        print("TASK ADDED SUCCESSFULLY")
    elif user_input==2:
        count=1
        print("   Task NAME                         DATE")

        for i,j in Task_dict.items():
            print(count,".",i,"\t\t\t",j)
            count+=1
    
    elif user_input==3:
        print("   Bye")
        break
    else:
        print("Invalid Selection")
    c_input=input("Do you Want to Add More Task  Yes or No ")
    if c_input!='yes':
        print("bye")
        break


    #OUTPUT
    """
My To DO App
    ===============
    1.Add Task
    2.View Task
    3.Exit

 Chose operation: 1
ENTER TASK NAME: buy fridge
Enter Date: 12/01/2021
TASK ADDED SUCCESSFULLY
Do you Want to Add More Task  Yes or No yes
My To DO App
    ===============
    1.Add Task
    2.View Task
    3.Exit

 Chose operation: 1
ENTER TASK NAME: shopping
Enter Date: 13/01/2021
TASK ADDED SUCCESSFULLY
Do you Want to Add More Task  Yes or No yes
My To DO App
    ===============
    1.Add Task
    2.View Task
    3.Exit

 Chose operation: 1
ENTER TASK NAME: pay emi
Enter Date: 15/01/2021
TASK ADDED SUCCESSFULLY
Do you Want to Add More Task  Yes or No yes
My To DO App
    ===============
    1.Add Task
    2.View Task
    3.Exit

 Chose operation: 2
   Task NAME                         DATE
1 . Buy Fridge                   12/01/2021
2 . Shopping                     13/01/2021
3 . Pay Emi                      15/01/2021
Do you Want to Add More Task  Yes or No no
bye
    """