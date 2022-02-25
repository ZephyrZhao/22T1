from flask import Flask, jsonify, abort, request
app = Flask(__name__)
books = [
    {
        'id': 1,
        'title': u'论语',
        'auther': u'孔子',
        'price': 18
    },
    {
        'id': 2,
        'title': u'道德经',
        'auther': u'老子',
        'price': 15
    }
]
# 获取所有的书列表
@app.route('/bookstore/api/v1/books', methods=['GET'])
def get_tasks():
    return jsonify({'books': books})

# 获取指定书的信息
@app.route('/bookstore/api/v1/books/<int:id>', methods=['GET'])
def get_task(id):
    for book in books:
        if book['id']==id:
            return jsonify({'book': book})
    # flask.abort(错误码)可以让开发者在检测到错误时，立即将错误信息返回，返回的错误码必须是已知的http协议错误码
    # 404 not found， 400 bad request， 200 ok
    abort(404)

# 新增一本书
@app.route('/bookstore/api/v1/books/', methods=['POST'])
def create_task():
    if not request.form or not 'title' in request.form:
        abort(400)
    book = {
        'id': books[-1]['id'] + 1,
        'title': request.form['title'],
        'auther': request.form['auther'],
        'price': request.form['price'],
    }
    books.append(book)
    return jsonify({'book': book}), 201
# 更新一本书的信息
@app.route('/bookstore/api/v1/books/<int:id>', methods=['PUT'])
def update_book(id):
    for book in books:
        if book['id']==id:
            book["title"] = request.form['title']
            book["auther"] = request.form['auther']
            book["price"] = request.form['price']
        return jsonify({'books': books})
    abort(400)

# 删除一本书
@app.route('/bookstore/api/v1/books/<int:id>', methods=['DELETE'])
def delete_task(id):
    for book in books:
        if book['id']==id:
            books.remove(book)
            return jsonify({'result': True})
    abort(404)

    return jsonify({'result': True})


if __name__ == '__main__':
    app.run(debug=True)