# 基于词典的方法进行词语级情感倾向性分析：



## 目的：

情感分析指的是对新闻报道、商品评论、电影影评等文本信息进行观点提取、主题分析、情感挖掘。情感分析的内容包括：情感的持有者分析、态度持有者分析、态度类型分析(一系列类型如喜欢(like),讨厌(hate),珍视(value),渴望(desire)等;或者简单的加权积极性如积极(positive),消极(negative)和中性(neutral)并可用具体的权重修饰。总的来说，***\*情感分析就是对文本信息进行情感倾向挖掘。\****

本次实验利用***\*基于词典的方法\****,就***\*J\*******\*ieba\*******\*中文分词\****使用功能,来对已有的语义知识库来推断词语的语义倾向性。我们结合老师提供的数据集中的正负情感词种子词集选择数个情感种子词，来计算数据集中最具有正向或负向情感的前50个单词(除去种子词)。通过这次实验来加深我们对社会计算理论知识的理解，巩固我们对词语级情感倾向性分析的应用。



## 内容：

### 方案设计：

基于词典的方法:根据已有的语义知识库，首先给定一个具有情感倾向的种子——***\*词语集合\****。当识别新词倾向性时，使用词义词典查找与新词语义相近的词语集，并根据***\*该词与种子集中每个词的词义相似程度来确定其语义倾向值\****。新词与正向种子集中的各个词联系越紧密，则该词的正向倾向越强烈；与负向种子集中的各个词联系越紧密，则该词的负向倾向越明显。

 令新词为w,定义种子集为seedset=(PP,PN),其中PP代表正向种子词集，PN代表负向种子词集。词w的语义倾向值为:

![img](file:///C:\Users\ming\AppData\Local\Temp\ksohtml13916\wps1.jpg) 

其中，ppk∈PP,pnl∈PN,K和L分别为正向种子集和负向种子集中种子词的个数。设置阈值为θ(θ≥0)，则|Polarity(w)|> θ表明该词是正向的，

Polarity(w)<-θ表示该词是负向的，|Polarity(w)|≤θ表示该词是中性词。Polarity(w)数值的大小表征词w的正负倾向强度。

概要设计：

利用数据库，jieba，OpenHowNet库来设计，jieba分词后，利用OpenHownet计算相似度，然后存入数据库中，再利用数据库的去重，排序，查询功能来得到正向或负向情感的前50个单词(除去种子词)

![img](file:///C:\Users\ming\AppData\Local\Temp\ksohtml13916\wps2.jpg)

### 具体设计：

实验结果展示

![img](file:///C:\Users\ming\AppData\Local\Temp\ksohtml13916\wps3.jpg)![img](file:///C:\Users\ming\AppData\Local\Temp\ksohtml13916\wps4.jpg) 

![img](file:///C:\Users\ming\AppData\Local\Temp\ksohtml13916\wps5.jpg)![img](file:///C:\Users\ming\AppData\Local\Temp\ksohtml13916\wps6.jpg) 

在尝试使用数据库存储后可以得到相对更加准确的结果，词条如下:
负向词：
有味 难吃 酸 油腻 嫩 满 反胃 赶不上 来不及 融 麻 慢 慢慢 晚 迟 迟到 迟迟 黏糊
凸 腻 油 难受 快 黄 冷 下饭 可口 合口味 寡淡 尽快 浓烈 浓郁 鲜美 晚点 好吃 稀烂 讨厌 毛 咸 发腻 可恨 可恶 够呛 焦 时 静 晚一点 较晚 美好 死
正向词：
对 棒 达 夸 赞 精选 完善 推 恭维 提倡 称赞 表扬 差 不错 欢迎 亲 地道 称 保证 行 俱佳 够味儿 良好 实在 评论 评 瓷实 体贴 保障 对得起 理睬 致敬 致歉 道歉 鞠躬 

好好 破 错 排 理 吸收 帮 帮助 帮忙 误 耍 拉 恭喜 纪录 记录

数据库截图:

![img](file:///C:\Users\ming\AppData\Local\Temp\ksohtml13916\wps7.jpg) 



### 核心算法分析

首先定义种子集PP

![img](file:///C:\Users\ming\AppData\Local\Temp\ksohtml13916\wps8.jpg) 

使用cursor()方法创建一个游标对象，再使用execute()方法执行SQL

![img](file:///C:\Users\ming\AppData\Local\Temp\ksohtml13916\wps9.jpg) 

再使用execute()方法执行SQL

![img](file:///C:\Users\ming\AppData\Local\Temp\ksohtml13916\wps10.jpg) 

使用预处理语句创建表，一个词和Polarity

![img](file:///C:\Users\ming\AppData\Local\Temp\ksohtml13916\wps11.jpg) 

定义函数得到词w的倾向值Polarity

![img](file:///C:\Users\ming\AppData\Local\Temp\ksohtml13916\wps12.jpg) 

读取数据集文件(外卖评论.csv)

![img](file:///C:\Users\ming\AppData\Local\Temp\ksohtml13916\wps13.jpg) 

 

 

 

 

 

 

 

之后再利用jieba分词工具对表中的数据进行分词

![img](file:///C:\Users\ming\AppData\Local\Temp\ksohtml13916\wps14.jpg) 

最后将数据库进行排序，并输出前50个正向词和负向词

![img](file:///C:\Users\ming\AppData\Local\Temp\ksohtml13916\wps15.jpg) 

![img](file:///C:\Users\ming\AppData\Local\Temp\ksohtml13916\wps16.jpg)



## 小结：

通过本次实习的结果可以看出，正向词和负向词的分词结果绝大部分是较为准确的，但是比较容易受所选的种子词个数和种子词的使用频率影响。但是也可能是分词工具的作用对相同的词语不同意义的分辨能力有限，毕竟一句话的真正含义是无法通过单独词语来逐次分析得到的。比如所得结果中的负向词“美好”“快”不禁让人认为是好的方面，而正向词中的“差”“拉”“破”也有可能是代表着负向的含义。通过对分词结果的分析，可以看出分词准确性与数据集的数量以及种子词的数量和质量有着重要的联系。

而相对的，在编程过程中遇到了相当一部分的问题，jieba分词想对于我们正常使用者来说有着较大的差别，有相当一部分的词汇jieba不能准确的分开，我们所使用的jieba.posseg.cut()并不能达到我想达到的效果。设置种子词的时候，有相当一部分的常用词并不能在词库中查找到，而且Polarity的计算结果会导致一些分类错误的出现。

以上就是使用python以及数据库进行简单情感分析的过程。通过这次社会计算项目，实现了运用于特定问题的情景之中的情感分析，使得我们对社会计算这一领域的问题有了更深的认识和了解。