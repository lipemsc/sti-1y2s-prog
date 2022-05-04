### Ex 31
Considere a base de dados Sensores esquematizada na Figura 6. Implemente uma API/web service RESTful com os métodos GET, POST, PUT e DELETE, para as operações CRUD, sobre a tabela:

 - ~~(a) Alert~~
 - ~~(b) Unit~~
 - ~~(c) Location~~
 - **(d) Sensor**
 - ~~(e) Reading~~


#### NOTE TO SELF

Usar:

 - PUT para Update
 - POST para INSERT
 - DELETE para DELETE
 - GET para SELECT

Extensão YARC no Chrome dá muito jeito. Mas está cheia de tracking.

O seguinte faz o mesmo:

    curl 127.0.0.1:8080/app -X POST -d '{"key":"value"}' -H "Content-Type: application/json"

Dá (e devo) para usar diferentes rotas para diferentes `REQUEST METHODS`


