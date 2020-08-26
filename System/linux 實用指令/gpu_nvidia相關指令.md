# GPU Nvidia 相關指令

## 確認 cuDNN 版本
```
whereis cuda
cat /usr/local/cuda/include/cudnn.h | grep CUDNN_MAJOR -A 2
```

## 確認 CUDA 版本
```
nvcc --version
```



## 持續監控 GPU 使用情況
``` sh
while true; clear; do nvidia-smi ; sleep 2; done
```


## 確認GPU卡資訊
```
lspci | grep ' VGA ' | cut -d" " -f 1 | xargs -i lspci -v -s {}
```


## 只使用某張GPU訓練
```
CUDA_VISIBLE_DEVICES=1
```

## TF 版本資訊
- [TF與CUDA使用版本資訊](https://tensorflow.google.cn/install/source#gpu)
