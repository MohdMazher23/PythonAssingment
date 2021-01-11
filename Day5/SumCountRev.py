def sum_count_reverse(num):
    number=num
    sum,count=0,0
    string_value=str(num)
    list_value=list(string_value)
    for i in list_value:
        sum=sum+int(i)
        count+=1
    #rev_value=list_value[-1::-1]
    reverse=0
    while num>0:
        val=num%10
        reverse=reverse*10+val
        num=num//10
    print("OUTPUT")
    print("GIVEN NUMBER : ",number)
    print("The sum of given number is: ",sum)
    print("The count of given number is ",count)
    print("the reverse of given no is:",reverse)


sum_count_reverse(123)

#OUTPUT
"""
OUTPUT
GIVEN NUMBER :  123
The sum of given number is:  6
The count of given number is  3
the reverse of given no is: 321

"""