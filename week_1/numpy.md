# numpy

### 创建简单的数组

**创建一个数组**

```python
import numpy as np
n1=np.array([1,2,3])    #创建一个简单的一维数组
n2=np.array([0.1,0.2,0.3]) #创建一个包含小数的一维数组
n3=np.array([[1,2],[3,4]]) 	#创建一个包含小数的一维数组

```

![](D:\typora\typora_note\numpy_easy.jpg)



**为数组指定数据类型**

```python
import numpy as np
list=[1,2,3]
#创建浮点型数组
n1=np.array(list,dtype=np.float)

```



**数组的复制**

```python
import numpy as np	
n1=np.array([1,2,3])		#创建数组
n2=np.array(n1,copy=True)	#复制数组	
n2[0]=3				#修改数组中的第一个元素为3
n2[2]=1				#修改数组中的第三个元素为1
```



**通过ndmin参数控制最小维数**

```python
nd1=[1,2,3]
nd2=np.array(nd1,ndmin=3)  #三维数组

#输出结果
[[[1,2,3]]]

```



### 不同方式创建数组

**创建指定维度和数据类型未初始化的数组**

```python
import numpy as np
n=np.empty([2,3])

```



**创建指定维度（以0填充）的数组**

```python
import numpy as np
n=np.zeros(3)
#输出结果
[0.0.0.]
```



**创建指定维度为（以1填充）的数组**

```python
import numpy as np
n=np.ones(3)
#输出结果
[1.1.1.]
```



**创建指定维度和类型的数组并以指定值填充**

```python
import numpy as np
n=np.full((3,3),8)
#输出结果
[[8 8 8]
[8 8 8]
[8 8 8]]

```



### 从数组范围创建数组



**通过arange（）函数创建数组**

```python
import numpy as np
n=np.arange(1,12,2)
#输出结果
[1 3 5 7 9 11]

```



**利用linspace()函数创建等差数列**

```python
import numpy as np
n1=np.linspace(7500,10000,6)
#输出结果
[7500. 8000. 8500. 9000. 9500. 10000.]
```





**使用logspace()函数创建等比数列**

```python
import numpy as np
n=np.logspace(0,63,64,base=2,dtype='int')

```

![](D:\typora\typora_note\logspace.jpg)





### 生成随机数组



**rand()函数**

```python
import numpy as np
n=np.random.rand(5)
print("随机生成0-1的一维数组")
print(n)
n1=np.random.rand(2,5)
print("随机生成0-1的二维数组")
print(n1)

```

![](D:\typora\typora_note\rand.jpg)



**randn()函数---用于从正态分布中返回随机生成的数组**

```python
import numpy as np
n1=np.random.randn(5)
print("随机生成满足正态分布的一维数组")
print(n1)
n2=np.random.randn(2,5)
print("随机生成满足正态分布的二维数组")
print(n2)

```

![](D:\typora\typora_note\randn.jpg)

****



**randint()函数---在一定范围内生成随机数组**

```python
import numpy as np
n1=np.random.randint(1,3,10)
print("随机生成10个1-3且不包括3的整数：")
print(n1)
n2=np.random.randint(5,10)
print("size数组大小为空随机返回一个整数")
print(n2)
n3=np.random.randint(5,size=(2,5))
print("随机生成5以内的二维数组")
print(n3)
```

![](D:\typora\typora_note\randint.jpg)



**normal()函数--生成正态分布的随机数组**

```python
import numpy as np
n=np.random.normal(0,0.1,10)

```

![](D:\typora\typora_note\normal.jpg)



### 从已有的数组中创建数组



**asarray()函数---用于创建数组（与array（）函数类似）**

```python
import numpy as np
n1=np.asarray([1,2,3])				#通过列表创建数组
n2=np.asarray([(1,1),(1,2)])		#通过列表的元组创建数组
n3=np.asarray((1,2,3))				#通过元组创建数组
n4=np.asarray(((1,1),(1,2),(1,3)))	#通过元组的元组创建数组
n5=np.asarray(([1,1],[1,2]))		#通过元组的列表创建数组
print(n1)
print(n2)
print(n3)
print(n4)
print(n5)

```

![](D:\typora\typora_note\asarray.jpg)



