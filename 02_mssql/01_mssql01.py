import pyodbc 

server = '127.0.0.1'
database = 'DoItSQL'
username = 'sa'
password = 'qwer1234'

# 커넥션 커밋
conn = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER='+server+';DATABASE='+database+';ENCRYPT=no;UID='+username+';PWD='+ password)
cursor = conn.cursor()
cursor.execute("SELECT top 5 * from stock")
row = cursor.fetchone()
while row:
    print(row[0])
    row = cursor.fetchone()