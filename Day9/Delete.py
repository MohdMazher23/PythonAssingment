import mysql.connector as ms
try:
    conn=ms.Connect(
        host="localhost",
        user="root",
        password="123",
        database="mydba",
        charset='utf8'
    )
    print("Database Connected Successfully")
    cursor=conn.cursor()
    print("PRODUCTS TABLE BEFORE delete operation")
    select="SELECT * FROM products"
    cursor.execute(select)
    data=cursor.fetchall()
    for row in data:
        print(row)
    delete_query="DELETE FROM products WHERE price>40"
    cursor.execute(delete_query)
    print("Row is deleted succesfully")
    conn.commit()
    print("PRODUCTS TABLE AFTER delete operation")
    select="SELECT * FROM products"
    cursor.execute(select)
    data=cursor.fetchall()
    for row in data:
        print(row)


except ms.DatabaseError as e:
    print("OPeration Failed reson is:",e)
    if conn:
        conn.rollback()
finally:
    if cursor:
        cursor.close()
    if conn:
        conn.close()

#OUTPUT
"""
PRODUCTS TABLE BEFORE delete operation
(101, 'Soap', 50)
(102, 'Choclate', 10)
(103, 'chips', 20)

Row is deleted succesfully
PRODUCTS TABLE AFTER delete operation
(102, 'Choclate', 10)
(103, 'chips', 20)

"""