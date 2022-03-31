# Docker
指令需要有 root 權限.

## 顯示 container 清單
`docker ps`

## 進入 container 內部
`docker exec -it xxx bash`

## docker contrianer 自動重開
1. `docker ps -a` 確認 container 名稱
2. `docker update --restart unless-stopped [CONTAINER_NAME]`
3. 四種模式: [no, on-failure, always, unless-stopped]
4. `docker inspect` 檢查是否有變更設定成功
5. `docker inspect --format '{{.HostConfig.RestartPolicy.Name}}' <container-id>`
