from flask import Flask ,request,url_for,redirect
app = Flask(__name__)

# --------HTTP 方法-------------------------------------------------------------------------------------
# login.html为演示脚本,用浏览器打开
# GET：   请求指定页面信息，并返回
# HEAD：  类似于GET。只是没有实体，只返回报头                   
# POST：  向指定资源提交数据并发送处理请求
# PUT：   client 向 server发送的数据取代指定的内容            
# DELETE：请求服务器删除指定内容



@app.route('/success/<name>')
def success(name):
    return 'welcome {}'.format(name)
 
@app.route('/login',methods = ['POST', 'GET'])
def login():
    if request.method == 'POST':
        # request.from['nm'] 获取表单中name属性为 nm
        # input 标签 name属性规定了 input元素的名称，用于对提交到服务器后的表单进行标识
        # 只有 name 属性的表单元素才能再提交表单时传递值
        user = request.form['nm']
        return redirect(url_for('success',name = user))
    else:
        user = request.args.get('nm')
        return redirect(url_for('success',name = user))
 
if __name__ == '__main__':
    app.run(debug = True)