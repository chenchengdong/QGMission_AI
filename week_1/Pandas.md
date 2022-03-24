# Pandas:

- 轻松导入Excel数据

```python
import pandas as pd					#导入pandas模块
df=pd.read_excel('data.xlsx')		#读取Excel
df1=df.head()					#读取前5条数据
print(df1)						#输出前五条数据
```



**Series对象**

- 什么是Series对象
  1. 类似一维数组，又一组数据以及与这组数据相关的标签（即索引）组成，或者仅有一组数据没有索引也可以创建一个简单的Series。Series可以存储整数，浮点数，字符串，python对象等多种类型的数据

![](D:\typora\typora_note\series.png)



- 创建一个Series对象----主要使用pandas的Series()方法，语法如下：

```python
s=pd.Series(data,index=index)
#data:--表示数据，支持字典，多维数组，标量值（只有大小没用方向的值 如s=pd.Series(5)）
#index: 表示行标签（索引）
#返回值：Series对象

#eg:在成绩表中添加一列“物理”成绩
import pandas as pd
s1=pd.Series([88,60,75])
print(s1)
#结果
0  88
1  60
2  75
```



- 手动设置Series索引

```python
import pandas as pd
s1=pd.Series([88,60,75],index=[1,2,3])
s2=pd.Series([88,60,75],index=['明日同学','高同学','七月流火'])
print(s1)
print(s2)
#结果
1   88
2   60
3   75
dtype:int64
明日同学   88
高同学     60
七月流火   75
dtype:int64
```



- Series的索引

```python
import pandas as pd
s1=pd.Series([88,60,75])
print(s1[0])
#结果
88
```



- Series标签索引

```python
import pandas as pd
s1=pd.Series([88,60,75],index=['明日同学','高同学','七月流火'])
print(s1['明日同学'])					#通过一个标签索引获取索引值
print(s1[['明日同学','七月流火']])			#通过多个标签索引获取索引值
#结果
88
明日同学    88
七月流火    75
```



- Series切片索引

```python
print(s1['明日同学':'七月流火'])
#结果
明日同学   88
高同学     60
七月流火   75

#通过位置切片1~4获取数据
s2=pd.Series([88,60,75,34,68])
print(s2[1:4])
#结果
1   60
2   75
3   34
```



- 获取Series索引和值

```python
import pandas as pd
s1=pd.Series([88,60,75])
print(s1.index)
print(s1.value)
#输出
RangeIndex(start=0,stop=3,step=1)
[88 60 75]
```





**DataFrame对象**

- 图解DateFrame对象，由行，列数据组成的表格。DateFrame既有行索引也有列索引，它可以看作是由Series对象组成的字典，不过这些Series对象共用一个索引

![](D:\typora\typora_note\DateFrame.jpg)

- 遍历DataFrame数据，输出成绩表的每一列数据

```python
import pandas as pd
data=[[110,105,99],[105,88,115],[109,120,130]]
index=[0,1,2]
columns=['语文','数学','英语']
#创建DataFrame数据
df=pd.DataFrame(data=data,index=index,columns=columns)
print(df)
#遍历DataFrame数据的每一列
for col in df.columns:
    series=df[col]
    print(series)
#结果
    语文  数学   英语
0	110	 105    99
1   105   88    115
2   109   120   130

0   110
1   115
2   109
Name: 语文，dtype:int64
        
0   105
1   88
2   120
Name:数学，dtype:int64

0   99
1   155
2   130
```



- 创建一个DataFrame对象---主要使用pandas的Dataframe（）方法

```python
pandas.DataFrame(data,index,columns,dtype,copy)
#data:表示数据，可以是ndarray数组、Series对象、列表、字典等
#index:表示行标签（索引）
#columns：列标签（索引）
#dtype:每一列数据的数据类型，其与python数据类型有所不同，如object数据类型对应的是python的字符型
#copy:用于复制数据
#返回值：DataFrame
```



