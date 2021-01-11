def factorial(num):
    factorial_value=1
    for i in range(1,num):
        factorial_value+=factorial_value*i

    print("factorail of a given number is",factorial_value)
    

factorial(5)

#output
"""
factorail of a given number is 120
"""