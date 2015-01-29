SERVER_URL = "http://127.0.0.1:5001/"

from flask import Flask, render_template, redirect, request

from urls import get_url, add_url

app = Flask(__name__)

def make_normal(url):
    if (url[:7] == "http://" or url[:8] == "https://"):
        return url
    else:
        return "http://" + url

@app.route("/")
def home():
    return render_template("add_url.html")

@app.route("/added/<url_id>")
def result(url_id):
    return render_template("result.html", url=SERVER_URL + url_id)

@app.route("/new_url", methods=["POST"])
def new_url():
    url = add_url(make_normal(request.form['url']))
    return redirect("/added/" + url)
    

@app.route("/<int:url_id>")
def return_url(url_id):
    return redirect(get_url(url_id))

if __name__ == "__main__":
    app.run(debug=True, port=5001)
