# Anaconda 使用指令集

## 安裝
``` sh
wget https://repo.continuum.io/archive/Anaconda2-5.0.1-Linux-x86_64.sh
bash Anaconda2-5.0.1-Linux-x86_64.sh
```

## 建立環境
``` sh
conda create --yes -n py2 python=2
```

## 進入/離開環境
```
source activate py2
source deactivate
```