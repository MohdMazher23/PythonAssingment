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
    mycursor.execute("CREATE TABLE products (id INT, name VARCHAR(20), price INT)")
    print("Table Created")
    conn.commit()

    

except ms.DatabaseError as e:
    print("OPeration Failed reason is ",e)
    if conn:
        conn.rollback()

finally:
    if mycursor:
        mycursor.close()
    if conn:
        conn.close()

#OUTPUT
"""
CreateProductTable.py
Data Base connected
Table Created

"""