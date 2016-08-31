import sqlite3 
conn = sqlite3.connect("hellrpgdb.db")
c = conn.cursor()


class Model():
	def __init__(self):
		pass

	def check_user(self, username, password):
		c.execute("""
			SELECT username, password FROM user
			WHERE username = ? AND password = ?
			""",(username, password))

		verified_user = c.fetchall()
			
		return verified_user
	
	def new_user(self, username, password):
		c.execute("""INSERT INTO user
			(username, password)
			VALUES (?, ?)
			""",(username, password))
		conn.commit()
		

	def update_user(self, username, password):
		c.execute("""UPDATE user
					SET username = ? , password = ?
					WHERE username = ? AND password = ?
					""",(username, password))
		conn.commit()

class Sum(Model):
	def __init__(self):
		self.count = counter()

	def counter(self, value):
		self.count += value

	def finalize(self):
		return self.count


	# def create_login_table(self):
	# 	conn = sqlite3.connect('hellrpgdb.db')
	# 	print("opening the database to create table")
	# 	conn.execute(''' CREATE TABLE USER
	# 		(ID INT PRIMARY KEY NOT NULL,
	# 		username TEXT NOT NULL,
	# 		password TEXT NOT NULL);''')
	# 	print("Table created Sucessfully")
	# 	c.close()

	# def create_login(self, c_username, c_password):
	# 	conn = sqlite3.connect('hellrpgdb.db')
	# 	print('database opened to insert data')

	# 	conn.execute("""INSERT INTO USER(username, password)
	# 		VALUES(?, ?);
	# 		""",(c_username, c_password)
	# 		)

	# 	conn.commit()
	# 	print("Records new user created sucessfully")
	# 	conn.close()












		

# conn = sqlite3.connect('hellrpgdb.db')
# print ("Opened database successfully");

# cursor = conn.execute("SELECT id, user_name, user_type, password, email  from user")
# for row in cursor:
#    print ("id = ", row[0])
#    print ("user_name = ", row[1])
#    print ("user_type = ", row[2])
#    print ("password = ", row[3])
#    print ("email = ", row[4])

# print ("Operation done successfully");


# conn.close()

