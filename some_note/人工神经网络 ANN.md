# 人工神经网络 ANN

  ANN神经网络，实际上就是模仿人脑的逻辑思维过程，在计算机层面的实现。因此在懂得计算机层面实现之前，我们先分析一下我们人脑的分析过程。

我们先从最简单的开始，我们思考一下，我们是怎么知道，“2”这个数字是2。这个问题听起来可能有点无脑，但给你看到2这个数字，你就知道是2，这个过程其实没有那么简单。我们看到2，首先会注意到这个数字形状的上方有个弧度，之后顺着弧度下来会有一个平直方向的弯折，人脑将这些信息整合，最后反馈出结果，这个数字是2。而这些信息，就称作特征量。我把这些特征量提取并简化，就会得到接下来这张图

![特征提取](C:\Users\Administrator\Pictures\typoraimg\xs.png)

红点表示数字2的特征量在图像中的位置，如果以逻辑图的方式再进行进一步简化和抽象化，就变成了下面这张

![逻辑化](C:\Users\Administrator\Pictures\typoraimg\lj.png)

类似的，我们图中的1代表对我们做出判断有用的特征量，如果把上面这张图中的行都并排放一起，且把无特征量的位置标上0，就组成了![二进制](C:\Users\Administrator\Pictures\typoraimg\b.png)

这样就巧妙的组成了计算机最熟悉的二进制数，而这个二进制数就包含了数字“2”的所有特征信息（当然，是简化后的），同样，其余的0~9的数字也可以由这样一个独一无二的二进制数来包含其特征信息，足以将其和其他数字区分开。因此我们几乎所有的计算机识别过程的第一步，就是提取将要识别的物体的特征，就像世界上不可能有两片相同的树叶一样🍃，每个物体都会提取出不同的特征，只要将特征量的位置分布设置得足够多，记录的位置量足够大，再相似的两物体都会有不同的特征信息。这些信息共同的做决策，决定这个物体是什么。

现在我们回到我们的数字“2”![特征提取](C:\Users\Administrator\Pictures\typoraimg\xs.png)

我们可以思考一下，这里的所有红点（特征点），每个提供的信息都一样重要吗，当然不是，最重要的特征点当然是那些最能把这个数字和其他数字区分开来的。比如区分4和9，最重要的点当然能把这两个区别开来的数字“4”靠右边的那些特征。因此我们引入一个重要概念——**权重矩阵 W**。通过矩阵的线性运算将比较重要的特征点赋予较大的权重，比较无关紧要的点赋予较小的权重，这样就能更好的帮助神经网络实现决策。

将特征量赋予权重的过程，我们通过矩阵乘法实现，即将包含权重信息的矩阵（称为权重矩阵）与转化成矩阵的二进制信息相乘。但乘出来后的结果还不是最终结果，而是将特征量提取出来后的结果，称为隐藏层，为了更好的提取特征向量，我们还引入——**偏置节点**和**激活函数**，偏置节点用于提升权重矩阵提取出的特征的精度，使特征的提取更加灵活；激活函数的作用则在于矩阵之间的操作是线性的操作，但是自然界中特征的提取往往是非线性的，因此需要加入激活函数来提高网络提取特征的丰富程度，使之提取出的特征更加自然和多样化。而要得到我们期望的结果，我们还要对隐藏层中处理好的信息再做一层矩阵操作和又一次的激活函数，才能得到最终的输出结果，第二层激活函数的作用在于矩阵操作后的结果并不是我们想要的输出，激活函数在这里的作用就是将矩阵操作后的结果转化成我们想要的输出（后文会讲到我们想要的输出是什么）。关于连接隐藏层到输出层之间的矩阵，也是权重矩阵，这次的矩阵运算在于将我们隐藏层的特征向量转化成我们期望的输出。为简化表述，我们将输入层与隐藏层之间的权重矩阵记作**θ1**，隐藏层与输入层之间的权重矩阵记作**θ2**。

而接下来的问题是，我们期望的输出是什么？就像前面说到将图像输入计算机一样，计算机的输出也是一堆数字，因此，我们用不同的二进制数编码代表不同的数字。在以后我们要规定我们期望的输出时往往都要对各种可能输出的状态进行编码以便于计算机输出，称为==one hot encoder==。在光学数字识别中我们使用简单的编码，即用1×10的列表，每个数字在列表中的对应相同数字的索引的值设为1，其他位为0，例如数字0在1×10的列表中第0位索引的值设为1，其他为0，就得到数字0的编码[1,0,0,0,0,0,0,0,0,0]。以此类推，这些编码就是我们的每个数字的期望输出。因此上文提到的用激活函数来得到想要的输出在这里的体现，就在于将矩阵输出向量中的每个元素都转化成0~1之间的数，每个数都是对应索引数字与被识别数字匹配的概率，而在一个成熟的神经网络计算之下，我们输出的结果会逼近这个期望，以达到我们识别的效果。

在了解了**输入，权重矩阵，偏置节点和隐藏层**这些概念后，我们可以着手开始设计我们的神经网络了。

在设计神经网络时遇到的首先的第一个问题，权重矩阵中权重的值应该如何设置？我们不太可能一个一个的去估计每个特征的权重然后设计出对应的权重，也不太可能知道怎样的权重矩阵可以把隐藏层转化成逼近我们期望的输出。因此神经网络里的__学习__就由此引出，其中较为普遍的学习算法——**反向传播算法**。有了反向传播算法，我们的神经网络就有了学习能力，我们先随机给出θ1，θ2中各个权重的值，得到神经网络的计算输出再与我们的期望输出做差，得到**output_errors**，来衡量我们的计算输出相比于期望输出偏差多少，接着我们用θ2矩阵乘隐藏层得到输出的逆过程——用output_errors矩阵乘隐藏层，得到原先的权重矩阵与理想权重矩阵的**偏差矩阵**。接着我们用偏差矩阵乘一个小于1的数，这个数称为**学习速率**，再和原本的权重矩阵相加。这就是更新θ2矩阵的步骤，可以理解为以**学习速率**大小的速率更新θ2权重矩阵来逐渐减小期望与计算输出之间的差，减小误差。再利用output_errors算出偏差层误差hidden_errors，用于更新θ1。

反向传播算法的理解涉及矩阵求导，矩阵微分，矩阵的各种乘法等矩阵运算，我们现在可以先不必掌握其原理。我在下文用学过的函数方程类比矩阵做个简单粗糙的解释，如果没有兴趣了解也可以，毕竟我们身边本就充满着黑箱，我们带着黑箱的思维使用他们也并没有什么不好。