- 下面通过两种方法创建DataFrame---(二维数组创建和通过字典创建)

  1. 通过二维数组创建

  ```python
  import pandas as pd
  #解决数据输出时列名不对齐的问题
  pd.set_option('display.unicode.east_asian_width',True)
  data=[[110,105,99],[105,88,115],[109,120,130]]
  columns=['语文','数学','英语']
  df=pd.DataFrame(data=data,columns=columns)
  print(df)
  #结果
      语文   数学    英语
  0   110   105     99
  1   105   88      115
  2   109   120     130
  ```

  1. 通过字典创建DataFrame

  ```python
  import pandas as pd
  #解决数据输出时列名不对齐的问题
  pd.set_option('display.unicode.east_asian_width',True)
  df=pd.DataFrame({
      '语文':[110,105,99]
      '数学':[105,88,115]
      '英语':[109,120,130]
      '班级':'高一7班'
  }，index=[0,1,2])
  print(df)
  #结果
   
       语文    数学    英语    班级
  0    110     105     109    高一7班
  1    105     88     120	    高一7班
  2    99      115    130     高一7班
  ```



- DataFrame重要属性和函数

- 属性

![](D:\typora\typora_note\属性.jpg)

- 函数

![](D:\typora\typora_note\函数.jpg)





### 导入外部数据

- 导入外部.xls和.xlsx文件----主要使用pandas的read_excel()方法，语法如下：

```python
pandas.read_excel(io,sheet_name=0,header=0,names=0,index_col=None,usecols=None,squeeze=False,dtype=None,shiprows=None,shipfooter=0)
#io:字符串，.xls或.xlsx文件路径或类文件对象
#sheet_name:None,字符串，整数，字符串列表或整数列表，默认值为0
#header:指定作为列名的行
#names:默认值为None，要使用的列名列表
#index_col:指定列为索引列，默认值为None,索引0是DataFrame的行标签
#usecols:int,list列表或字符串，默认值为None
	#如果为None,则解析所有的列
    #如果为int，则解析最后一列
    #如果为list列表，则解析列号列表的列
    #如果为字符串，则表示以逗号分隔的excel
#squeeze：布尔值，默认为False
#dtype:列的数据类型名称或字典，默认值为None
#skiprows:省略指定行数的数据，从第一行开始
#skipfooter:省略指定行数的数据，从尾部数的行开始
```



- 常规导入

```python
import pandas as pd
df=pd.read_excel('1月.xlsx')
df1=df.read()   
print(df1)          #输出前5条数据
```



- 导入指定的Sheet页

