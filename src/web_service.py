from flask import Flask, jsonify

app = Flask(__name__, static_url_path="")

@app.route('/json', methods=['GET'])
def json():
    content = {'id': 1, 'first_name': 'Leilah', 'last_name': 'Shapter'}
    content2 = {'id': 2, 'first_name': 'Rob', 'last_name': 'Jerrolt'}
    lista = [content, content2]
    return jsonify(lista)

@app.route('/', methods=['GET'])
def helloWorld():
    return "Hello world!"

if __name__ == '__main__':
    app.run()