**fromiter()函数---用于可迭代对象中建立数组对象**

```python
import numpy as np
iterable=(x*2 for x in range(5))
n=np.fromiter(iterable,dtype='int')
print(n)
#输出结果
[0 2 4 6 8]

```



**empty_like()函数--用于创建一个与给定数组具有相同维度和数据类型且未初始化的数组**

```python
import numpy as np
n=np.empty_like([[1,2],[3,4]])
print(n)
#输出结果
[[0 0]
[0 0]]

```



**zeros_like()函数--用于创建一个与给定数组维度和数据类型相同，并以0填充的数组**

```python
import numpy as np
n=np.zeros_like([[0.1,0.2,0.3],[0.4,0.5,0.6]])
print(n)
#输出结果
[[0. 0. 0.]
[0. 0. 0.]]

```



**ones_like()函数--用于创建一个与给定数组维度和数据类型相同，并以1填充的数组**

```python
import numpy as np
n=np.ones_like([[0.1,0.2,0.3],[0.4,0.5,0.6]])
print(n)
#输出结果
[[1. 1. 1.]
[1. 1. 1.]]
```



**full_like()函数--用于创建一个与给定数组维度和数据类型相同，并以指定值填充的数组**

```python
import numpy as np
a=np.arange(6)		#创建一个数组
print(a)	
n1=np.full_like(a,1)	#创建以恶搞与数组a维度和数据类型相同的数组，以1填充
n2=np.full_like(a,0.2)	#创建以恶搞与数组a维度和数据类型相同的数组，以0.2填充
#创建一个与数组a维度和数据类型相同的数组，以0.2填充，浮点型
n3=np.full_like(a,0.2,dtype='float')
print(n1)
print(n2)
print(n3)

#输出结果
[1 1 1 1 1 1]
[0 0 0 0 0 0]
[0.2 0.2 0.2 0.2 0.2 0.2]
```



### 数组的基本操作

**数据类型**

![](D:\typora\typora_note\data_series.jpg)

```python
import numpy as np
np.int8(3.141)
#输出结果
3
np.float64(8)
#输出结果
8.0
#在创建ndarray数组时，可以直接指定数值类型
a=np.arange(8,dtype=float)
#结果
[0. 1. 2. 3. 4. 5. 6. 7.]
```



### 数组运算



**加法运算**

```python
import numpy as np
n1=np.array([1,2])
n2=np.array([3,4])
print(n1-n2)		#减
print(n1*n2)		#乘
print(n1/n2)		#除
print(n1+n2)		#加
print(n1**n2)		#幂运算
#结果
[-2 -2]
[3 8]
[0.33333333 0.5      ]
[4 6]
[1 16]
```



**数组标量运算**

```python
import numpy as np
n1=np.linspace(7500,10000,6,dtype='int')
print(n1)
print(n1/1000)			#米转换成千米
#输出结果
[7500 8000 9000 9500 10000]
[7.5 8. 8.5 9. 9.5 10.]
```



### 数组的索引和切片

**索引**

```python
import numpy as np
n1=np.array([[1,2,3],[4,5,6]])
print(n1[1][2])
#输出结果
6
```



**切片**

**特点**

1. 索引是左闭右开区间
2. 当没有start参数时，代表从0开始取数

![](D:\typora\typora_note\切片.jpg)

![切片2](D:\typora\typora_note\切片2.jpg)



**二维数组索引**

```python
import numpy as np
#创建3行4列的二维数组
n=np.array([[0,1,2,3],[4,5,6,7],[8,9,10,11]])
print(n[1])			#输出第2行元素
print(n[1,2])		#输出第2行第3列
print(n[-1])		#输出倒数第1行
#输出结果
[4 5 6 7]
6
[8 9 10 11]
```



**二维数组切片**

```python
import numpy as np
#创建3行3列的二维数组
n=np.array([[1,2,3],[4,5,6],[7,8,9]])
print(n[:2,1:])		#输出第一行致第三行（不包括第三行）的第二列至最后一列
print(n[1,:2])		#输出第二行第一列到第三列（不包括第三列）的元素
print(n[:2,2])		#输出第一行至第三行（不包括第三行）的第三列的元素
print(n[:,:1])		#输出所有行的第一列至第二列
#输出结果
[[2 3]
[5 6]]

[4 5]

[3 6]

[[1]
[4]
[7]]
```



