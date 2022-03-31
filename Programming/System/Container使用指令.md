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

# Docker-Compose
Docker Compose 是用來組合多個 container 成為一個完整服務的工具。可以很簡單的透過 Compose 的 yaml 來設定你的container應用程式。
* 啟動服務: `docker-compose -p $(PROJECT) up -d`
* 關閉服務: `docker-compose -p $(PROJECT) stop`
* 移除服務: `docker-compose -p $(PROJECT) down`
