#!/bin/python3

import flask
import mysql.connector

connector = mysql.connector.connect(
  host="localhost",
  user="root",
  password="root",
  database="torneios"
)

PRIMARY_KEYS = {
    "torneios": "id_torneio",
    "equipa": "id_equipa",
    "jogo": "id_jogo",
    "jogador": "id_jogador"
}

VALID_TABLES = (
    "equipa",
    "jogador",
    "jogo",
    "membros_equipa",
    "torneios"
)

cursor = connector.cursor()

def genfields():
    cursor.execute("SHOW TABLES")
    result = cursor.fetchall()
    fields = []
    for i in result:
        cursor.execute(f"SHOW COLUMNS FROM {i[0]}")
        result2 = cursor.fetchall()
        for j in result2:
            fields.append(j[0])
    return fields

cursor.dictionary = True

VALID_FIELDS = genfields()

app = flask.Flask(__name__)

@app.route('/torneios/<id>', methods=["GET"])
def gettorneios(id):
    cursor.execute("SELECT * FROM torneios WHERE id_torneio=%s", (id,) )
    result = cursor.fetchall()
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
        assert table in VALID_TABLES, "Possible SQL Injection attempt / Wrong Table"
        sqlprops = ""
        sqlvals = []
        sqlpropstemplate = ""
        fst = True
        for prop in flask.request.json:
            assert prop in VALID_FIELDS, "Possible SQL Injection attempt / Wrong Field"
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
        print(f"{type(ex).__name__}: {ex}")
        return flask.Response(f"Ocorreu um erro\n", status=400)

    else:
        return flask.Response("Done\n", status=201)

@app.route('/<table>/<id>', methods=["PUT"])
def update(id, table):
    try:
        assert table in VALID_TABLES, "Possible SQL Injection attempt / Wrong Table"
        sqlprops = ""
        sqlvals = []
        fst = True
        for prop in flask.request.json:
            assert prop in VALID_FIELDS, "Possible SQL Injection attempt / Wrong Field"
            if not fst:
                sqlprops += " , "
            else:
                fst = False
            sqlprops += f"{prop} = %s"
            
            sqlvals.append(flask.request.json[prop])
        del fst
        sqltemplate = f"UPDATE {table} SET {sqlprops} WHERE {PRIMARY_KEYS[table]} = %s"
        sqlvals.append(id)
        print(sqltemplate)
        print(sqlvals)
        cursor.execute(sqltemplate, sqlvals)
        connector.commit()

    except Exception as ex:
        print(f"{type(ex).__name__}: {ex}")
        print(cursor._executed_list)
        return flask.Response(f"Ocorreu um erro\n", status=400)

    else:
        return flask.Response("Done\n", status=201)


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

