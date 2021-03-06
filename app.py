from flask import Flask,request, jsonify
from detector import main

app = Flask(__name__, static_url_path='/static')


@app.route('/', methods=['POST'])
def hello_world():
    response = main.run(request.form.get('image_url'))
    return jsonify(response)


if __name__ == '__main__':
    app.run()
