# Semi-Supervised Learning
一種結合標記資料與未標記資料的學習方式。典型的使用情境為有少量的標記資料與大量的未標記資料。

## Self-training
1995年，Yarowsky等人提出自我訓練算法，被視為半監督學習的基本雛形。

Self-training，顧名思義，就是在已有標籤基礎上，讓模型對無標籤數據進行分類，然後再把分類預測用於訓練，並從中獲取額外信息。

![](https://pic3.zhimg.com/80/v2-8f912949b5392732ee0776c89ede86c6_hd.jpg)

Self-training的主要缺點是模型無法糾正自己的錯誤。如果模型對自己的分類結果很有“自信”，但這是盲目自信，分類結果是錯的，那它就會在訓練中放大誤差。

此外，如果數據集 U 和數據集 L 的重合度很低，標籤集 C 並不能覆蓋U的所有類別，這種不良影響就更嚴重了。在這種情況下，模型的性能注定會很差。

### Pseudo-Label : The Simple and Efficient Semi-Supervised Learning Method for Deep Neural Networks
這是一篇發表在 ICML 2013 的文章，是一個相當簡單的讓網絡 work in semi-supervised fashion 的方法。就是把網絡對無標籤數據的預測，作為無標籤數據的標籤（即 Pseudo label），用來對網絡進行訓練，其思想就是一種簡單自訓練。

![](https://www.zhihu.com/equation?tex=L+%3D+%5Csum_%7Bm%3D1%7D%5En+%5Csum_%7Bi%3D1%7D%5EC+L%28y_i%5Em%2C+f_i%5Em%29+%2B+%5Calpha%28t%29+%5Csum_%7Bm%3D1%7D%5E%7Bn%27%7D+%5Csum_%7Bi%3D1%7D%5EC+L%28%7By%27%7D_i%5Em%2C+%7Bf%27%7D_i%5Em%29)

雖然思想簡單，但是還是有些東西需要注意的，就是這個 a(t)，其決定著無標籤數據的代價在網絡更新的作用，選擇合適的a(t) 很重要，太大性能退化，太小提升有限。在網絡初始時，網絡的預測時不太準確的，因此生成的 pseudo label 的準確性也不高。在初始訓練時， a(t) 要設為 0，然後再慢慢增加，論文中給出其增長函數。在後面的介紹中，有兩篇論文都使用了一種高斯型的爬升函數。

## Multi-view training
為了改善Self-training算法存在難以自查的缺點，那我們可以從不同數據的視角出發，構建不同的模型。

這裡的多角度只是一個泛指，它可以是不同特徵，也可以是不同的模型架構和不同數據集。

### Co-training
1998年，CMU的Blum和Mitchell在論文Combining Labeled and Unlabeled Data with Co-Training中首次提出Co-training概念。

這是多角度訓練的一個經典算法，也提出了相對較強的假設：資料L 可以被兩個條件獨立的特徵集L1 和L2 表示，且每個特徵集都能夠訓練出一個強學習器。

Co-training有 m1 和 m2 兩個模型，它們分別在不同的特徵集上訓練。每輪迭代中，如果兩個模型裡的一個，比如模型m1 認為自己對樣本x 的分類是可信的，置信度高，分類概率大於閾值τ ，那m1 會為它生成偽標籤，然後把它放入m2 的訓練集。

![](https://pic3.zhimg.com/80/v2-18770ddccd1aa69c1e11e89a70167afa_hd.jpg)

在Blum和Mitchell的那篇論文裡，Co-training的實驗場景是網頁分類，他們把網頁文本作為一個視角，把指向網頁的超鏈接信息作為第二個視角，成功完成了分類任務。

但現實任務中往往不存在這麼多條件獨立視圖，為了彌補這一缺陷，Chen等人在2011年提出了一種偽多視圖正則化（pseudo-multiview regularization）的方法[19]，能把特徵分成兩個互斥的角度，從而保證Co-training的有效性。

### Democratic Co-learning
不同於把不同特徵集作為視角，2004年，Zhou和Goldman提出了一種新算法——Democratic Co-learning[21]，他們認為基於不同的歸納偏差建模會是個更合適的選擇。這意味著這些模型不是固定不變的，它們在不同神經網絡裡可能有不同的架構，也可能是看起來完全不一樣的算法。

Democratic Co-learning首先會在數據集L上單獨訓練各模型，之後它再用這些模型對數據集U中的樣本進行分類預測。如果大多數模型對樣本的分類給出了可信度較高的結果，那它會給樣本生成標籤，並放入數據集 L 中。這個置信度的判斷標準是對於標籤分類結果，贊同模型的置信度平均值 w 之和是否大於不贊同模型的置信度的均值總和。

重複這個過程，直到所有樣本都已生成標籤。為了保障“民主”，最終預測會引入加權係數。

![](https://pic4.zhimg.com/80/v2-81572d330770694632174dc3ffce999f_hd.jpg)

### Tri-training
這是周志華等人於2005提出的一種算法，也是迄今為止所有多視圖訓練算法中知名度最高的一種。從某種意義上來說，Tri-training可以被視為Democratic Co-learning的一個特例，它會訓練三個獨立模型，然後用三者的一致性減少對不含標籤數據的預測偏差。

Tri-training的一個主要前提是初始模型必須是多樣的，這和Democratic Co-learning一樣，但後者實現的方法是使用不同的的架構，而前者則是從原始訓練數據L中用Bootstrap採樣機制獲得不同變體Si 。在這些採樣變體上分別訓練出 m1 、 m2 、 m3 三個模型後，它們無需計算置信度，只需按照“少數服從多數”的做法篩選出標籤。

例如對於預測標籤，模型 mj 和 mk 表示強烈同意，但模型 mi 不置可否，那麼算法會為樣本生成多數同意的偽標籤，然後把它放入 mi 的訓練集。

![](https://pic4.zhimg.com/80/v2-fa0f301e40918bfdaf1162b86245f97b_hd.jpg)

* Tri-training with disagreement
	* 模型只要在薄弱點有所提升就可以了，並且帶標籤的數據不該被簡單的數據點歪曲信息。
	* 要求對於模型 mj 和 mk 置信度較高的樣本，第三個模型 mi 應該拒絕預測，也就是disagreement。
* Asymmetric tri-training
	* 對於無監督域適應來說，不同於帶標籤數據，測試數據和無標籤數據擁有不同的源域。為了使Tri-training算法適應這種轉變，Asymmetric tri-training讓三個模型中的一個只在Pseudo-label上訓練，而不是已有標籤集（算法4中的第10行），並且這個模型只會在測試期間完全對目標域樣本進行分類。
	* 這就是它非對稱（Asymmetric）的原因——三個模型的作用是不一樣的。
	* ![](https://pic2.zhimg.com/80/v2-a9fefc3076db127c2d7d4a6dfa2f54ad_hd.jpg)
	* ![](https://pic3.zhimg.com/80/v2-2baa2363970e9b9ada89a5ec5df44ff6_hd.jpg)
* Multi-task tri-training
	* 如果說Tri-training有什麼缺點，那應該就是它有三個獨立模型要訓練，所以必須依賴大量訓練數據，這在實踐中的代價昂貴的。
	* 為了緩解這一問題，2018年，Ruder和Plank把遷移學習思想引入半監督學習，提出Multi-task tri-training算法[23]，旨在減少三體訓練過程中的時間、空間複雜度，實現跨模型知識共享和加速訓練。
	* 正如Multi-task這個詞所顯示的，Multi-task tri-training不再單獨訓練模型，而是共享參數，並用多任務學習（MTL）機制對它們進行聯合訓練。
	* Multi-task tri-training可以聯合訓練多任務模型及其三個特定模型的輸出，而且因為正交約束強制模型m1 和m2 之間的不同表示，算法不用對帶標籤的源域數據進行bootstrap採樣直至收斂。第三個模型 m3 只在生成了偽標籤的目標樣本上訓練，最後算法會依據“多數投票”機制決定最終預測結果。
	* ![](https://pic4.zhimg.com/80/v2-92f511f88f542838e7479b57f216fc67_hd.jpg)


## Self-ensembling
Self-ensembling其實和上一節的Multi-view training存在諸多相似之處，因為它們都結合了模型的不同變體，如Multi-task tri-training就可以被看作是一種Self-ensembling，它用三個不同的模型創建了一個更強的預測器。

但兩者也有不同，和Multi-view training相比，Self-ensembling對模型的多樣性看得更重。這類算法通常會在不同配置下訓練單個模型，以保證預測結果更穩健。下面所列的算法都是近幾年提出的，其中一些已經在計算機視覺上取得了state-of-the-art的成果。

### Ladder networks
Ladder Networks出自Semi-Supervised Learning with Ladder Networks，這篇由Rasmus等人撰寫的文章被譽為2015年深度學習領域“五大佳文”之一。

這篇文獻採用半監督的方法，充分利用了無標籤數據+少量有標籤數據，相比於以往的方法精度上有了大幅的提升。因為最後的網絡結構像梯子一樣，所以把它翻譯為“階梯網絡”。

Ladder networks 是 deep autoencoder 的變型。

- 下面是 Ladder networks 結構圖，與 deep autoencoder 網絡相比，在編碼部分的每一層都有一條橫向 skip connection，連接到解碼層。
- 除此之外，Ladder networks 在 encoder layer 的每一層都引入了噪聲(類似於 denoising autoencoder，不過 denoising autoencoder 只對輸入層加入噪聲，而 Ladder networks 是對 encoder layer 的每一層都加入了噪聲)
- 另外，階梯網絡網絡的損失函數是每一層的構建誤差損失函數C0、C1……CL(與降噪自編碼器不同在於：降噪自編碼器只對解碼輸出層構建損失函數C0)。最後無監督階梯網絡的總損失函數就是C0+C1……+CL。

![](https://img-blog.csdn.net/20160417115044145)

Ladder Network 對隱變量進行加噪降噪（這兩者的結合），而且是對網絡裡面每一層的隱變量（中間表示）都加denoising autoencoder，並用l-2 norm 進行最小化學習

- 可以看到，ladderNet 的降噪函數g 其實接收了兩個信息，一個是來自上層解碼器的隱變量重構z，另一個是從skip connection 傳過來的加噪隱變量z'，有了這個加噪隱變量 ，降噪函數就能很好地恢復編碼器（或者說分類器）丟失的信息，而不需要強迫編碼器保留所有的信息，這就是skip connection 的作用了。
- 在設計降噪函數g時，要去選擇讓隱變量服從哪一種類型的分佈，論文最終選了高斯分佈（Gaussian latent variables），則加噪隱變量 z' = z + n ，其中 n 是高斯噪聲。

Ladder Network 採用的是在網絡訓練過程中，直接把有監督和無監督的損失函數相加起來，作為總損失函數，進行梯度下降整體訓練。

- 給定N個有標籤的樣本數據(x(1),y(1))、(x(2),y(2))……，以及M個無標籤的樣本數據x(N+1)、 x(N+2)、x(N+3)……並且有標籤的樣本數據個數遠小於無標籤數據。我們的目標是學習出一個函數用來判別數據的標籤P(y|x)。
- 在階梯網絡中，這個函數是一個深度降噪自編碼器，噪聲加入所有的隱藏層，然後最後的損失函數是有標籤樣本數據的交叉熵損失函數+無監督各層噪聲解碼器重構誤差歐式損失函數：
	- ![](https://img-blog.csdn.net/20160417181912282)
![](https://pic2.zhimg.com/80/v2-ca2badd9329408116bfa922010e8eb41_hd.jpg)

算法前向傳導流程：

1. 先是有噪聲通道編碼、解碼前向計算；
2. 無噪聲通道前向計算；
3. 通過無噪聲通道各層數據Z與解碼器Z'構建損失函數;這樣就可以得到無監督部分損失函數。
4. 有監督部分損失函數計算：直接在噪聲通道的編碼器頂層接入分類器，構建損失函數。

需要注意的是：在訓練的時候，有監督部分輸出採用的是噪聲通道y’，構建損失誤差的；而在測試使用階段，採用的是無噪聲通道計算y。編碼階段和解碼階段有採用tied-weight、採用參數權值共享，CNN反捲積過程也是一樣。在訓練的時候，有標籤樣本隨機抽取但是需要保證每批各個類別的樣本個數相同，保證類別平衡。

The steps involved in implementing the Ladder network are typically as follows:

1. Take a feedforward model which serves supervised learning as the encoder. The network consists of 2 encoder paths - clean and corrupted encoder. The only difference is that the corrupted encoder adds Gaussian noise at all layers.
2. Add a decoder which can invert the mappings on each layer of the encoder and supports unsupervised learning. Decoder uses a denoising function to reconstruct the activations of each layer given the corrupted version. The target at each layer is the clean version of the activation and the difference between the reconstruction and the clean version serves as the denoising cost of that layer.
3. The supervised cost is calculated from the output of the corrupted encoder and the output target. The unsupervised cost is the sum of denoising cost of all layers scaled by a hyperparameter that denotes the significance of each layer. The final cost is the sum of supervised and unsupervised cost.
4. Train the whole network in a fully-labeled or semi-supervised setting using standard optimization techniques (such as stochastic gradient descent) to minimize the cost.

比較具體的網絡架構圖，有算法完整的框架

![](https://pic4.zhimg.com/80/v2-11893dbb07b4219d8b2f5c3be2288843_hd.jpg)

### Virtual Adversarial Training
VAT整體的設計思路源於對抗訓練，然而對抗訓練只適用於Supervised Learning的訓練，VAT則實現了 Semi-Supervised Learning。

對抗樣本就是使得機器學習的算法產生誤判的樣本。我們用一張解釋對抗樣本最經典的圖例說明。

![](http://www.twistedwg.com/assets/img/Adv/VAT1.png)

如上圖所示，原有的模型以57.7%的置信度判定圖片為熊貓，但添加微小的擾動後，模型以99.3%的置信度認為擾動後的圖片是長臂猿。這個添加擾動得到的樣本， 我們就稱之為對抗樣本。

傳統意義上來說，對抗訓練需要利用原始樣本的標籤才能生成擾動，但在2017年，Miyato等人在論文中首次提出Virtual Adversarial Training，指出無需標籤，模型也能生成對抗樣本，這就為它在半監督學習領域的使用打開了渠道。

下圖顯示了VAT如何在二維合成數據集上進行半監督學習。實驗使用了一個NN分類器，其中一個隱藏層有50個隱藏單元。在訓練開始時，分類器預測同一群中輸入數據點的不同標籤， 並且邊界上的LDS非常高（訓練剛開始時邊界）。算法優化模型在具有大LDS值的點周圍平滑。隨著訓練的進行，模型的演變使得具有大LDS值的點上的標籤預測受到附近標記輸入的強烈影響。這鼓勵模型預測屬於同一群集的點集的相同標籤，這是在半監督學習中經常需要的。在迭代1000次後，邊界已經分的很清晰了，同時預測的標籤也是越來越精準。

![](http://www.twistedwg.com/assets/img/Adv/VAT2.png)

### Π model / Temporal Ensembling

作者讓同一個圖片輸入網絡兩次，由於有一些隨機的因素（dropout, augmentation等），會使得兩次的隱藏層的輸出（也就是z）會不一樣，作者把兩個不同的z做差，然後求l2，作為loss的一部分，當然loss的另一部分就是那些有標籤數據的交叉熵(cross entropy)。

另外，由於模型最開始時是很不准確的，所以產生的z可能沒有多大意義，所以需要先對有label的數據進行訓練，也就是需要把兩次不同的z比較的loss進行屏蔽。作者這裡設置了一個隨時間變化的變量w(t)，在t=0時，設置w(t)為0，也是z比較的loss權重為0，然後w(t)隨著時間增大而增大。

![](https://images2015.cnblogs.com/blog/798706/201703/798706-20170328143803608-1153552920.png)

![](https://images2015.cnblogs.com/blog/798706/201703/798706-20170328144155436-204997815.png)

時序組合模型和雙模型的不同點在於，比較的z來源不同。在雙模型中，兩個z都是來自同一迭代時間內產生的兩次結果。但在時序組合模型中，一個z來自上次迭代周期產生的結果，一個z來自當前迭代時間內產生的結果，也就是比較了兩次不同時間內產生的z。

在時序組合模型中，由於一次迭代期間內，只用產生一次z，那麼相比於雙模型，它就有了兩倍的加速。作者在論文中說，他們使用的以前的z，並不是恰恰上次迭代的z，而是歷史z的加權和，即Z ← αZ + (1 − α)z（這個看著和reinforcement learning 中的reward的更新類似）。這樣做的好處是能夠保留歷史信息，衰減長遠歷史信息和穩定當前值。

![](https://images2015.cnblogs.com/blog/798706/201703/798706-20170328151130998-1812977939.png)

![](https://images2015.cnblogs.com/blog/798706/201703/798706-20170328151230014-1510280027.png)

### Mean Teacher
Mean Teacher 這篇文章一上來就說“模型成功的關鍵在於 target 的質量”，一語道破天機啊。而提高 target 的質量的方法目前有兩：1.精心選擇樣本噪聲；2. 找到一個更好的 Teacher model。而論文采用了第二種方法。

Mean teacher 也是堅信“平均得就是最好的”（不知道是不是平均可以去噪的原因...orz），但是時序上的平均已經被temporal ensembling 做了，因此Mean teacher 提出了一個大膽的想法，我們對模型的參數進行移動平均（weight-averaged），使用這個移動平均模型參數的就是teacher model 了，然後用teacher model 來構造高質量target。

一思索就覺得這想法好，對模型的參數進行平均，每次更新的網絡的時候就能更新teacher model，就能得到target，不用像temporal ensembling 那樣等一個迭代期這麼久，這對online model 是致命的。

## 相关工具和领域

# Ref
- [一文概览能生成代理标签的半监督学习算法](https://zhuanlan.zhihu.com/p/37747650)
- [非对称Tri-training实现无监督迁移](https://zhuanlan.zhihu.com/p/26523750)
- [深度学习（三十二）半监督阶梯网络学习笔记](https://blog.csdn.net/hjimce/article/details/50877704)
- [Introduction to Semi-Supervised Learning with Ladder Networks](https://rinuboney.github.io/2016/01/19/ladder-network.html)
- [三顾 Semi-supervised Learning with Ladder Network](https://zhuanlan.zhihu.com/p/34516078)
- [半监督阶梯网络学习笔记](https://blog.csdn.net/hjimce/article/details/50877704)