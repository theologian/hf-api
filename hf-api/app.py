from flask import Flask, request, jsonify, make_response
import logging, json
import priority as p

log = logging.getLogger('werkzeug')
# disables verbose logging
log.setLevel(logging.ERROR)

app = Flask(__name__)

@app.route('/', methods = ['POST'])
def post_data():
    data = request.args
    response_data = p.run_priority(data)
    response_data = jsonify(response_data)
    return response_data

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=3000, debug=True)
    p.run_once()
