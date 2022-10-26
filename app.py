from flask import  Flask,render_template

app = Flask(__name__)

@app.route('/') #요청이 루트로 들어옴???
def index():
    print('/ 호출들어옴') # DB 연결 등등 하고
    return render_template('index.html') # 템플릿 파일 찾아서 html에 연동해라

@app.route('/blog')
def blog():
    print('/blog 호출됨')
    return render_template('blog.html')

@app.route('/list')
def list():
    print('/list 호출됨')
    return render_template('list.html')

app.run(port=80,debug=True) # 웹 서비스의 기본 포트 80 (생략가능)

