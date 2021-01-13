while True:
    print("1.Add")
    print("2.Sub")
    print("3.Mul")
    print("4.Div")
    print("5.exit")
    user_input=int(input("Chose Operation:\n"))
    
    try:
        value1=int(input("Enter The First Value:\n"))
        value2=int(input("Enter The First Value:\n"))
        if user_input==1:
            sum=value1+value2
            print("The sum is: ",sum)
        elif user_input==2:
            if value1<value2:
                value1,value2=value2,value1
                sub=value1-value2
                print("The subraction of two values is:",sub)
        elif user_input==3:
            mul=value1*value2
            print("The Multiplication of two values is:",mul)
        elif user_input==4:
            div=value1/value2
            print("division:",div)
        elif user_input==5:
            print("Bye")
            break
        else:
            print("Enter valid operation")
    
        nx=input("Do you Want To Exit Yes Or No:\n")
        if nx!='no':
            print("bye")
            break
    except (ZeroDivisionError,ValueError) as msg:
        print("Invalid number enter exception is:",msg)
