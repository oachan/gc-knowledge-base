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
conda activate ENV_NAME
conda deactivate
```


## 刪除環境
conda env remove -n ENV_NAME




# Ipython notebook 使用

## 創建個人的 jupyter config file
* jupyter notebook --generate-config

## 修改設定檔 /home/[user]/.jupyter/jupyter_notebook_config.py
* c.NotebookApp.ip = '140.96.83.235' # 修改 server ip
* c.NotebookApp.open_browser = False # 這樣執行後才不會自動開瀏覽器
* c.NotebookApp.password = u'sha1:e4289527fd1a:f127541630422dc248bc67c98591377583ad4275' # 參考下方截圖產生個人加密密碼
* c.NotebookApp.port = 1711 # 請選擇一個你最喜歡的 port，不要跟別人衝到

## 設定加密密碼
``` sh
from notebook.auth import passwd
passwd()
Enter password:
Verify password:
Out[2]: 'sha1:67c9e60bb8b6:9ffede0825894254b2e042ea597d771089e11aed'
```

## jupyter notebook 載入 kernels
* conda install ipykernel
* conda install jupyter
* conda install nb_conda nb_conda_kernels
