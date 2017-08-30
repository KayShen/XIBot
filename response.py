import json
from bottle import route, run, request

@route('/response', method='POST')
def upload_image():
    response = request.query.payload
    print response

if __name__ == "__main__":
    run(host='0.0.0.0', port=8080, debug=True)