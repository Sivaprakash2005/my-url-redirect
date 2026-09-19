from flask import Flask, redirect

app = Flask(__name__)

# YOUR DOMAIN
DOMAIN = "qrto.org"

# DESTINATION
DESTINATION_URL = "https://docs.google.com/forms/d/e/1FAIpQLSeYrUBMQVCKx3tY058wU1aDxJzBLbbMPwRcdu_996lW-Kj7iw/viewform"


@app.route("/hUtZh0")
def activate_redirect():

    print(f"{DOMAIN}/hUtZh0 activated")

    return redirect(DESTINATION_URL, code=302)


@app.route("/")
def home():
    return f"""
    <h1>{DOMAIN}</h1>
    <p>Redirect is active.</p>
    <a href="/hUtZh0">Open Link</a>
    """


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)