print("====LOGIN APP====")
user_name="mazher123"
password="9898@Hello"
special_char=['!','@','#','$','%','^','&','*','(',')','-','_','+','=','.','/','?']



count=0
for i in range(1,4):
    input_user_name=input("\nENTER USER NAME- ")
    break_count=0
    for i in input_user_name:
        if break_count>0:
            break

        for j in special_char:
            if i==j:
                print("NO SPECIAL CHARACTER ALLOWED IN USER NAME")
                
                break_count+=1
    input_password=input("ENTER YOUR PASSWORD- ")
    if user_name==input_user_name and password==input_password:
        print("\n *LOGIN SUCCESSFUL*")
        break
        
        
    else:
        print("\nWRONG USER NAME OR PASSWORD ENTER")
        
        count+=1
        attempt_left=3-count
        print("ONLY",attempt_left," ATTEMPT LEFT ")
        
    
if count>3:
    exit


#OUTPUT1
"""
====LOGIN APP====
ENTER USER NAME- mazher123
ENTER YOUR PASSWORD- 9898@Hello

 *LOGIN SUCCESSFUL*
"""

#OUTPUT2
"""
====LOGIN APP====

ENTER USER NAME- mazher@123
NO SPECIAL CHARACTER ALLOWED IN USER NAME
ENTER YOUR PASSWORD- mazhe

WRONG USER NAME OR PASSWORD ENTER
ONLY 2  ATTEMPT LEFT

ENTER USER NAME- mazher123
ENTER YOUR PASSWORD- hellomazher

WRONG USER NAME OR PASSWORD ENTER
ONLY 1  ATTEMPT LEFT

ENTER USER NAME- mazher99
ENTER YOUR PASSWORD- mazher9908

WRONG USER NAME OR PASSWORD ENTER
ONLY 0  ATTEMPT LEFT
"""


