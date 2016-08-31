import sqlite3

conn = sqlite3.connect('hellrpgdb.db')
print ("Opened database successfully");

cursor = conn.execute("SELECT id, user_name, user_type, password, email  from user")
for row in cursor:
   print ("id = ", row[0])
   print ("user_name = ", row[1])
   print ("user_type = ", row[2])
   print ("password = ", row[3])
   print ("email = ", row[4])

print ("Operation done successfully");

conn.commit()
conn.close()