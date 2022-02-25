from flask import Flask , redirect, url_for
app = Flask(__name__)

# --------Flask 路由--------------------------------------------------------------------------------------
# 如果访问地址 http://127.0.0.1:5000，浏览器返回“Index Page”
@app.route('/')
def index():
    return 'Index Page'
 
# 如果访问地址 http://127.0.0.1:5000/hello，浏览器返回“Hello,World”
@app.route('/hello')
def hello():
    return 'Hello, World'

# --------Flask 变量规则-----------------------------------------------------------------------------------------
# string 默认类型，接受没有“/”的字符串   e.g. '/user/<username>'
# int, float                         e.g. '/post/<int:post_id>'
# path 和 string 类似，但是接受斜杠“/”  e.g. '/path/<path:subpath>'
# uuid 只接受 uuid 字符串

# 当访问  http://127.0.0.1:5000/user/w3cschool 时，页面显示为用户User w3cschool。
@app.route('/user/<username>')
def show_user_profile(username):
    return f'User {username}'

# 当访问http://127.0.0.1:5000/post/3时，页面显示为帖子3.
# 用户在浏览器地址栏上输入的都是字符串，但是在传递给show_post函数处理时已经被转换为了整型。 
@app.route('/post/<int:post_id>') 
def show_post(post_id):
    #显示提交整型的用户"id"的结果，注意"int"是将输入的字符串形式转换为整型数据
    return 'Post {}'.format(post_id)

# 当访问http://127.0.0.1:5000/path/file/A/w3cschool.txt 时，
# 页面显示为 Subpath file/A/w3cschool.tx
@app.route('/path/<path:subpath>')
def show_subpath(subpath):
    return 'Subpath {}'.format(subpath)

# --------唯一的 URL / 重定向行为-------------------------------------------------------------------------------------
# projects的URL是中规中矩的，尾部有一个斜杠，看起来就如同一个文件夹。访问一个没有斜杠结尾的URL（/projects）时
#   Flask 会自动进行重定向，帮您在尾部加上一个斜杠（/projects/)。
# about的URL没有尾部斜杠，因此其行为表现与一个文件类似。如果访问这个URL时添加了尾部斜杠（/about/）
#   就会得到一个 404 NOT FOUND 错误。这样可以保持 URL 唯一，并有助于搜索引擎重复索引同一页面

@app.route('/projects/')
def projects():
    return 'The project page'

@app.route('/about')
def about():
    return 'The about page'

# --------URL 构建-------------------------------------------------------------------------------------
# url_for（）函数对于动态构建特定函数的URL非常有用。接受函数的名称作为第一个参数，以及任意数量的关键字参数
# （每个参数对应于URL的变量部分）。
@app.route('/admin/')
def hello_admin():
   return 'Hello Admin'
 
@app.route('/guest/<guest>')
def hello_guest(guest):
    return 'Hello {} as Guest'.format(guest)
 
@app.route('/user/<name>')
def hello_user(name):
    if name =='admin':
      # url重定向到 hello_admin()   
        return redirect(url_for('hello_admin'))
    else:
        return redirect(url_for('hello_guest',guest = name))
 
if __name__ == '__main__':
    app.run(debug = True)
