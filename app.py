from flask import Flask, render_template

app = Flask(__name__)


@app.get("/admin/dashboard")
def dashboard():
    module = 'dashboard'
    return render_template('admin/dashboard.html', module=module)


@app.get("/admin/user")
def user():
    module = 'user'
    return render_template('admin/user.html', module=module)
