import = sqlite3

conn = sqlite3.conect('hellrpgDB.py')

conn.execute(
	""""
	CREATE TABLE Player (
		id Integer primary key,
		Health,
		weapon,
		potions,
		gender,
		))