
user_input=int(input("ENTER NO TO PRINT EVEN NO UPTO: "))
def even_no(user_input):
    for i in range(1,user_input+1):
        if i%2==0:
            print(i,end=" ")
print("OUTPUT:")
print("EVEN NUMBERS IS:")
even_no(user_input)
#OUTPUT
"""
ENTER NO TO PRINT EVEN NO UPTO: 20
OUTPUT:
EVEN NUMBERS IS:
2 4 6 8 10 12 14 16 18 20
"""
        

