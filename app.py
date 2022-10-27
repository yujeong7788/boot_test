from flask import  Flask,render_template,request

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

@app.route('/write')
def write():
    print('/write 호출됨')
    return render_template('write.html')

@app.route('/signup')
def signup():
    print('/signup 호출됨')
    return render_template('signup.html')

@app.route('/user/<username>')
def show_username(username):
    return f'username : {username}'

@app.route('/user/<username>/<int:age>')
def show_username_age(age,username):
    return f'이름은 {username} 나이는 {age}'

@app.route('/user')
def show_user():
    return f'{request.args.get("age")}'

@app.route('/formtest',methods=['GET','POST'])
def formtest():
    if request.method =='GET':
        return render_template('formtest.html')
    else:
        print(request.form)
        return render_template('result.html',data = request.form) # post는 ??에 담긴다
    

if __name__=="__main__":
    app.run(port=80,debug=True)

# app.run(port=80,debug=True) # 웹 서비스의 기본 포트 80 (생략가능)

