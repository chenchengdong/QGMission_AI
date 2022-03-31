## QG训练营人工智能组第2周周记

2022年 3月 31日

### 生活随记

- 周一：一开始我对于代码实现是十分恐惧的，在听完师兄的培训只会还是不知道该如何用代码实现线性回归，同时高数也还没学到梯度。然后我就上网看了一下，猛然发现，原来就是师兄在ppt里提到的最小二乘法和矩阵求导，再配合numpy的np.dot()和转置公式即可完成最小二乘法的线性回归
- 周二：经历过周一的思考，周二基本上就有思路如何写了，但是遇到的第一个问题是，一开始我随便整了一个学习率，立刻就溢出的，接着我在师兄的引导下删除了几个特征量，还是溢出，我就开始怀疑是不是算法写错了，但是经过一波验算，发现没有错之后我就有上网看了一下别人是如何完成的，发现是我学习率调大了，接着是画图上遇到了一个小问题，就是画散点图的时候，我传入的x，y这两个数据集维度不同，然后又是一波调试，最后一波折腾之后的出来的结果就是，np.array()是个好东西，你值得拥有！
- 周三：周三基本上没做过，都在学习线代和高数（落太多了😭）
- 周四：下午将线性回归封装成了一个类，晚上进行了数据分析文件的收尾工作，赶在ddl前交已经是万幸啦🤣
- 这里放一张拟合后的图片纪念一下😁

![](https://ccd123.oss-cn-guangzhou.aliyuncs.com/img/20220331225318.png)

![](https://ccd123.oss-cn-guangzhou.aliyuncs.com/img/20220331225223.png)

```python
#线性回归核心代码：
    def gradient_descent(self):
        for self.i in range(self.iter_numbers):  # 开始梯度下降
            self.cost = np.dot((np.dot(self.X_train, self.theta) - self.y_train).T,
                               (np.dot(self.X_train, self.theta) - self.y_train)) / len(
                self.y_train)  # 利用最小二乘法计算梯度来算出均方误差
            print("iteration:%d  /  均方误差:%f" % (self.i, self.cost))  # 打印出迭代次数和cost的值
            self.ti_du = np.dot(2 * self.X_train.T, (np.dot(self.X_train, self.theta) - self.y_train)) / len(
                self.y_train)  # 算出梯度
            self.theta = self.theta - self.alpha * self.ti_du  # 利用梯度进行下降，改变theta的值
        return self.theta  # 返回拟合之后的theta
```



### 一周总结

- 本周一开始是感觉要写不完了，然后也花时间去想去做了，我只能说最后还是勉勉强强能完工啦！就是在刚学一样东西的时候是很蓝的啦，在入门只后就会感觉也没有开始的时候难哩！🤣

- flatten（）函数可以将数组降维！！！但是前提一定是要数组！！np.array()行！

### 存在问题

- 对python语法和三大库不熟悉，查起来和调用和调试起来十分折腾，但暂时还没想到什么方法来解决，只能说，多运用多锻炼吧！

### 下周规划

- 我我我我我要看吴恩达！！！！！！！！！！😋