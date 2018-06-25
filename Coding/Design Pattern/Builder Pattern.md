# Builder pattern

## 定義
將一個複雜物件的構建與他的參數分離，使得同樣的構建過程可以創建不同的物件。

## 與 Factory pattern 的差異
工廠類模式：創建單個類的模式（關注單個產品）
建造者模式：將各種產品集中起來進行管理（關注複合對象）

## Python 是否需要 Builder pattern ?
But Python supports named parameters, so this is not necessary. You can just define a class's constructor:

``` python
class SomeClass(object):
    def __init__(self, foo="default foo", bar="default bar", baz="default baz"):
        # do something
```

and call it using named parameters:

``` python
s = SomeClass(bar=1, foo=0)
```

