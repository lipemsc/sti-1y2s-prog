#!/bin/python3

import flask
import mysql.connector

connector = mysql.connector.connect(
  host="localhost",
  user="root",
  password="root",
  database="torneios"
)

cursor = connector.cursor(dictionary=True)

app = flask.Flask(__name__)

@app.route('/torneios/<id>', methods=["GET"])
def gettorneios(id):
    cursor.execute("SELECT * FROM torneios WHERE id_torneio=%s", (idsensor,) )
    result = cursor.fetchall()
    connector.commit()
    try:
        return flask.jsonify(result[0])
    except IndexError:
        abort(404)

@app.route('/app/<id>', methods=["DELETE"])
def delete(idsensor):
    cursor.execute("DELETE FROM torneio WHERE id_torneio=%s", (idsensor,) )
    deletedrows = cursor.rowcount
    connector.commit()
    
    if deletedrows > 0:
        return Response("", status=201)
    else:
        abort(400)

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

        addedrows = cursor.rowcount
        connector.commit()

        if addedrows > 0:
            return flask.jsonify({"sucess": True})
        else:
            return flask.jsonify({"sucess": False})

    except Exception as error:
        print(error)
        return flask.jsonify({"sucess": False, "error_message": str(error)})

@app.route('/app/<idsensor>', methods=["PUT"])
def update(idsensor):
    try:
        query = """UPDATE sensor
        SET """
        updatevals = []
        try:
            updatevals.append(flask.request.json["idLocation"])
            query += "idLocation = %s, "
        except NameError:
            pass

        try:
            updatevals.append(flask.request.json["name"])
            query += "name = %s, "
        except NameError:
            pass

        try:
            updatevals.append(flask.request.json["unit"])
            query += "unit = %s, "
        except NameError:
            pass

        query = query[0:-2]
        query += " WHERE idSensor=%s"
        updatevals.append(idsensor)
        result = cursor.execute(query, updatevals)

        addedrows = cursor.rowcount
        connector.commit()

        return flask.jsonify({"sucess": True})

    except Exception as error:
        print(error)
        return flask.jsonify({"sucess": False, "error_message": str(error)})


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

