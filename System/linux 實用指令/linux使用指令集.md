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


# 關機
* sudo shutdown +30 "Development server is going down for maintenance. Please save your work ASAP."


# 顯示多個檔案, 附加檔案名稱
* tail -n +1 file1.txt file2.txt file3.txt


# 系统级 IO 监控
* iostat -xdm 1
    * https://jaminzhang.github.io/os/Linux-IO-Monitoring-and-Deep-Analysis/

# 查看所有的掛載資訊
* df -h