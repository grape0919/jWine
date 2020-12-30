from __future__ import with_statement

from flask import Flask, redirect, render_template

# create our little application :)
app = Flask(__name__)
app.config.from_object(__name__)

@app.route("/")
def root():
     return redirect("/home")

@app.route("/home")
def about():
     return render_template("main.html", currentnav=1)

@app.route("/searcher")
def searcher():
     return render_template("searcher.html", currentnav=2)

@app.route("/recommend")
def recommend():
     return render_template("recommend.html", currentnav=3)

@app.route("/signin")
def signin():
     return render_template("signin.html", currentnav=0)

@app.errorhandler(404)
def page_not_found(e):
    # note that we set the 404 status explicitly
    return render_template('404.html'), 404

app.register_error_handler(404, page_not_found)

if __name__ == '__main__':
     
     url = 'http://localhost'
     # webbrowser.open(url)
     app.run(host='0.0.0.0', port=80, debug=True)
