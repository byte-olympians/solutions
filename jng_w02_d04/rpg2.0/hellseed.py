"""
seed the database with admins
"""

import sqlite3
conn = sqlite3.connect('hellrpgdb.db')
c = conn.cursor()


c.execute(
	"""CREATE TABLE user (
	id INTEGER PRIMARY KEY,
	username TEXT,
	password TEXT,
	last_played INTEGER
	);"""
)

conn.commit()
conn.close()
print("Your database was created")



# db = 'hellrpgdb.db'

# user = ["Andrew", "Super User", "Cheese", "Andrew.Kolansky@gmail.com" ]

# conn = sqlite3.connect(hellrpgdb.db)
# c = conn.cursor()

# print("Replacing old data")
# c.execute("DELTE FROM user")

# for user in USERS:
# 	c.execute("""INSERT INTO user("user_name",
# 	 "user_type", "password", "email") VALUES(?,?,?,?)
# 		""",(user[0],user[1], user[2], user[3], user[4]))

# conn.commit()
# c.close()

# print("Looks like we're all good")