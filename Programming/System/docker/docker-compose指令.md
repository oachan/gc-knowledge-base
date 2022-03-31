# Docker-Compose
Docker Compose 是用來組合多個 container 成為一個完整服務的工具。可以很簡單的透過 Compose 的 yaml 來設定你的container應用程式。
* 啟動服務: `docker-compose -p $(PROJECT) up -d`
* 關閉服務: `docker-compose -p $(PROJECT) stop`
* 移除服務: `docker-compose -p $(PROJECT) down`

## `docker-compose.yml` Example
``` yml
version: "3.9"

services:
  web:
    build: .
    ports:
      - "8000:5000"
    volumes:
      - .:/usr/src/app
    environment:
      - FLASK_ENV: development
    restart: always
```


## 額外資訊
[用 docker-compose 優雅關閉服務](https://blog.wu-boy.com/2021/06/graceful-stop-service-using-docker-compose-in-golang/)
