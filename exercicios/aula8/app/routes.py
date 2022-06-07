import mysql.connector
import json
from flask import render_template
from app import app

connector = mysql.connector.connect(
  host="localhost",
  user="root",
  password="root",
  database="sensors"
)

cursor = connector.cursor(dictionary=True)

@app.route('/')
def index():
    cursor.execute("""
        SELECT sensor.idSensor as id, sensor.name as name, location.name as loc, unit.unit as unit
        FROM
            sensor
                INNER JOIN location ON sensor.idLocation=location.idLocation
                INNER JOIN unit ON sensor.unit=unit.unit
        """)
    result = cursor.fetchall()
    connector.commit()
    #return json.dumps(result)
    #print(result)
    return render_template('index.html', data=result)

@app.route('/id/<id>')
def byid(id):
    cursor.execute(f"""
        SELECT sensor.idSensor as id, sensor.name as name, location.name as loc, location.description as locd, unit.unit as unit, unit.description as unitd
        FROM
            sensor
                INNER JOIN location ON sensor.idLocation=location.idLocation
                INNER JOIN unit ON sensor.unit=unit.unit
        WHERE sensor.idSensor={id}
        """)
    result = cursor.fetchall()
    connector.commit()
    #return json.dumps(result)
    #print(result)
    return render_template('id.html', data=result)