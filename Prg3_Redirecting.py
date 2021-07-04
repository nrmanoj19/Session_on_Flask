from flask import Flask, redirect, url_for
app = Flask(__name__)


@app.route('/admin')
def my_admin():
    return "Welcome Admin"


@app.route('/guest/<g_name>')
def my_guest(g_name):
    return "Welcome %s as Guest" % g_name


@app.route('/user/<name>')
def my_user(name):
    if name == 'admin':
        return redirect(url_for('my_admin'))
    else:
        return redirect(url_for('my_guest', g_name=name))


app.run(debug=True)
