# Anaconda 使用指令集

## 安裝
``` sh
wget https://repo.continuum.io/archive/Anaconda2-5.0.1-Linux-x86_64.sh
bash Anaconda2-5.0.1-Linux-x86_64.sh
```

## 建立環境
``` sh
conda create --yes -n ENV_NAME python=2
```

## 進入/離開環境
```
source activate ENV_NAME
source deactivate
```


## 刪除環境
conda env remove -n ENV_NAME
