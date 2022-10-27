# 변수와 쿼리문 연결
import dbconn as db

conn = db.dbconn()
cursor = conn.cursor()

sql = '''insert into blog values(?,?,?)'''

# data = [('첫번째 글제목','첫번째 글내용','/static/blog/img/img01.png'),
#         ('두번째 글제목','두번째 글내용','/static/blog/img/img02.png')]
# cursor.executemany(sql,data) # 여러개 데이터 처리

data = ('첫번째 글제목','첫번째 글내용','/static/blog/img/img01.png')
cursor.execute(sql,data)
conn.commit()
conn.close()