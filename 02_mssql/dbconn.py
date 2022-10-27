import pyodbc



def dbconn():
    server = '127.0.0.1'
    database = 'DoItSQL'
    username = 'sa'
    password = 'qwer1234'
    
    conn = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER='+server+';DATABASE='+database+';ENCRYPT=no;UID='+username+';PWD='+ password)
    return conn

if __name__=="__main__":
    print(__name__)
    # 자기 파일이 실행될때만 나오고 다른데서 호출할때는 안뜬다
#커넥션 개체까지 리턴시켜주는 함수