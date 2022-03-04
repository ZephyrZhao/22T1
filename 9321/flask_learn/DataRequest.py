from flask import Flask, request, render_template
app = Flask(__name__)

# --------数据请求-------------------------------------------------------------------------------------
# request.
# from    -字典对象，包含表单的健值对
# args    -解析查询字符串的内容，是问号(?)之后的URL的一部分
# cookies -保存cookie名称的健值对
# method  -当前请求的方法
# files   -上传文件有关的数据

@app.route('/login', methods=['POST', 'GET'])
def login():
    error = None
    if request.method == 'POST':
        if valid_login(request.form['user'],
                       request.form['password']):
            return log_the_user_in(request.form['user'])
        else:
            error = 'Invalid username/password'
    # 当请求形式为“GET”或者认证失败则执行以下代码
    return render_template('login.html', error=error)

def valid_login(id,password):
    # todo 链接数据库，获取id和密码进行对比
    return True
def log_the_user_in(user):
    #todo 返回该用户进入系统的页面
    return f'Welcome Home! {user}'

if __name__=='__main__':
    app.run(debug=True)
