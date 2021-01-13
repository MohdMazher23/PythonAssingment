while True:
    print("""My TO Do APP
    ========
    1.Add task
    2.View All tasks
    0.exit
    """)
    user_input=int(input("Enter Your Choise:\n "))
    

    if user_input==1:
        with open("ToDoApp.txt",'a') as fp:
            task_name=input("Enter Task Name:\n ")
            nextline=task_name
            fp.write(nextline+"\n")
    elif user_input==2:
        with open("ToDoApp.txt",'r') as fp:
            data=fp.readlines()
            print("Your Task\n ==========")
            for line in data:
                print(line,end=" ")
    user_input_continue=input("DO you want to continue yes or no \n")
    if user_input_continue!='yes':
        print("bye")
        break


    #OUTPUT
    """
    My TO Do APP
    ========
    1.Add task
    2.View All tasks
    0.exit

Enter Your Choise:
 1
Enter Task Name:
 Shopping
DO you want to continue yes or no
yes
My TO Do APP
    ========
    1.Add task
    2.View All tasks
    0.exit

Enter Your Choise:
 1
Enter Task Name:
 Bike Wash
DO you want to continue yes or no
yes
My TO Do APP
    ========
    1.Add task
    2.View All tasks
    0.exit

Enter Your Choise:
 1
Enter Task Name:
 Vist Bank
DO you want to continue yes or no
yes
My TO Do APP
    ========
    1.Add task
    2.View All tasks
    0.exit

Enter Your Choise:
 2
Your Task
 ==========
Shopping
 Bike Wash
 Vist Bank
 DO you want to continue yes or no
no
bye
    """