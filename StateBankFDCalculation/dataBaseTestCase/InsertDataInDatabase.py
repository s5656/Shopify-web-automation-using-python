import mysql.connector

connection = mysql.connector.connect(host="localhost", port=3306, user="root", passwd="", database="new_schema")

cur = connection.cursor()
#cur.execute("insert into fd_calculatoins values(20000,10,2,'year(s)','Simple Interest',24000)")
#cur.execute("insert into fd_calculatoins values(40000,15,5,'year(s)','Simple Interest',70000)")
#cur.execute("insert into fd_calculatoins values(50000,10,3,'month(s)','Simple Interest',51250)")
#cur.execute("insert into fd_calculatoins values(75000,12,2,'month(s)','Simple Interest',76500)")
#cur.execute("insert into fd_calculatoins values(75000,12,2,'day(s)','Simple Interest',75045.32)")
connection.commit()
connection.close()
print("done")
