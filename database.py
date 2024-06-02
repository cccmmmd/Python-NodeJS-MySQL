import mysql.connector

con=mysql.connector.connect(
    user="root",
    password="1234567",
    host="localhost",
    database="mydb"
)
print("資料庫連線成功")
# Cursor 對資料庫下 SQL 指令
cursor=con.cursor()


# 新增資料
cursor.execute("INSERT INTO product(id, name) VALUES(5, '奶茶)")
cursor.commit() #確定執行

# 將變數資料帶入 SQL 指令
productId = 6
productName = "奶綠"
cursor = con.cursor()
cursor.execute("INERT INTO product(id, name) VALUES(%s, %s)",(productId, productName)) #只有一個變數時(productId,)
con.commit()

# 更新資料
cursor.execute("UPDATE product SET name='美式咖啡' WHERE id=1" )
con.commit()

productId = 1
productName = "美式"
cursor.execute("UPDATE product SET name=%s WHERE id=%s", (productName, productId) )
con.commit()

# 取得一筆資料
cursor.execute("SELECT * FROM product WHERE id=2")
data=cursor.fetchone()
print(data)
print(data[0], data[1])

# 取得多筆資料
cursor.execute("SELECT * FROM product")
data=cursor.fetchall()
print(data)

#逐一印出
for row in data:
    print(row)

# 刪除
cursor.execute("DELETE FROM product WHERE id=2" )
con.commit()


# 關閉資料庫
con.close()