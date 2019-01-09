from flask import Flask, jsonify, request

app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def tp():
    if request.method == 'POST':
        return jsonify({"Requested ": request.form['name']})
    else:
        return jsonify({"tej": 'kumawat'})


@app.route('/<int:num>', methods=['GET', 'POST'])
def get_square(num):
    return jsonify({"Square : ": num ** 2})


if __name__ == '__main__':
    app.run(debug=True)

# curl -v 127.0.0.1:5000
# curl -v 127.0.0.1:5000/5
# curl -v -X POST  -d 'name=tej' 127.0.0.1:5000/
