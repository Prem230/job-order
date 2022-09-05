from flask import Flask, redirect, url_for

app = Flask(__name__)


@app.route('/admin')
def hello_admin():
    return "Hello "


if __name__ == '__main__':
    app.run(debug=True)
