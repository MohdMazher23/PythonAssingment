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
    insert="INSERT INTO products (id, name, price) VALUES (%s,%s,%s)"
    val=[(101,'Soap',50),(102,'Choclate',10),(103,'chips',20)]
    cursor.executemany(insert,val)
    print("RECORDS ADDED SUCCESSFULLY")
    conn.commit()
except ms.DatabaseError as e:
    print("OPeration Failed reson is:",e)
    if conn:
        conn.rollback()
finally:
    if cursor:
        cursor.close()
    if conn:
        conn.close()


#output
"""
Database Connected Successfully
RECORDS ADDED SUCCESSFULLY
"""