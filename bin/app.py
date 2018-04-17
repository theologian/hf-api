from flask import Flask, abort, request 
import logging

from flask import Flask
from flask_restful import Resource, Api, reqparse

log = logging.getLogger('werkzeug')
# disables verbose logging
log.setLevel(logging.ERROR)

app = Flask(__name__)
api = Api(app)

@app.route('/', methods = ['POST'])
def get_data():
    if request.method == 'POST':
        args = request.args
        print (args)
        p1count = args['p1']
        p2count = args['p2']
        p1 = request.args.get('p1')
        p2 = request.args.get('p2')
        return jsonify(dict(data=[p1, p2]))
        #return '''<h1>The value is p1: {}</h1>'''.format(p1)

@app.route('/test/', methods = ['POST'])
def get_priority():
    return request.query_string

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=3000, debug=True)
