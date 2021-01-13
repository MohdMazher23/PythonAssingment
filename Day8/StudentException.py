class AttandenceShortageEXp(Exception):
    def __init__(self,msg):
        self.msg=msg
class IncomeExp(Exception):
    def __init__(self,args):
        self.msg=args
class GPAExp(Exception):
    def __init__(self,args):
        self.msg=args
print("OUTPUT")
attendance=int(input("ENTER THE ATTENDANCE PERCENTAGE:\n"))
income=int(input("ENTER INCOME:\n"))
GPA=float(input("ENTER YOUR GPA:\n"))
if attendance<75:
    raise AttandenceShortageEXp("Your Attendance Is Less Than Required Attendance")
elif income>500000:
    raise IncomeExp("Your Income Is Higher")
elif GPA<7.0:
    raise GPAExp('your GPA Is Less Than Required')

#OUTPUT1
"""
OUTPUT
ENTER THE ATTENDANCE PERCENTAGE:
70
ENTER INCOME:
50000
ENTER YOUR GPA:
7.5
Traceback (most recent call last):
  File "StudentException.py", line 14, in <module>
    raise AttandenceShortageEXp("Your Attendance Is Less Than Required Attendance")
__main__.AttandenceShortageEXp: Your Attendance Is Less Than Required Attendance

"""
#OUTPUT2
"""
OUTPUT
ENTER THE ATTENDANCE PERCENTAGE:
76
ENTER INCOME:
400000
ENTER YOUR GPA:
6.8
Traceback (most recent call last):
  File "StudentException.py", line 19, in <module>
    raise GPAExp('your GPA Is Less Than Required')
__main__.GPAExp: your GPA Is Less Than Required

"""
#OUTPUT3
"""
OUTPUT
ENTER THE ATTENDANCE PERCENTAGE:
75
ENTER INCOME:
600000
ENTER YOUR GPA:
7.8
Traceback (most recent call last):
  File "StudentException.py", line 17, in <module>
    raise IncomeExp("Your Income Is Higher")
__main__.IncomeExp: Your Income Is Higher

"""

