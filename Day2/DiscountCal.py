while True:

    print("DISCOUNT CALCULATOR APP")
    purchase_amount=int(input("ENTEER THE PURCHASE AMOUNT "))
    discount_amount=0
    if purchase_amount>100 and purchase_amount<=1000:
        discount_amount=(0/100)*purchase_amount
    elif purchase_amount>1001 and purchase_amount<=2000:
        discount_amount=(20/100)*purchase_amount

    elif purchase_amount>2001 and purchase_amount<=3000:    
        discount_amount=(20/100)*purchase_amount

    elif purchase_amount>3001:
        discount_amount=(25/100)*purchase_amount


    print("\n\n")
    print("PURCHASE AMOUNT= ",purchase_amount)
    print("Disount = ",discount_amount)
    total_bill=purchase_amount-discount_amount
    print("TOTAL AMOUNT AFTER DISCOUNT IS ",total_bill)
    u_input=input("DO YOU WANT TO CONTINUE TYPE YES ELSE NO  ")
    if u_input!='yes':
        ("Exited")
        break

#OUTPUT
"""
PURCHASE AMOUNT=  3500
Disount =  875.0
TOTAL AMOUNT AFTER DISCOUNT IS  2625.0
DO YOU WANT TO CONTINUE TYPE YES ELSE NO  yes
DISCOUNT CALCULATOR APP
ENTEER THE PURCHASE AMOUNT 2500



PURCHASE AMOUNT=  2500
Disount =  500.0
TOTAL AMOUNT AFTER DISCOUNT IS  2000.0
DO YOU WANT TO CONTINUE TYPE YES ELSE NO  no
"""