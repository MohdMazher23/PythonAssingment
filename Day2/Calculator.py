while True:
    print("MY CALCULATOR\n ===========\n 1.ADD\n 2.SUB\n 3.MUL\n 4.DIV\n 5.EXIT")
    user_input=int(input("CHOSE OPERATION "))

    if user_input==5:
        break
    
    first_value=int(input("Enter First Value: "))
    second_value=int(input("Enter Second Value: "))
    if user_input == 1:
        sum=first_value+second_value
        print("The sum of",first_value,"and",second_value,"is: ",sum)

    elif user_input == 2:
        if first_value<second_value:
            second_value,first_value=first_value,second_value
        sub=first_value-second_value
        print("The substraction of",first_value,"and",second_value,"is: ",sub)

    elif user_input == 3:
        mul=first_value*second_value
        print("The multiplication of",first_value,"and",second_value,"is: ",mul)

    elif user_input == 4:
        div=first_value/second_value
        print("The division of",first_value,"and",second_value,"is: ",round(div,4))

    else:
        print("INVALID SELECTION")
        break
    c_inptt=int(input("DO YOU WANT TO CONTINUE 1 FOR YES 0 FOR NO= "))
    if c_inptt!=1:
        break

#OUTPUT

"""
MY CALCULATOR
 ===========
 1.ADD
 2.SUB
 3.MUL
 4.DIV
 5.EXIT
CHOSE OPERATION 1
Enter First Value: 10
Enter Second Value: 20
The sum of 10 and 20 is:  30
DO YOU WANT TO CONTINUE 1 FOR YES 0 FOR NO= 1
MY CALCULATOR
 ===========
 1.ADD
 2.SUB
 3.MUL
 4.DIV
 5.EXIT
CHOSE OPERATION 2
Enter First Value: 40
Enter Second Value: 10
The substraction of 40 and 10 is:  30
DO YOU WANT TO CONTINUE 1 FOR YES 0 FOR NO= 1
MY CALCULATOR
 ===========
 1.ADD
 2.SUB
 3.MUL
 4.DIV
 5.EXIT
CHOSE OPERATION 4
Enter First Value: 1667
Enter Second Value: 78
The division of 1667 and 78 is:  21.3718
DO YOU WANT TO CONTINUE 1 FOR YES 0 FOR NO= 0

"""