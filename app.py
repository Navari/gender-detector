from flask import Flask, jsonify
from detector import main

app = Flask(__name__, static_url_path='/static')


@app.route('/<username>')
def hello_world(username):
    print(username)
    response = main.run(username)
    if not response:
        return jsonify({'error' : 'Instagram error'})
    return jsonify(response)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
