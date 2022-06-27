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

cursor = connector.cursor(dictionary=True)

def genfields():
    c = connector.cursor()
    c.execute("SHOW TABLES")
    result = c.fetchall()
    fields = []
    for i in result:
        c.execute(f"SHOW COLUMNS FROM {i[0]}")
        result2 = c.fetchall()
        for j in result2:
            fields.append(j[0])
    del c
    return fields

VALID_FIELDS = genfields()
#print(VALID_FIELDS)

app = flask.Flask(__name__)

@app.route('/<table>/<id>', methods=["GET"])
def gettorneios(id, table):
    try:
        assert table in VALID_TABLES, "Possible SQL Injection attempt / Wrong Table"
        cursor.execute(f"SELECT * FROM {table} WHERE id_torneio=%s", (id,) )
        result = cursor.fetchall()
        retval = result[0]
        return flask.jsonify(retvalue)
    except Exception as ex:
        print(f"{type(ex).__name__}: {ex}")
        return flask.Response(f"Ocorreu um erro\n", status=400)

@app.route('/<table>/<id>', methods=["DELETE"])
def delete(id, table):
    try:
        assert table in VALID_TABLES, "Possible SQL Injection attempt / Wrong Table"
        cursor.execute(f"DELETE FROM {table} WHERE id_torneio=%s", (id,) )
        deletedrows = cursor.rowcount
    except Exception as ex:
        print(f"{type(ex).__name__}: {ex}")
        return flask.Response(f"Ocorreu um erro\n", status=400)
    else:
        return flask.Response("Done\n", status=201)

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
        return flask.Response(f"Ocorreu um erro\n", status=400)

    else:
        return flask.Response("Done\n", status=201)


@app.route('/<table>', methods=["GET"])
@app.route('/<table>/', methods=["GET"])
def getall(table):
    try:
        assert table in VALID_TABLES, "Possible SQL Injection attempt / Wrong Table"
        cursor.execute(f"SELECT * FROM {table}")
        result = cursor.fetchall()
        connector.commit()
        return flask.jsonify(result)
    except Exception as ex:
        print(f"{type(ex).__name__}: {ex}")
        return flask.Response(f"Ocorreu um erro\n", status=400)

if __name__ == '__main__':
    app.run(debug=True)

