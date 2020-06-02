from flask import Flask, redirect, url_for
app = Flask(__name__)
app.debug = True

@app.route('/')
def index():
    return 'hello'

if __name__=='__main__':
    app.run()