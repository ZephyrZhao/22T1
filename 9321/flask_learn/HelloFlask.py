# 导入了这个Flask类。这个类的一个实例将是我们的WSGI应用程序
from flask import Flask

# 接着我们创建一个该类的实例。第一个参数是应用模块或者包的名称。 
# __name__ 是一个适用于大多数情况的快捷方式。
# 有了这个参数， Flask 才能知道在哪里可以找到模板和静态文件等东西。
app = Flask(__name__)
 
# 然后我们使用 route() 装饰器来告诉 Flask 触发函数 的 URL 。
# 函数返回需要在用户浏览器中显示的信息。
# 默认的内容类型是 HTML ，因此字 符串中的 HTML 会被浏览器渲染。 
@app.route('/')
def hello_world():
   return "<p>Hello, World!</p>"
 
if __name__ == '__main__':
   # app.run(host, port, debug, options)
   # host='0.0.0.0' 可以让服务器被公开访问。
   # 
   app.run()