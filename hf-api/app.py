from flask import Flask, request, jsonify
from flask_restful import Api
import logging
import priority as p
import json

log = logging.getLogger('werkzeug')
# disables verbose logging
log.setLevel(logging.ERROR)

app = Flask(__name__)
api = Api(app)

@app.route('/', methods = ['POST'])
def get_p1():
    if request.method == 'POST':
        args = request.args
        p1 = request.args.get('p1')
        np1 = jsonify(dict(p1=[p1]))
        #if p1:
        #p.runwithit(np1)

        p1count = args['p1']
        p2count = args['p2']
        print p1count
        p2 = request.args.get('p2')
        np2 = jsonify(dict(p2=[p2]))
        #if p2:
        #p.runwithit(np2)
        return jsonify(dict(data=[args]))
        #return  args
        #return  '{} {}'.format(np1, np2)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=3000, debug=True)
    p.run_once()
