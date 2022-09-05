from flask import Flask, render_template, request, session, redirect,url_for

app = Flask(__name__)



@app.route('/')
def index():
    if 'username' in session:
        username = session['username']
        return 'logged in as' + username + '<br>' + "<b><a href = /logout> click hear to log out</a></b>"
    return "you are not logged in <br><a href = '/login'</b>" + "click hear to login</b></a>"



@app.route('/login', methods=["POST", "GET"])
def login():
    if request.method == "post":
        session['username'] = request.form['username']
        return redirect(url_for('index'))
    return render_template('session.html')



@app.route('/logout')
def logout():
    session.pop('username', None)
    return redirect(url_for('index'))


if __name__ == '__main__':
    app.run(debug=True)