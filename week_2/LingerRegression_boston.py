import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.preprocessing import MinMaxScaler

plt.rcParams["font.sans-serif"]="SimHei"   #修改字体的样式可以解决标题中文显示乱码的问题
plt.rcParams["axes.unicode_minus"]=False  #该项可以解决绘图中的坐标轴负数无法显示的问题

class LingerRegression_boston:

    def __init__(self):
        self.df = pd.read_csv('housing.csv', encoding='gbk')  # 创建对象时自动读取housing文件
        self.X = 0  # 创建X样本 属性
        self.y = 0  # 创建y样本 属性
        self.X_train = 0  # 创建X_train 属性
        self.y_train = 0  # 创建y_train 属性
        self.X_test = 0  # 创建X_test  属性
        self.y_test = 0  # 创建y_test 属性
        self.y_predict = 0  # 创建y_predict预测值 属性
        self.theta = 0  # 创建 系数θ 属性
        self.m = 0  # 创建抽取特征量个数  属性
        self.list1 = 0  # 创建 抽取特征量的矩阵 属性
        self.index1 = 0  # 创建用于删除列的的标签1 属性
        self.index2 = 0  # 创建用于删除列的标签2 属性
        self.alpha = 0.1  # 创建学习率 默认为0.1 属性
        self.iter_numbers = 1000  # 创建迭代次数  默认为1000 次属性
        self.cost = 0  # 损失值       属性
        self.i = 0  # 遍历变量     属性
        self.ti_du = 0  # 创建梯度    属性
        self.Normalizing()  # 调用标准化函数

    def Normalizing(self):  # 标准化
        scaler = MinMaxScaler().fit(self.df)
        self.df = pd.DataFrame(scaler.transform(self.df))

    def separate(self, list1, m):  # 将数据拆分成一些训练集，测试集
        self.list1 = list1
        self.m = m
        self.y = self.df.iloc[:, 13]
        self.X = self.df.iloc[:, self.list1]  # 抽取选择的特征量的列
        self.X.insert(0, '添加', np.ones(506))  # 先创建一个全是1的一维数组， 然后在每个X样本集前加一个1
        self.theta = np.mat(np.ones(self.m + 1)).T  # 创建一个m+1个特征量对应的向量，因为在每个样本集前加了1,用于点乘
        self.y_train = np.mat(self.y[:401]).T  # 创建y训练集 由于后面需要用到点乘，故将训练集转变为向量，转置是因为行向量转化为列向量
        self.index1 = self.X.iloc[401:, :].index.tolist()  # 将需要删除的下标变成一个list
        self.X_train = self.X.drop(labels=self.index1)  # dataframe 对象抽取前401行 创建X训练集
        self.y_test = np.mat(self.y[401:]).T  # 创建y测试集,由于后面需要用到点乘，故将测试集转变为向量，转置是因为行向量转化成列向量
        self.index2 = self.X.iloc[:401, :].index.tolist()
        self.X_test = self.X.drop(labels=self.index2)  # 创建X测试集

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

    def getPredict(self):
        self.y_predict = np.dot(self.X_test, self.theta)  # 算出y_predict的值
        return self.y_predict  # 返回

    def ModifyAlpha(self, alpha):
        self.alpha = alpha  # 修改学习率

    def MpdifyIter_n(self, iter_numbers):
        self.iter_numbers = iter_numbers  # 修改迭代次数

    def drawScatter(self):  # 将拟合的预测值和测试值的散点图画出来  实例方法
        self.y_predict = np.dot(self.X_test, self.theta)  # 要先获得预测值，以免在调用这个实例方法前没有调用getPredict
        plt.figure(figsize=(20, 10))  # 设置画布大小
        plt.scatter(np.arange(0, self.X_test.shape[0]), np.array(self.y_predict).flatten(),label='预测值', c='r')
        plt.scatter(np.arange(0, self.X_test.shape[0]), np.array(self.y_test).flatten(),label='真实值', c='g')
        plt.title('房价预测值与真实值散点图',size=20)
        plt.xlabel('样本个数',size=20)
        plt.ylabel('房价（经过标准化）',size=20)
        plt.legend(['预测值','真实值',],loc='best',fontsize=15)
        plt.xticks(size=15)
        plt.yticks(size=15)
        plt.ylim(0, 1)
        plt.show()

    def drawPlot(self):  # 画折线图
        self.y_predict = np.dot(self.X_test, self.theta)  # 要先获得预测值，以免在调用这个实例方法前没有调用getPredict
        plt.figure(figsize=(20, 10))
        plt.plot(np.arange(0, self.X_test.shape[0]), np.array(self.y_predict).flatten(),label='预测值', c='r',marker='p',ms=8)
        plt.plot(np.arange(0, self.X_test.shape[0]), np.array(self.y_test).flatten(), label='真实值',c='g',marker='.',ms=8)
        plt.grid(c='k', linestyle='--', linewidth=1, axis='y')
        plt.title('房价预测值与真实值曲线',size=20)
        plt.xlabel('样本个数',size=20)
        plt.ylabel('房价（经过标准化）',size=20)
        plt.legend(['预测值','真实值',],loc='best',fontsize=15)
        plt.xticks(size=15)
        plt.yticks(size=15)
        plt.ylim(0, 1)
        plt.show()

    def PrintPredict(self):  # 将测试值打印出来
        self.y_predict = np.dot(self.X_test, self.theta)  # 要先获得预测值，以免哉调用这个实例方法前没有调用getPredict
        print("预测值：")
        print("****************")
        print("****************")
        print()
        print(self.y_predict)
        print("实际值：")
        print("****************")
        print("****************")
        print()
        print(self.y_test)
