### Matplotlib可画的图：折线图，柱状图，直方图，饼形图，散点图，双y周可视化数据分析图表，堆叠柱形图，渐变饼形图，等高线图等



- 绘制体温折线图：

```python
import pandas as pd
import matplotlib.pyplot as plt
df=pd.read_excel('体温。xls')     #导入excel文件
#折现图
x=df['日期']       #x轴数据
y=df['体温']        #y轴数据
plt.plot(x,y)      
```



- 颜色设置

![](https://ccd123.oss-cn-guangzhou.aliyuncs.com/img/1c7b9707563e5ac2f813391e86cf605.jpg)

- 线条设置

![](https://ccd123.oss-cn-guangzhou.aliyuncs.com/img/90f9b2b96f739c6931a635d7f1e5c2d.jpg)

- 标记样式

![](https://ccd123.oss-cn-guangzhou.aliyuncs.com/img/1c0a640d2f05a7b4671429e079e90a6.jpg)

- 样例

```python
plt.plot(x,y,color='m',linestyle='-',marker='o',mfc='w')
```

![](https://ccd123.oss-cn-guangzhou.aliyuncs.com/img/baeece0e730d4a0f1cbc93c511da169.jpg)



- 设置画布

```python
matplotlib.pyplot.figure(num=None.figsize=None,dpi=None,facecolor=None,edgecolor=None,frameon=True)
```

![](https://ccd123.oss-cn-guangzhou.aliyuncs.com/img/4ca79d9267e9c2f7afc3433b1465b2f.jpg)



- 设置x轴，y轴标题

```python
plt.xlabel('2020年2月')       #x轴标题
plt.ylabel('基础体温')        #y轴标题
```

![](https://ccd123.oss-cn-guangzhou.aliyuncs.com/img/20220323204158.png)



- 坐标轴刻度

```python
plt.xticks(range(1,15,1))

plt.yticks([35.4,35.6,35.8......])
```



- 坐标轴范围

```python
plt.xlim(1,14)

plt.ylim(35,45)
```

  

- 网格线

```python
plt.grid(color='0.5',linestyle='--',linewidth=1)
```



- 添加文本标签

```python
matplotlib.pyplot.text(x,y,s,fontdict=None,withdash=False,**kwargs)
```

![](https://ccd123.oss-cn-guangzhou.aliyuncs.com/img/b31fc8362e3e2484568e4e096243291.jpg)



- 设置标题和图例
- 图标标题

```python
matplotlib.pyplot.title(label,fondict=None,loc='center',pad=None,**kwargs)
```

![](https://ccd123.oss-cn-guangzhou.aliyuncs.com/img/e5e91c2660896acec3ff890937baeae.jpg)

- 图表图例

```python
plt.legend()                    #自动显示图例
plt.legend('基础体温')          #手动添加图例
#设置图例显示位置
plt.legend(('基础体温'),loc='upper right',fontsize=10)
```

![](https://ccd123.oss-cn-guangzhou.aliyuncs.com/img/e18e8d1b7e1d08c51ac47041c1378cd.jpg)

- 调整图标与画布边缘间距

```python
plt.subplots_adjust(left=None,bottom=None,right=None,top=None,wspace=None,hspace=None)
```

![](https://ccd123.oss-cn-guangzhou.aliyuncs.com/img/5ba4ff0164e7284b0bc5b0e547896b3.jpg)

**上述参数表示画布，以画布为出发点，左下角为出发点**

- 其它设置
- 坐标轴的刻度线

```python
ply.tick_params(bottom=False,left=True,right=True,top=True)
```

- 设置x轴y轴的刻度线显示方向，其中in表示向内，out表示向外，inout表示在中间，默认刻度线向外

```python
plt.reParams['xtick.direction']='in'
plt.reParams['ytick.direction']='in'
```

![](https://ccd123.oss-cn-guangzhou.aliyuncs.com/img/82747966da65c219ade4860a39c3ecf.jpg)

- 绘制折线图
- 绘制柱形统计图

```python
matplotlib.pyplot.bar(x,height,width,bottom=None,*align='center',data=None,**kwargs)
```

![](https://ccd123.oss-cn-guangzhou.aliyuncs.com/img/3b431d5e12cc3e260e96cf33f175203.jpg)

```python
import matplotlib.pyplot as plt
x=[1,2,3,4,5]
height=[10,20,30,40,50,60]
plt.bar(x,height)
```

- 多柱形图

- 绘制直方图

```python
import matplotlib.pyplot as plt
x=[22,87,5,43,56,73,55,54,11,20,51,5,79,31,27]
plt.hist(x,bins=[0,25,50,75,100])
```

![](https://ccd123.oss-cn-guangzhou.aliyuncs.com/img/ec0493a3371adf84cf08aae39a44ce7.jpg)



- 绘制饼形图

![](https://ccd123.oss-cn-guangzhou.aliyuncs.com/img/99a1fb31a4a5ed7f60ae28f904e24cd.jpg)

```python
import matplotlib.pyplot as plt
x=[2,5,12,70,2,9]
plt.pie(x,autopct='%1.1f%%')
```



- 分裂饼形图：关键代码如下

```python
explode=(0.1,0,0,0,0,0,0,0,0,0)
```



- 环形图:关键参数

```python
wedgeprops={'width':0.4,'edgecolor':'k'}
```



- 绘制散点图

![](https://ccd123.oss-cn-guangzhou.aliyuncs.com/img/06f4ac228753de218cf51a84adc0721.jpg)

```python
import matplotlib.pyplot as plt
x=[1,2,3,4,5,6]
y=[19,24,37,43,55,68]
plt.scatter(x,y)
```



- 绘制面积图
- ![](https://ccd123.oss-cn-guangzhou.aliyuncs.com/img/4c92e3f1a038d77be5b2d728024da7e.jpg)

```python
import matplotlib.pyplot as plt
x=[1,2,3,4,5,6]
y1=[6,9,5,8,4]
y2=[3,2,5,4,3]
y3=[8,7,8,4,3]
y4=[7,4,6,7,12]
plt.stackplot(x,y1,y2,y3,y4,colors=['g','c','r','b'])
```

