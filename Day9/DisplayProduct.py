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
    mycursor.execute("SELECT * FROM products")
    data=mycursor.fetchall()
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
import mysql.connector as ms
(101, 'Soap', 50)
(102, 'Choclate', 10)
(103, 'chips', 20)
"""