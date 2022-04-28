import flask

app = flask.Flask(__name__)

@app.route('/app', methods=["GET", "POST"])
def index():
    if flask.request.method == "GET":
        return "Olá mundo"
    else:
        return "fgkljsdfgkldfhlgjkdhljk"

if __name__ == '__main__':
    app.run(debug=True)

