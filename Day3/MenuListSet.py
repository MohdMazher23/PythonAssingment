Task=[]
while True:
    print("""My To DO App
    ===============
    1.Add Task
    2.View Task
    3.Exit""")
    user_input=int(input("\n Chose operation: "))

    if user_input==1:
        input_task=input("ENTER TASK NAME: ")
        Task.append(input_task.capitalize())
        print("TASK ADDED SUCCESSFULLY")
    elif user_input==2:
        count=1
        print("YOUR TASK")
        for i in Task:
            print(count,".",i,"\n")
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
    
    #output
"""
My To DO App
    ===============
    1.Add Task
    2.View Task
    3.Exit

 Chose operation: 1
ENTER TASK NAME: have to clean aquarium before 6:00 pm
TASK ADDED SUCCESSFULLY
Do you Want to Add More Task  Yes or No yes
My To DO App
    ===============
    1.Add Task
    2.View Task
    3.Exit

 Chose operation: 2
YOUR TASK
1 . Go for shopping at 11:00 am

2 . Have to give bike to mechanic at 2:00 pm

3 . Have to clean aquarium before 6:00 pm

Do you Want to Add More Task  Yes or No no
bye
"""
            


