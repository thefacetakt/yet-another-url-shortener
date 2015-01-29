#Vagrand - front-end к virtual-box
SERVER_URL = "http://127.0.0.1:4999/"

from flask import Flask, render_template, redirect, request, url_for

from urls import get_url, add_url
app = Flask(__name__)


@app.route("/")
def home():
    return """
<head>
    <html>
    </html>
    <body>
        <h2> Shorten an url! </h2>
        <form method="post" action="/new_url">
            <label>
                Your url: <br />
                <input type="text" name="url" />
            </label>
            <input type="submit" value="Just do it!" />
        </form>
    </body>
</html>
"""

@app.route("/new_url", methods=["POST"])
def new_url():
    url = add_url(request.form['url'])
    print(url)
    return """
<head>
    <html>
    </html>
    <body>
        <h2> Cool! now your url is here:</h2>
        <a href=\"""" + SERVER_URL + url + """\">""" + SERVER_URL + url + """ </a>
    </body>
</html>
"""

@app.route("/<int:url_id>")
def return_url(url_id):
    return redirect(url_for(get_url(url_id)))

if __name__ == "__main__":
    app.run(debug=True, port=4999)
