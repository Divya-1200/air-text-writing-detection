from flask import Flask,render_template,request, redirect, url_for
from main_write import main
from main_detect import infer_by_web


app = Flask(__name__)
#commitmessage

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/text')
def text():
    a = main()
    print("detected text", a)
    return render_template("text.html",test=a)

if(__name__=="__main__"):
    app.run(debug=True)