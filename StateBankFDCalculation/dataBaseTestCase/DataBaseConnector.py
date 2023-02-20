import mysql.connector

connection = mysql.connector.connect(host="localhost", port=3306, user="root", passwd="", database="new_schema")

cur = connection.cursor()
cur.execute("insert into new_table values(105,'sham','pune')")
connection.commit()

# cur.execute("select * from new_table;")
# for row in cur:
#     print(row[0], row[1], row[2])

connection.close()

