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
    cursor.execute("SELECT * FROM torneios WHERE id_torneio=%s", (id,) )
    result = cursor.fetchall()
    connector.commit()
    try:
        return flask.jsonify(result[0])
    except IndexError:
        flask.abort(404)

@app.route('/torneios/<id>', methods=["DELETE"])
def delete(id):
    try:
        cursor.execute("DELETE FROM torneios WHERE id_torneio=%s", (id,) )
        deletedrows = cursor.rowcount
    except Exception:
        flask.abort(500)
    if deletedrows > 0:
        return flask.Response("", status=201)
    else:
        flask.abort(400)

@app.route('/<table>/', methods=["POST"])
@app.route('/<table>', methods=["POST"])
def add(table):

    try:
        sqlprops = ""
        sqlvals = []
        sqlpropstemplate = ""
        fst = True
        for prop in flask.request.json:
            if not fst:
                sqlprops += ", "
                sqlpropstemplate += ", "
            else:
                fst = False
            sqlprops += prop
            sqlvals.append(flask.request.json[prop])
            sqlpropstemplate += "%s"
        del fst
        sqltemplate = f"""INSERT INTO {table} ({sqlprops}) VALUES ({sqlpropstemplate})"""
        print(sqltemplate)
        cursor.execute(sqltemplate, sqlvals)
        connector.commit()

    except Exception as ex:
        print(ex)
        return flask.Response(f"{str(ex)}\n", status=500)

    else:
        return flask.Response("Done\n", status=201)

@app.route('/torneios/<id>', methods=["PUT"])
def update(id):
    try:
        query = """UPDATE torneios
        SET """
        updatevals = []
        try:
            updatevals.append(flask.request.json["id"])
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
        query += " WHERE id_torneio=%s"
        updatevals.append(idsensor)
        result = cursor.execute(query, updatevals)

        addedrows = cursor.rowcount
        connector.commit()

        return flask.jsonify({"sucess": True})

    except Exception as error:
        print(error)
        return flask.jsonify({"sucess": False, "error_message": str(error)})


@app.route('/torneios', methods=["GET"])
@app.route('/torneios/', methods=["GET"])
def getall():
    cursor.execute("SELECT * FROM torneios")
    result = cursor.fetchall()
    connector.commit()
    try:
        return flask.jsonify(result)
    except IndexError:
        return flask.jsonify({"sucess": False})

if __name__ == '__main__':
    app.run(debug=True)

