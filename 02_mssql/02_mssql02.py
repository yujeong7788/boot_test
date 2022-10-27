import dbconn as db

conn = db.dbconn()
cursor = conn.cursor()
sql = '''IF NOT EXISTS (SELECT * FROM sysobjects WHERE name='blog') 
	create table blog(
	id int identity not null primary key,
	title nvarchar(100) not null,
	content nvarchar(255) not null,
	img_path nvarchar(100))'''
cursor.execute(sql)
conn.commit()
conn.close()
# 변경이 있는건 commit , 쿼리 실행되는지 확인해보기