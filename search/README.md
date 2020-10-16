
Нужно добавить параметры
```
http.cors.enabled: true
http.cors.allow-origin: "*"
http.cors.allow-methods : OPTIONS, HEAD, GET, POST, PUT, DELETE
http.cors.allow-headers : X-Requested-With,X-Auth-Token,Content-Type, Content-Length
```
в `elastisearch.yml` в директории `config` и перезапустить демон.

Предполагается, что достучаться до `elasticsearch` можно по `localhost:9200`.
