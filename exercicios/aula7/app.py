import flask
import json
import mysql.connector
import mysql.connector

connector = mysql.connector.connect(
  host="localhost",
  user="root",
  password="root",
  database="sensors"
)

cursor = connector.cursor(dictionary=True)

app = flask.Flask(__name__)

@app.route('/app/<idsensor>', methods=["GET", "POST"])
def index(idsensor):
    if flask.request.method == "GET":
        cursor.execute("SELECT * FROM sensor WHERE idSensor=%s", (idsensor,) )
        result = cursor.fetchall()
        connector.commit()
        
        return flask.jsonify(result)
    else:
        return "fgkljsdfgkldfhlgjkdhljk"

if __name__ == '__main__':
    app.run(debug=True)

