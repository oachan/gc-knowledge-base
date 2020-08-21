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
```
conda env remove -n ENV_NAME
```

## 顯示環境清單
```
conda info --envs
```

# Ipython notebook 使用

## 創建個人的 jupyter config file
```
jupyter notebook --generate-config
```

## 修改設定檔 /home/[user]/.jupyter/jupyter_notebook_config.py
```
c.NotebookApp.ip = '140.96.83.235' # 修改 server ip
c.NotebookApp.open_browser = False # 這樣執行後才不會自動開瀏覽器
c.NotebookApp.password = u'sha1:e4289527fd1a:f127541630422dc248bc67c98591377583ad4275' # 參考下方截圖產生個人加密密碼
c.NotebookApp.port = 1711 # 請選擇一個你最喜歡的 port，不要跟別人衝到
```

## 設定加密密碼
``` sh
from notebook.auth import passwd
passwd()
Enter password:
Verify password:
Out[2]: 'sha1:67c9e60bb8b6:9ffede0825894254b2e042ea597d771089e11aed'
```

## jupyter notebook 載入 kernels
```
conda install ipykernel jupyter nb_conda nb_conda_kernels
```


## conda 安裝 requirements.txt
`conda install --yes --file requirements.txt`



## 安裝 Jupyter notebook extensions
```
conda install -c conda-forge jupyter_contrib_nbextensions
```


---


# Jupyter notebook extensions
有鑑於組內大家使用Jupyter越來越頻繁，在此整理 Jupyter notebook 的設定流程

---

## 流程

### 1. 安裝 conda 
建議安裝方式：

在官網上 `https://www.anaconda.com/distribution/` 下載 linux 64-Bit (x86) Installer (506 MB) 使用 bash 安裝

### 2. 設定 jupyter
- 創建個人的 jupyter config file `jupyter notebook --generate-config`
- 修改設定檔 /home/[user]/.jupyter/jupyter_notebook_config.py
```
c.NotebookApp.ip = '140.96.83.235' # 修改 server ip
c.NotebookApp.open_browser = False # 這樣執行後才不會自動開瀏覽器
c.NotebookApp.password = u'sha1:e4289527fd1a:f127541630422dc248bc67c98591377583ad4275' # 參考下方截圖產生個人加密密碼
c.NotebookApp.port = 1711 # 請選擇一個你最喜歡的 port，不要跟別人衝到
```
- 設定加密密碼
``` sh
from notebook.auth import passwd
passwd()
Enter password:
Verify password:
Out[2]: 'sha1:67c9e60bb8b6:9ffede0825894254b2e042ea597d771089e11aed'
```

### 3. 設定 jupyter notebook
- 建議建立 jupyter 環境
    - `conda create --yes -n <ENV_NAME> python=3` (或者可以指定更細的python版本，如`python=3.6`)
    - `conda activate <ENV_NAME>`
- 安裝 kernel 相關套件，來讓 jupyter 上可以使用 kernel (建議每個<ENV_NAME>都要安裝，而jupyter於base啟動，如此一來可在notebook內選擇要使用的環境)
```
conda install ipykernel jupyter nb_conda nb_conda_kernels
```


### 4. 設定 Jupyter notebook extensions
- 安裝 Jupyter notebook extensions
```
conda install -c conda-forge jupyter_contrib_nbextensions
```
- 可選以下套件來幫助 IDE 使用
    - Autopep8
        - 提供自動 formating code 功能按鍵，需先安裝 `pip install autopep8`
    - Table of Contents
        - 提供目錄，可快速前往
    - Collapsible headings
        - 提供章節隱藏功能
    - Hinterland
        - 快速自動補全提示
    - Comment/Uncomment Hotkey
        - 提供一個新的註解按鍵 (alt+c)，可以設定啟動 indent comment
    - ExecuteTime
        - Cell 的 output 增加執行時間與完成時間
    - Notify
        - 提供任務完成後 Chrome 通知功能
    - Codefolding
        - 提供程式碼折疊功能

### 5. 設定 Jupyter notebook themes
- 安裝 jupyterthemes
```
pip install jupyterthemes
```
- 使用方式
```
# list available themes
# onedork | grade3 | oceans16 | chesterish | monokai | solarizedl | solarizedd
jt -l

# select theme...
jt -t chesterish

# restore default theme
# NOTE: Need to delete browser cache after running jt -r
# If this doesn't work, try starting a new notebook session.
jt -r

...
```
- 尋找好看的設定指令(default 都不好看)
```
# Example
jt -t monokai -f fira -fs 13 -nf ptsans -nfs 11 -N -kl -cursw 5 -cursc r -cellw 95% -T

# 歡迎提供指令
...
```
