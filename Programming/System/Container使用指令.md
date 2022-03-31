# Docker
指令執行需要有 root/docker 權限.

## 顯示 container 清單
* 顯示啟動: `docker ps`
* 顯示所有: `docker ps -a`

## 進入 container 內部
`docker exec -it xxx bash`

## 設定 docker contrianer 自動重開
1. `docker ps -a` 確認 container 名稱
2. `docker update --restart unless-stopped [CONTAINER_NAME]`
3. 四種模式: [no, on-failure, always, unless-stopped]
4. `docker inspect` 檢查是否有變更設定成功
5. `docker inspect --format '{{.HostConfig.RestartPolicy.Name}}' <container-id>`

## `Dockerfile` Example
``` dockerfile
# pull official base image
FROM python:3.6.15

# set work directory
WORKDIR /usr/src/app

# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# install dependencies
RUN pip install --upgrade pip
COPY ./requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
# ... RUN pip install ...

# copy project
COPY . .
```

### python dockerfile
[打造最小 Python Docker 容器](https://blog.wu-boy.com/2021/07/building-minimal-docker-containers-for-python-applications/)
* python3.9
* python3.9-slim
* python3.9-alpine
* python3.9-alpine (Multistage)


# Docker-Compose
Docker Compose 是用來組合多個 container 成為一個完整服務的工具。可以很簡單的透過 Compose 的 yaml 來設定你的container應用程式。
* 啟動服務: `docker-compose -p $(PROJECT) up -d`
* 關閉服務: `docker-compose -p $(PROJECT) stop`
* 移除服務: `docker-compose -p $(PROJECT) down`

## `docker-compose.yml` Example
``` yml
version: '3.9'

services:
  web:
    build: ./Platform
    command: python manage.py runserver 0.0.0.0:38100
    volumes:
      - ./Platform/:/usr/src/app/
      - ./PlatformUploadScript/:/usr/src/PlatformUploadScript/
      - ./MovieScriptETL/:/usr/src/MovieScriptETL/
    ports:
      - 38100:38100
    environment:
      - HOST_IP=172.17.0.1
    restart: always
```
