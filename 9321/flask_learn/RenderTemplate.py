from flask import Flask, render_template
app = Flask(__name__)

# --------渲染模版-------------------------------------------------------------------------------------
# 在python中直接生成html 例如return '<html><body><h1>'Hello World'</h1></body></html>' 很傻
# 使用flask.render_template()自动渲染，只需提供模版名称和相应的参数
# e.g. 以该程序RenderTemplate.py为例模版文件必须是以下结构，flask回自动在templates和static文件夹中寻找模版
# /RenderTemplate.py
# /templates
#   /index.html
# /static
#   /hello.js
# e.g. 是一个包
# /RenderTemplate
#   /__init__.py
#   /templates
#       /index.html
#   /static
#       /hello.js

#####一个香甜的栗子
@app.route('/hello/<user>/')
def hello_name(user):
    return render_template('index.html',name=user)

######又一个栗子
@app.route('/hello/<int:score>/')
def isPass(score):
    return render_template('isPass.html',marks=score)
# html中传入int 型的marks，用{%...%}括住if-else-endif



#####淦，还有一个栗子
@app.route('/result/')
def result():
    dic = {'phy':50,'che':60,'maths':70}
    return render_template('result.html', result = dic)
# html 中传入ditc型的result，{%for key,value in result.items() %}返回key和value值
# {{...}} 括住打印到模版的 输出

# --------静态文件-------------------------------------------------------------------------------------

# static_file.html 中的按钮 onclick事件调用static/static_file.js中的sayHello()函数
@app.route('/static/')
def static_file():
    return render_template("static_file.html")

if __name__=='__main__':
    app.run(debug=True)