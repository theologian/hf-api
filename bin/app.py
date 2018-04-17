#from flask import Flask, abort, request 
from flask import Flask, request, jsonify
#from flask_restful import Resource, Api, reqparse
from flask_restful import Api
import logging
import priority as p

log = logging.getLogger('werkzeug')
# disables verbose logging
log.setLevel(logging.ERROR)

app = Flask(__name__)
api = Api(app)

@app.route('/', methods = ['POST'])
def get_data():
    if request.method == 'POST':
        args = request.args
        newdata = (args)
        p1count = args['p1']
        p2count = args['p2']
        p1 = request.args.get('p1')
        p2 = request.args.get('p2')
        update_data = p.runwithit(newdata)
        #return jsonify(dict(data=[p1, p2]))
        return update_data

@app.route('/test/', methods = ['POST'])
def get_priority():
    return request.query_string

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=3000, debug=True)
    p.run_once()
