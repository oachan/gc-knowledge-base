```
docker run
docker run \
    --name nginx-dev \
    -v /home/xxx/nginx_dev/nginx.conf:/etc/nginx/conf.d/default.conf:ro \
    --rm \
    -p 8090:8090 \
    nginx:1.21.3
	
	

nginx.conf
server {
        listen 8090 default_server;
        location / {
                proxy_http_version 1.1;
                proxy_pass http://xx.xx.xx.xx:33337;
                proxy_connect_timeout 20;
                proxy_send_timeout 20;
                proxy_read_timeout 90;
                proxy_ignore_client_abort on;
                proxy_set_header Host $host;
                proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
        }
}
```

這是把nginx作為reverse proxy的範例
只要改 proxy_pass http://xx.xx.xx.xx:33337; 即可



Markdown
## NginxReverseProxy
### 摘要
由於 gunicorn 在透過SIGHUP 重啟worker達成 reload model 目的時，會有一瞬間打向舊worker的請求失敗，
因此外層再串上本Reverse Proxy，當失敗時再自動retry
## 如何執行
- 掛載 `nginx.conf` 進 container 即可，並根據情況改 port.
- nginx:1.21.3 是 jmeter 測試過不會有失敗請求的版本，可視情況升級nginx.
```
docker run \
    --name nginx-dev \
    -v /home/xxx/nginx_dev/nginx.conf:/etc/nginx/conf.d/default.conf:ro \
    --rm \
    -p 8090:8090 \
    nginx:1.21.3
```
