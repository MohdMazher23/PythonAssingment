



print("POWER CONSUPTION APP")

units=float(input("ENTER THE NO OF units CONSUMED "))
if units<1 and units<0:
    print("INVALID units ENTERED")
else:
    if units>1.0 and units<=50.0:
        bill_amount=units*3
    elif units>51.0 and units<=100.0:
        bill_amount=units*6
    elif units>101.0 and units<=150.0:
        bill_amount=units*9
    elif units>151.0 and units<=200.0:
        bill_amount=units*12
    else:
        bill_amount=units*15

print("THE TOTAL units CONSUMED IS: ",units)
print("TOTAL BILL AMOUNT",round(bill_amount,4))
#output
"""
POWER CONSUPTION APP
ENTER THE NO OF units CONSUMED 151.9
THE TOTAL units CONSUMED IS:  151.9
TOTAL BILL AMOUNT 1822.8
"""