![](D:\typora\typora_note\二维数组.jpg)



### 数组重塑

**一维数组重塑**

```python
import numpy as np
n=np.arange(6)
print(n)
n1=n.reshape(2,3)
print(n1)
#输出结果
[0 1 2 3 4 5]
[[0 1 2]
[3 4 5]]
```



**多维数组重塑**

```python
import numpy as np
n=np.array([[0,1,2],[3,4,5]])
print(n)
n1=n.reshape(3,2)
print(n1)
#输出结果
[[0 1 2]
[3 4 5]]

[[0 1]
[2 3]
[4 5]]

```



**数组转置**

```python
n=np.arange(24).reshape(4,6)	#创建4行6列二维数组
print(n)
print(n.T)		#T属性行列转置
```

![](D:\typora\typora_note\矩阵转置.jpg)

**transpose()函数也可以实现数组转置**

```python
n=np.array([['A',100],['B',200],['C',300],['D',400],['E',500]])
print(n.transpose())		#行列转置
#结果
[['A' 'B' 'C' 'D' 'E']
['100' '200' '300' '400' '500']]
```



### 数组的增、删、改、查

**数组的增加**

```python
import numpy as np
#创建二维数组
n1=np.array([[1,2],[3,4],[5,6]])
n2=np.array([[10,20],[30,40],[50,60]])
print(np.hstack((n1,n2)))		#水平方向增加数据
print(np.vstack((n1,n2)))		#垂直方向增加数据
#结果
[[1 2 10 20]
[3 4 30 40]
[5 6 50 60]]

[[1 2]
[3 4]
[5 6]
[10 20]
[30 40]
[50 60]]

```



**数组的删除--主要用delete()方法**

```python
import numpy as np
#创建二维数组
n1=np.array([[1,2],[3,4],[5,6]])
print(n1)
n2=np.delete(n1,2,axis=0)		#删除第3行
n3=np.delete(n1,0,axis=1)		#删除第1列
n4=np.delete(n1,(1,2),0)		#删除第2行和第3行
print('删除第3行后的数组'：'\n',n2)
print('删除第1列后的数组'：'\n',n3)
print('删除第2行和第3行后的数组'：'\n',n4)
#结果
[[1 2]
[3 4]
[5 6]]

[[1 2]
[3 4]]

[[2]
[4]
[6]]

[[1 2]]
```



**数组的修改**

```python
#创建二维数组
n1=np.array([[1,2],[3,4],[5,6]])
print(n1)
n1[1]=[30,40]
n1[2][1]=88
print('修改后的结果':,'\n',n1)
#结果
[[1 2]
[3 4]
[5 6]]

[[1 2]
[30 40]
[5 88]]

```



**数组的查询---numpy.where(condition,x,y)**

1. 满足condition返回参数x，否则返回y

```python
n1=np.arange(10)
print(n1)
print(np.where(n1>5,2,0))
#结果
[0 1 2 3 4 5 6 7 8 9]
[0 0 0 0 0 0 2 2 2 2]
```



### NumPy矩阵的基本操作

**创建矩阵**

```python
import numpy as np
a=np.mat('5 6;7 8')
b=np.mat([[1,2],[3,4]])
print(a)
print(b)
n1=np.array([[1,2],[3,4]])
print(n1)
#结果
[[5 6]
[7 8]]

[[1 2]
[3 4]]

[[1 2]
[3 4]]
```

1. mat()函数创建矩阵类型，array()函数创建数组类型，而用mat()函数创建的矩阵才能进行一些线性代数的操作

**创建一个3x3的矩阵 2x4矩阵**

```python
data1=np.mat(np.zeros((3,3)))
print(data1)
data2=np.mat(np.ones((2,4)))
print(data2)
#结果
[[0. 0. 0.]
[0. 0. 0.]
[0. 0. 0.]]

[[1. 1. 1. 1.]
[1. 1. 1. 1.]]


```



**创建对角矩阵**

