from flask import Flask, redirect

app = Flask(__name__)

SOURCE_PATH = "/hUtZh0"

DESTINATION_URL = "https://docs.google.com/forms/d/e/1FAIpQLSeYrUBMQVCKx3tY058wU1aDxJzBLbbMPwRcdu_996lW-Kj7iw/viewform"


@app.route(SOURCE_PATH)
def redirect_site():
    return redirect(DESTINATION_URL)


@app.route("/")
def home():
    return "URL Redirect is working!"


if __name__ == "__main__":
    app.run(debug=True)