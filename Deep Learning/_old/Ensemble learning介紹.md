# Ensemble learning介紹

## Bagging := Bootstrap aggregation
<方法1>Ensemble的Bagging方法(Bagging := Bootstrap aggregation)用于多个复杂模型/容易overfitting模型/low bias high variance模型的融合以及降低variance
(1)Bagging的动机： 我们知道，对于一个机器学习模型，如果提高其模型的复杂性(比如：线性模型把input feature增加)，那么这个模型的bias是会不断地降低的，可是此时variance同时又会开始不断增加，所以综合起来，复杂的模型是有可能overfitting的（overfitting的一个统计学体现就是：小的bias 和 大的 variance）。 但是，学界给出了一个使用混合模型减小复杂模variance的方法，也就是bagging。




## Boosting
<方法二>.Ensemble的Boosting方法(Boosting很好记，就是一种和Bagging相反的方法，当我们使用Boosting的时候，是应该想要将对数据集fitting不是很好的模型变得更加的fit,也就是说Boosting是用作提升模型的fit程度，降低模型的Bias值的Ensemble方法)

Boosting的优势：Boosting承诺，只要你当前的模型的测试正确率比乱猜好一点(如:二分类，测试正确率比50%高一点)，Boosting就有能力把正确率提升至百分之百。

Boosting的主要步骤: (注意：在训练Boosting中的多个模型时，需要按顺序训练，先训练模型1，然后是模型2，然后是模型3...)


## ref
[lihungyi的ensemble learning intro课](https://www.jianshu.com/p/9baa00b20348)