```python
data1=np.mat(np.eye(2,2,dtype=int))		#创建2x2对角矩阵
print(data1)
data1=np.mat(np.eye(4,4,dtype=int))		
print(data1)
a=[1,2,3]
data=np.mat(np.diag(a))   #对角线1、2、3矩阵
#结果
[[1 0]
[0 1]]

[[1 0 0 0]
 [0 1 0 0]
 [0 0 1 0]
 [0 0 0 1]]

[[1 0 0]
 [0 2 0]
 [0 0 3]]
```



**矩阵运算**

```python
import numpy as np
data1=np.mat([[1,2],[3,4],[5,6]])
data2=np.mat([1,2])
print(data1+data2)		#加法运算    not in 线代
print(data1-data2)		#减法运算    not in 线代
print(data1/data2)		#矩阵除法运算 not in 线代
print(data1*data2)		#矩阵乘法运算 与线代相同
#结果
[[2 4]
[4 6]
[6 8]]

[[0 0]
[2 2]
[4 4]]

[[1. 1.]
[3. 2.]
[5. 3.]]

[[7 10]
[15 22]
[23 34]]

```

![](D:\typora\typora_note\matrix.jpg)



**矩阵之间的相乘运算**

```python
import numpy as np
n1=np.mat('1 3 3;4 5 6;7 12 9')		#创建矩阵
n2=np.mat('2 6 6;8 10 12;14 24 18')			
print('矩阵相乘结果为：\n',n1*n2)			#矩阵相乘
print('矩阵对应元素相乘结果为: \n',np.multiply(n1,n2))
#结果
[[68 108 96]
[132 218 192]
[236 378 348]]

[[2 18 18]
[32 50 72]
[98 288 162]]

```



**矩阵转换**

**矩阵转置**

```python
import numpy as np
n1=np.mat('1 3 3;4 5 6;7 12 9')
print('矩阵转置结果为:\n',n1.T)
#结果
[[1 4 7]
[3 5 12]
[3 6 9]]
```



**矩阵求逆**

```python
import numpy as np
n1=np.mat('1 3 3;4 5 6;7 12 9')			#创建矩阵
print('矩阵的逆矩阵结果为:\n',n1.l)  	#逆矩阵
#结果
[[-0.9	0.3	0.1]
[0.2	-0.4	0.2]
[0.43333333	0.3	-0.23333333]]
```

**NumPy数学运算函数**

![](D:\typora\typora_note\NUMPY_fun.jpg)

**NumPy统计分析函数**

![](D:\typora\typora_note\numpy_stasticfun.jpg)

**几个常用的统计函数**

1. sum()函数

```python
import numpy as np
n=np.array([[1,2,3],[4,5,6],[7,8,9]])
print('对数组元素行求和：')
print(n.sum())
print('对数组元素按行求和：')
print(n.sum(axis=0))
print('对数组元素按列求和：')
print(n.sum(axis=1))
#结果
45

[12 15 18]

[6 15 24]
```

![](D:\typora\typora_note\array_simple.jpg)



**数组的排序**

**sort()函数**

```python
import numpy as np
n=np.array([[4,7,3],[2,8,5],[9,1,6]])
print('数组排序：')
print(np.sort(n))
print('按行排序：')
print(np.sort(n,axis=0))
print('按列排序：')
print(np.sort(n,axis=1))
#结果
[[3 4 7]
[2 5 8]
[1 6 9]]

[[2 1 3]
[4 7 5]
[9 8 6]]

[[3 4 7]
[2 5 8]
[1 6 9]]
```



**argsort()函数**

```python
x=np.array([4,7,3,2,8,5,1,9,6])
print('升序排序后的索引值')
y=np.argsort(x)
print(y)
print('排序后的顺序重构')
print(x[y])
#结果
[6 3 2 0 5 8 1 4 7]

[1 2 3 4 5 6 7 8 9]
```



**lexsort()函数**

用于对多个序列进行排序。可以把它当作是对电子表格进行排序，每一列代表一个序列，排序时优先照顾靠后

```python
import numpy as np
math=np.array([101,109,115,108,118,118])
en=np.array([117,105,118,108,98,109])
total=np.array([621,623,620,620,615,615])
sort_total=np.lexsort((en,math,total))
print('排序后的索引值')
print(sort_total)
print('通过排序后的索引获取排序后的数组：')
print(np.array([[len[i],math[i],total[i]]for i in sort_total]))
```

