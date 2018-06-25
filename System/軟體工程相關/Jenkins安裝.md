# Jenkins 安裝指南

## OS: ubuntu 14.04

### 安裝

1. 安裝 Ubuntu Linux 14.04 LTS
2. 安裝 Java
3. 安裝 Jenkins
    ```sh
    wget -q -O - https://pkg.jenkins.io/debian/jenkins-ci.org.key | sudo apt-key add -
    sudo sh -c 'echo deb http://pkg.jenkins.io/debian-stable binary/ > /etc/apt/sources.list.d/jenkins.list'
    sudo apt-get update
    sudo apt-get install jenkins
    ```
4. 設定 Jenkins
    ```
    # /etc/default/jenkins
    HTTP_PORT=8080
    ```
5. 設定 sudo 權限與免密碼
    ```
    # /etc/passwd
    jenkins:x:111:117:Jenkins,,,:/var/lib/jenkins:/bin/bash

    # /etc/sudoers
    %sudo   ALL=(ALL:ALL) NOPASSWD: ALL

    # /etc/group
    sudo:x:27:user,jenkins
    ```
6. 管理 Jenkins
    ```
    # Upgrade
    sudo apt-get update && sudo apt-get upgrade jenkins

    # Start, Restart, Stop
    sudo service jenkins start
    sudo service jenkins restart
    sudo service jenkins stop
    ```
7. 登入Web管理頁面
- curl http://[host]:8080
- default account: admin
- default passwd: cat /var/lib/jenkins/secrets/initialAdminPassword

### Git原始碼管理
1. 需確認linux環境下，安裝的jenkins，已安裝git。
2. 安裝好Jenkins和Git，並確認Jenkins中已經安裝了Git plugin外掛。
3. default clone 下來的 repository 會放置在 /var/lib/jenkins/workspace

### 建議安裝的 Plugin
1. Git plugin
2. Config File Provider Plugin
3. SonarQube Scanner for Jenkins