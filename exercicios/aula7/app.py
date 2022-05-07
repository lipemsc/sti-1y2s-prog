#!/bin/python3

import flask
import json
import mysql.connector

connector = mysql.connector.connect(
  host="localhost",
  user="root",
  password="root",
  database="sensors"
)

cursor = connector.cursor(dictionary=True)

app = flask.Flask(__name__)

@app.route('/app/<idsensor>', methods=["GET"])
def get(idsensor):
    cursor.execute("SELECT * FROM sensor WHERE idSensor=%s", (idsensor,) )
    result = cursor.fetchall()
    connector.commit()
    try:
        return flask.jsonify(result[0])
    except IndexError:
        return flask.jsonify({"sucess": False})

@app.route('/app/<idsensor>', methods=["DELETE"])
def delete(idsensor):
    cursor.execute("DELETE FROM sensor WHERE idSensor=%s", (idsensor,) )
    deletedrows = cursor.rowcount
    connector.commit()
    
    if deletedrows > 0:
        return flask.jsonify({"sucess": True})
    else:
        return flask.jsonify({"sucess": False})

@app.route('/app/', methods=["POST"])
@app.route('/app', methods=["POST"])
def add():
    #print(dict(flask.request.json))
    #return flask.request.json["aaa"]

    try:
        cursor.execute(
            """INSERT INTO sensor
                (idLocation, name, unit)
            VALUES
                (%s, %s, %s)""",
            (flask.request.json["idLocation"], flask.request.json["name"],flask.request.json["unit"]))

    except:
        return flask.jsonify({"sucess": False})

    addedrows = cursor.rowcount
    connector.commit()
    
    if addedrows > 0:
        return flask.jsonify({"sucess": True})
    else:
        return flask.jsonify({"sucess": False})

@app.route('/app/', methods=["GET"])
@app.route('/app', methods=["GET"])
def getall():
    cursor.execute("SELECT * FROM sensor")
    result = cursor.fetchall()
    connector.commit()
    try:
        return flask.jsonify(result)
    except IndexError:
        return flask.jsonify({"sucess": False})

if __name__ == '__main__':
    app.run(debug=True)

