# linux 使用指令集

## 查詢 port 對應的 pid
```
netstat -nlp | grep [port]
```

## 新增遠端桌面設定檔
``` sh
# vi  ~/.xsession
add line "xfce4-session"
```

## Linux 時間同步
``` sh
sudo ntpdate -s time.nist.gov 
```

## CPU/GPU 資訊
``` sh
cat /proc/cpuinfo
nvidia-smi -L
```

## Remove carriage return in Unix
``` sh
dos2unix *
```


# 檔案複製

## 遠端
* scp

## 進度
* pv


# 歷史紀錄
* history


# 查天氣
* curl 'wttr.in/hsinchu?lang=zh'
* curl 'wttr.in/:help'​
* https://github.com/chubin/wttr.in
