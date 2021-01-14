import mysql.connector as ms

try:
    conn=ms.connect(
        host="localhost",
        user="root",
        password="123",
        database="mydba",
        charset="utf8"
    )
    print("Data Base connected")
    mycursor=conn.cursor()
    query="SELECT * FROM products WHERE id=101 AND price>=50"
    mycursor.execute(query)
    data=mycursor.fetchall()
    print("Products table")
    for row in data:
        print(row)



except ms.DatabaseError as e:
    print("OPeration Failed reson is:",e)
    if conn:
        conn.rollback()
finally:
    if mycursor:
        mycursor.close()
    if conn:
        conn.close()

#OUTPUT
"""
DisplayOnly.py
Data Base connected
Products table
(101, 'Soap', 50)
(101, 'Soap', 50)
(101, 'Soap', 50)

"""
        