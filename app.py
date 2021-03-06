from flask import Flask, request, render_template, redirect, url_for, abort


import game

app = Flask(__name__)



@app.route('/')
def index():
    return "메인페이지"

@app.route('/hello')
def hello():
    return 'Hello, world!'



@app.route('/hello/<name>')
def hellovar(name):
    character = game.set_character(name)
    return "{0}님 반갑습니다." .format(character["닉네임"]) 

@app.route('/game')
def ame():
    return "{0}님 반갑습니다." .format(character["닉네임"]) 



@app.route('/input/<int:num>')    
def input(num):
    name =''
    if num == 1:
        name = '도라에몽'
    elif num == 2:        
        name = '진구'
    elif num ==3:
        name = '퉁퉁이'
    else:
        return "없어요"
    return "hello {}".format(name)

@app.route('/login')
def login():
    return render_template('login.html') 



# @app.route('/method', methods=['GET', 'POST'])    
# def method():
#     if request.method == 'GET':
#         return "GET으로 전달된 데이터"
     
#     else:
#         id = request.form['id']
#         pw = request.form['pw']
        
#         if (id == 'aaa' and pw == '1234'):
#             print(id, pw)
#             root= Tk()
#             root.withdraw()
#             return msg.showinfo('로그인 성공!' ,'아이디: {} 패스워드: {}'.format(id, pw))
#         else:
#             root= Tk()
#             root.withdraw()
#             return msg.showinfo("로그인 실패", "잘못 입력하셨습니다.")



@app.route('/form')
def login():
    return render_template('test1.html')


@app.route('/method', methods=['GET', 'POST'])
def method():
    if request.method == 'GET':
        return 'GET으로 전송이다'
    else:
        num = request.form['num']
        name = request.form['name']
        print(num, name)
        with open("static/save.txt", "w", encoding='utf-8') as f:
            f.write("%s,%s" % (num, name))
        return 'POST 이다 학번은: {} 이름은: {} '.format(num, name)


@app.route('/naver')    
def naver():
    return render_template("naver.html")

@app.route('/daum')
def daum():
    return redirect("https://www.daum.net/")

@app.route('/move/daum')
def url_test():
    return redirect(url_for('daum'))


@app.route('/move/naver')
def url_test2():
    return redirect(url_for('naver'))


@app.route('/img')
def img():
    return render_template("image.html")

@app.route('/urltest')
def url_test3():
    return redirect(url_for('naver'))

@app.route('/move/<site>')    
def move_site(site):
    if site == 'naver':
        return redirect(url_for('naver'))
    elif site == 'daum':
        return redirect(url_for('daum'))
    else: 
        return abort(404)

@app.errorhandler(404)
def page_not_found(error):
    return "페이지가 없습니다. URL을 확인하세요." , 404


if __name__ == '__main__':
    # with app.test_request_context():
    #     print(url_for('daum'))
    #     print(url_for('naver'))
    app.run(debug=True)


