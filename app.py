from __future__ import with_statement

from flask import Flask, request, g, redirect, url_for, \
     abort, render_template, flash
from flask.helpers import send_file
from flaskext.markdown import Markdown

# create our little application :)
app = Flask(__name__)
app.config.from_object(__name__)
Markdown(app, extensions=['nl2br', 'fenced_code', 'md_in_html' , 'legacy_attrs'])

@app.route("/")
def root():
     return redirect("/about")

@app.route("/about")
def about():
     return render_template("article.html", content=open("./static/about.md", encoding="UTF-8").read(), currentnav=1)

@app.route("/cv")
def cv():
     return render_template("article.html", content=open("./static/cv.md", encoding="UTF-8").read(), currentnav=2)

@app.route("/portfolio")
def portfolio():
     return render_template("article.html", content=open("./static/portfolio.md", encoding="UTF-8").read(), currentnav=3)

@app.route("/download")
def download():
     file_name = 'static/resources/RESUME_hongkyo-kim.zip'
     return send_file(file_name,
                    mimetype='zip',
                    attachment_filename='RESUME(Hongkyo-kim).zip',# 다운받아지는 파일 이름. 
                    as_attachment=True)

if __name__ == '__main__':
     
     url = 'http://localhost'
     # webbrowser.open(url)
     app.run(host='0.0.0.0', port=80, debug=True)
