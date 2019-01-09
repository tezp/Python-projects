from flask import Flask, request
from flask_restful import Resource, Api

app = Flask(__name__)
api = Api(app)

names = []


class MyRestAPI(Resource):

    def get(self):
        return names

    def post(self):
        names.append(request.form['name'])
        return {'Names ': names}

    def put(self):
        names[0] = request.form['name']
        return {'names ': names}

    def delete(self):
        del names[int(request.form['id'])]
        return names


api.add_resource(MyRestAPI, '/')

if __name__ == '__main__':
    app.run(debug=True)

# curl -v -X POST  -d 'name=tejprakash' 127.0.0.1:5000/
# curl -v 127.0.0.1: 5000
# curl -v -X PUT  -d 'name=tpk' 127.0.0.1:5000/
# curl -v -X DELETE  -d 'id=1' 127.0.0.1:5000/
