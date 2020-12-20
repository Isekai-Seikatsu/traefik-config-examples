from flask import Flask, request

app = Flask(__name__)

@app.route('/')
def index():
    return 'Home Page'

@app.route('/rate-limit-0')
def rate_limit_0():
    return 'Rate Limit 0'

@app.route('/rate-limit-1')
def rate_limit_1():
    return 'Rate Limit 1'

@app.route('/headers')
def headers():
    return dict(request.headers)
