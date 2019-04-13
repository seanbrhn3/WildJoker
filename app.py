from flask import Flask, render_template, request, url_for
from googleapiclient.discovery import build
from httplib2 import Http
from oauth2client import file, client, tools
from pprint import pprint
from SendJoke import Spreadsheet

app = Flask(__name__)
sheets = Spreadsheet()
@app.route('/')
def index():
    return render_template("index.html")

@app.route('/google',methods=['GET','POST'])
def google():
    jokes = sheets.google_values
    if request.method == "POST":
        print(request.form["joke"])
        sheets.add_values_google(request.form)
    return render_template("google.html",jokes=jokes)

@app.route('/amazon',methods=['GET','POST'])
def amazon():
    jokes = sheets.amazon_values
    if request.method == "POST":
        print(request.form)
        sheets.add_values_amazon(request.form)
    return render_template("amazon.html",jokes=jokes)

if __name__ == '__main__':
    app.run(debug=True)
