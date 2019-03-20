from flask import Flask, render_template, redirect, url_for, request
app = Flask(__name__)


posts = [
    {
        'author': "me",
        'title': 'hello',
        'content': 'there',
        'date_posted': 'today'
    },
    {
        'author': "you",
        'title': 'hello',
        'content': 'there',
        'date_posted': 'yday'
    }

]

@app.route("/")
@app.route("/home")
def hello():
    return render_template('home.html', posts=posts)

@app.route("/about")
def about():
    return render_template('about.html', posts=posts)

@app.route("/login")
def login():
    error = None
    if request.method == 'POST':
        if request.form['username'] != 'admin' or request.form['password'] != 'admin':
            error = 'Invalid Credentials.'
        else:
            return redirect(url_for('home'))
    return render_template('login.html', error=error)


if __name__ == '__main__':
    app.run(debug=True)