![](https://ccd123.oss-cn-guangzhou.aliyuncs.com/img/%E5%AF%BC%E5%85%A5%E6%8C%87%E5%AE%9A%E7%9A%84sheet%E9%A1%B5.jpg)

```python
import pandas as pd
df=pd.read_excel('1月.xlsx',sheet_name='莫寒')
df1=df.head()               #输出前5条数据
```



**通过行，列索引导入指定行，列数据**

DataFrame是二维数据结构，因此它既有行索引也有列索引，当导入Excel数据时，行索引会自动生成，如 0，1，2；而列索引则默认将第0行作为列索引（如上图A，B。。。。）。DataFrame行，列索引的示意图如图所示。

![](https://ccd123.oss-cn-guangzhou.aliyuncs.com/img/df6f97eb96ac739c7e4a5f65b90e039.jpg)



- 指定行索引导入Excel数据：

  如果指定行索引导入Excel数据，则需要设置index_col参数。（因为改变行的索引值是一列一列改的，索引要设置列的变化）下面将“买家会员名”作为行索引（位于第0列），导入Excel数据：程序代码如下：

  ```python
  import pandas as pd
  df1=pd.read_excel('1月.xlsx',index_col=0)      #‘买家会员名’为行索引
  df1=df1.head                                 #输出前5条数据
  ```

- 指定列索引导入excel数据，则需要设置header参数（因为改变列索引值是一行一行改的，索引要设置行的变化），主要代码如下：

  ```python
  df2=pd.read_excel('1月.xlsx',header=1)
  ```

- 如果将数字作为索引，可以设置header的参数为None,主要代码如下：

  ```python
  df3=pd.read_excel('1月.xlsx',header=None)        #列索引为数字
  ```



**导入指定列数据：**

- 导入第一列数据：

```python
import pandas as pd
df1=pd.read_excel('1月.xlsx',usecols=[0])       #导入第一列
df1.head()                                
```

- 如果导入多列，可以在列表中指定多个值：

```python
df2=pd.read_excel('1月.xlsx',usecols=[0,3])       #导入第一列和第四列
#也可以指定列的名称
df3=pd.read_excel('1月.xlsx',usecols=['买家会员名','宝贝标题'])
```



**导入csv文件：-----主要用pandas的read_csv（）方法**

```python
pandas.read_csv(filepath_or_buffer,sep=','delimiter=None,header='infer',names=None,index_col=None,usecols=None,dtype=None)
#filepath_or_buffer:字符串，文件路径，也可以是url连接
#sep、delimiter:字符串，分隔符
#header:指定作为列名的行，默认值为0，即取第一行的值为列名。数据为列名以外的数据，若数据不包括列名，则设置header=None
#names:默认值为None,要使用的列名列表
#index_col:指定列为索引列
#usecols:
#dtype:列的数据类型名称或字典，默认值为None
```



- 导入csv文件：

  ```python
  import pandas as pd
  df1=pd.read_csv('1月.csv',encoding='gbk')     #导入csv文件，并指定编码格式，excel一般默认编码格式为gbk,而py是utf-8,故要改
  df1=df1.head()           #输出前5条数据
  ```

- 导入txt文本文件----同样用read_csv()，不同的是需要指定sep参数

  ```python
  import pandas as pd
  df1=pd.read_csv('1月.txt',sep='\t',encoding='gbk')
  print(df.head())
  ```

- 导入html网页：

  ```python
  pandas.read_html(io,match='.+',flavor=None,header=None,index_col=None,encoding=None)
  #io：字符串，文件路径
  #match:正则表达式
  #flavor:解析器默认为lxml
  #header：指定列标题所在行
  #index_col：指定行标题对应的列，列表list为多重索引
  #encoding：编码格式
  #返回值：返回一个DataFrame
  ```

- 使用read_html（）时，首先要确认一下网页表格是否为table类型，检测元素时查看代码中是否含有表格标签<table>...<table>

- 样例，导入NBA球员薪资数据

```python
import pandas as pd
df=pd.DataFrame()
url_list=['网址']
for i in range(2,13):
    url='网址'%i
    url_list.append(url)
#遍历网页中的table读取网页表格数据
for url in url_list:
    df=df.append(pd.read_html(url),ignore_index=True)
#列表解析：遍历dataFrame第3列，以子字符串$开头
df=df[[x.startswith('$')for x in df[3]]]
df.to_csv('NBA.csv',header=['PK','NAME','TEAM','SALARY'],index=False)  #导出csv文件
```



**数据抽取：**

- 数据分析的过程中，并不是所有的数据都是我们想要的，此时可以抽取部分数据，主要使用DataFrame对象的loc属性和iloc属性，

  ```python
  #loc属性：以列名和行名作为参数，当只要一个参数时，默认时行名，即抽取整行数据，包括所有列
  
  #iloc属性:以行和列位置索引（即0，1，2，。。。）作为参数，0表示第一行，1表示第二行，一次类推，当只有一个参数时，默认时行索引，即抽取整行数据，包括所有列。如果抽取第一行数据，则df.iloc[0]
  ```

- 抽取一行数据

  ```python
  import pandas as pd
  data=[[110,105,99],[105,88,115],[109,120,130],[112,115]]
  name=['明日','七月流火','高员员','二月二']
  columns=['语文','数学','英语']
  df=pd.DataFrame(data=data,index=name,columns=columns)
  df1=df.loc['明日']
  ```

  ![](https://ccd123.oss-cn-guangzhou.aliyuncs.com/img/0aa00a915c7e0ee5fb539554ec900b8.jpg)

- 这里一个是返回了一行，只不过它是要返回dataframe类型,所以在返回一行时，它又行列变换了一下

- 抽取多行数据

  ```python
  df1=df.loc[['明日','高员员']]
  df1=df1.iloc[[0,2]]
  ```

  ![](https://ccd123.oss-cn-guangzhou.aliyuncs.com/img/20220323151854.png)

- 连续抽取多行数据

```python
print(df.loc['明日':'二月二'])    #从明日到二月二
print(df.loc[:'七月流火':])      #从第一行到七月流火
```



- 抽取指定列数据:

  ```python
  import pandas as pd
  data=[[110,105,99],[105,88,115],[109,120,130],[112,115]]
  name=['明日','七月流火','高员员','二月二']
  columns=['语文','数学','英语']
  df=pd.DataFrame(data=data,index=name,columns=columns)
  df1=df['语文']
  ```

- 抽取指定列数据

- 按条件抽取数据：

  ```python
  import pandas as pd
  data=[[110,105,99],[105,88,115],[109,120,130],[112,115]]
  name=['明日','七月流火','高员员','二月二']
  columns=['语文','数学','英语']
  df=pd.DataFrame(data=data,index=name,columns=columns)
  df1=df.loc[(df['语文']>105)&(df['数学']>68)]
  ```



- 按列增加数据

  ```python
  import pandas as pd
  data=[[110,105,99],[105,88,115],[109,120,130],[112,115]]
  name=['明日','七月流火','高员员','二月二']
  columns=['语文','数学','英语']
  df=pd.DataFrame(data=data,index=name,columns=columns)
  df['物理']=[88,79,60,50]
  ```



- 使用loc属性增加一列物理成绩

```python
df.loc[:'物理']=[88,79,60,50]    #有问题
```



- 在指定位置插入一列

  ```python
  wl=[88,79,60,50]
  df.insert(1,'物理',wl)
  ```

- 按行增加数据   1.一行用loc属性  2.多行用字典结合append()方法实现

```python
df.loc['钱多多']=[100,120,99]         #有问题
```



- 增加多行数据

```python
df_insert=pd.DataFrame({'语文':[100,123,138],'数学':[99,142,60],'英语':[98,139,99]},index=['钱多多','童年','无名'])
df1=df.append(df_insert)
```



- 修改数据:

- 修改列标题:

```python
df.columns=['语文','数学（上）','英语']
```

- 修改行标题

```python
df.index=list('1234')
```



- 修改数据----loc和iloc属性
- 修改整行数据--例如修改明日同学各科成绩

```python
df.loc['明日']=[120,115,109,98]
```

- 修改整列数据

```python
df.loc[:'语文']=[115,106,120,113,120,123,111]
```

- 修改某一数据

```python
df.loc['明日','语文']=150
```



- 删除数据----主要用dataframe对象的drop()方法，语法如下：

```python
DataFrame.drop(labels=None,axis=0,index=None,columns=None,level=None,inplace=False,error='raise')
#labels:表示行标签或列标签
#axis：axis=0,表示按行删除；axis=1,表示按列删除；默认值为0
#index:删除行，默认值为None
#columns:删除列，默认值为None
#level:针对有两级索引的数据。level=0,表示按第一级索引删除整行，level=1表示按第二级索引删除整行，默认值为None
#inplace:可选参数，对原数组做出修改并返回一个新数组。默认值为False,如果值为True,那么原数组直接就被替换
#参数值为ignore或raise，默认值为raise,如果值为ignore(忽略)，则取消错误
```



- 删除行、列数据

```python
df.drop(['数学'],axis=1,inplace=True)            #删除某列
df.drop(columns='数学',inplace=True)             #删除columns为数学的列
df.drop(labels='数学',axis=1,inplace=True)      #删除标签为数学的列
df.drop(['明日','二月二'],inplace=True)          #删除某行
df.drop(index='明日',inplace=True)            #删除index为“明日”的行
df.drop(labels='明日',axis=0,inplace=True)    #删除行标签为“明日”的行
```



- 删除特定的行

```python
df.drop(index=df[df['数学'].isin([88])].index[0],inplace=True)  
#删除“数学”成绩中包含88的行
df.drop(index=df[df['语文']<110].index[0],inplace=True)
#删除“语文”成绩中小于110的行
```



- 数据清洗:
- 数据缺失值查看与处理：缺失值是值由于某种原因导致数据为空，这种情况一般有不处理、删除、填充\替换、插值（以均值\中位数\众数等填补）这4中处理方式
- 缺失值查看--首先我们要找到缺失值，主要使用DataFrame对象的info()方法

```python
import pandas as pd
df=pd.read_excel("C:\\Users\\chenchengdong\\Downloads\\热线受理统计信息（更新到2021年）.xlsx")
print(df)
print(df.info())
```



- 判断数据是否缺失还可以使用isnull()和notnull()的方法

```python
print(df.isnull())
print(df.notnull())
```



- 缺失值的删除处理--通过前面的判断得知数据缺失的情况，下面将缺失值删除，主要使用dropna()方法，该方法用于删除含有缺失值的行，主要代码如下：

```python
df1=df.dropna()
```

![](https://ccd123.oss-cn-guangzhou.aliyuncs.com/img/20220323173130.png)

- 缺失值的填充处理：如果比例高于30%可以选择放弃这个指标，做删除处理，低于30%尽量不要删除，而是选择将这部分数据填充，一般以0，均值，众数填充，dataframe对象中的fillna()函数可以实现快速填充该缺失值，pad/ffill表示用前一个非缺失值去填充该缺失值，backfill/bfill表示用下一个非缺失值填充该缺失值；none用于指定一个值去替换缺失值
- 样例：将第一列“NaN”的数据填充为无

```python
df['热线受理统计信息-20211215']=df['热线受理统计信息-20211215'].fillna('无')
```



- 重复值处理----对于数据中存在的重复数据，包括重复的行或者几行中某几列的值重复一般做删除处理，主要使用DataFrame对象的drop_duplicates()方法：
- 判断每一"行"数据是否重复（完全相同），主要代码如下：

```python
df1.duplicated()
```

- 去除全部的重复数据

```python
df1.drop_duplicates()
#去除指定列的重复数据
df1.drop_duplicates(['买家会员名'])
#保留重复行中的最后一行
df1.drop_duplicates(['买家会员名'],keep='last')
```





- 对series对象重新设置索引

```python
s1=pd.Serise([88,60,75],index=[1,2,3])
print(s1)
printf(s1.reindex([1,2,3,4,5]))
#新出现的索引的值也可以不用NaN来代替
s1.reindex([1,2,3,4,5],fill_value=0)
```



- 对DataFrame对象重新设置索引，用reindex()方法来修改行索引和列索引

```python
import pandas as pd
data=[[110,105,99],[105,88,115],[109,120,130]]
index=['mr001','mr003','mr005']
columns=['语文','数学','英语']
df=pd.DateFrame(data=data,index=index,columns=columns)
print(df)
#重新设置行索引
df.reindex(['mr001','mr002','mr003','mr004','mr005'])
#重新设置列索引
df.reindex(columns=['语文','物理','数学','英语'])
#一起改
df.reindex(index=['mr001','mr002','mr003','mr004','mr005'],columns=['语文','物理','数学','英语'])
```

- 设置某列为行索引

```python
df2=df.set_index(['买家会员名'])
```



数据清洗后重新设置连续的行索引

```python
df2=df.dropna().reset_index(drop=True)
```



- 数据排序

```python
DataFrame.sort(by,axis=0,ascending=True,inplace=False,kind='quicksort',na_position='last',ignore_index=False)
#by:要排序列表名
#axis:轴，0表示行，1表示列
#ascending:升序或降序排序
#inplace:
#na_position:
#
#
```



- 按一列数据排序

```python
excelFile='mrbook.xlsx'
df=pd.DataFrame(pd.read_excel(excelFile))
#按”销量“列排序
df=df.sort_value(by='销量',ascending=False)
#多列数据排序
df1=df.sort_value(by=['图书名称','销量'])
#对统计结果进行排序

#按行进行排序
df=dfrow.sort_values(by=0,ascending=True,axis=1)
```



- 数据排名

```python
#顺序排名

#平均排名

#最小值排名

#最大值排名
```

