class LimitExceedExp(Exception):
    def __init__(self,arg):
        self.arg=arg
class InvalidMinExp(Exception):
    def __init__(self,arg):
        self.arg=arg
class InsuficentFundExp(Exception):
    def __init__(self,arg):
        self.arg=arg
amount=10000
while True:
    print("1.WITHDRAWL")
    print("2.DEPOSIT")
    print("3.Exit()")
    n=int(input("Chose Operation:"))
    
    if n==1:
        withdraw_amount=int(input("Enter amount "))
        if withdraw_amount>amount:
            raise InsuficentFundExp("Insufficient Balance in your account")
        
        elif withdraw_amount<100:
            raise InvalidMinExp("Amount To Less TO withdraw")
        else:
            amount-=withdraw_amount
    elif n==2:
        deposit_amount=int(input("Enter The Amount To Deposit "))
        if deposit_amount>10000:
            raise LimitExceedExp("The Deposit Limit is Reached")
        else:
            amount+=deposit_amount
    elif n==3:
        print("BYE")
        break
    nxp=input("Do You Want To Continue Yes or No: " )
    if nxp!='yes':
        print("Bye")
        break

#OUtput
"""

python AtmExp.py
1.WITHDRAWL
2.DEPOSIT
3.Exit()
Chose Operation:1
Enter amount 5000
Do You Want To Continue Yes or No: yes
1.WITHDRAWL
2.DEPOSIT
3.Exit()
Chose Operation:1
Enter amount 6000
Traceback (most recent call last):
  File "AtmExp.py", line 20, in <module>
    raise InsuficentFundExp("Insufficient Balance in your account")
__main__.InsuficentFundExp: Insufficient Balance in your account

"""
#OUTPUT 2
"""
python AtmExp.py
1.WITHDRAWL
2.DEPOSIT
3.Exit()
Chose Operation:1
Enter amount 99
Traceback (most recent call last):
  File "AtmExp.py", line 23, in <module>
    raise InvalidMinExp("Amount To Less TO withdraw")
__main__.InvalidMinExp: Amount To Less TO withdraw

"""
#OUTPUT 3
"""
1.WITHDRAWL
2.DEPOSIT
3.Exit()
Chose Operation:2
Enter The Amount To Deposit 11000
Traceback (most recent call last):
  File "AtmExp.py", line 29, in <module>
    raise LimitExceedExp("The Deposit Limit is Reached")
__main__.LimitExceedExp: The Deposit Limit is Reached
"""


