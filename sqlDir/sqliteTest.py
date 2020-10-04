import sqlite3


# def convert(value):
#     if value.startwith('~')
#     return value.strip('~')
#     if not value:
#         value = 0
#     return float(value)

conn = sqlite3.connect('test.db')
curs = conn.cursor()
curs.execute(''' 
create table test(
id TEXT PRIMARY KEY,
desc TEXT ,
water FLOAT,
kcal FLOAT,
protein FLOAT,
fat FLOAT,
ash FLOAT,
carbs FLOAT,
fiber FLOAT,
suger FLOAT
)
''')
query ='INSERT INTO test VALUES(?,?,?,?,?,?,?,?,?,?)'
# field_count =10
# for line in open('abbrev.txt'):
	# fields = line.split('^')
	# vals =[convert(f) for f in fields[:field_count]]
vals = ['1','nothing',1.2,1.2,1.2,1.2,1.2,1.2,1.2,1.2]
curs.execute(query,vals)
	

conn.commit()
conn.close()
