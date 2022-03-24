# Python 语法

**多行语句**

- 如果语句很长，可以使用反斜杠\来实现多行语句

```python
total=item_one+\
	  itrm_two+\
       item_three
```

- 在[],{},或（）中的多行语句，不需要使用反斜杠\

```python
total=['item_one','item_two','item_three',
'item_four','item_five']
```



**字符串**

- 字符串不能被改变

![](D:\typora\typora_note\字符串.png)

- 字符串更新：

![](D:\typora\typora_note\字符串更新.png)

- python三引号允许一个字符串跨多行

```python
para_str="""这是一个
跨多行字符串的实例
多行字符串可以使用制表符
TAB（\t）
也可以使用换行符[ \n ]
"""
print(para_str)
#结果

#这是一个多行字符串的实例
#多行字符串可以使用制表符
#TAB (    )
#也可以使用换行符 [ 
#]
```



- f-string----格式化字符串以f开头，后面跟着字符串，字符串中的表达式用大括号{}包起来，它会将变量或表达式计算后的值替换进去

```python
name='Runoob'
print(f'hello {name}')	#替换变量
#结果
'hello Runoob'
print(f'{1+2}')		#使用表达式
#结果
'3'
w={'name':'Runoob','url':'www.runoob.com'}
print(f'{w["name"]}:{w["url"]}')
#结果
'Runoob: www.runoob.com'
```



**同一行中显示多条语句**

- 语句之间使用;分隔

```python
import sys;x='runoob';sys.stdout.write(x+'\n')
#结果
runoob
```



**多个语句构成代码组**

- 除去第一行后面的一行或多行代码构成代码组
- 首行和代码组称为一个字句

```python
if expression:
    suite
elif expression:
    suite
else:
    suite
```



**print()输出**

- 默认换行，否end=""



**import 与from...import**

![](D:\typora\typora_note\import.png)



**标准数据类型**

- 多变量赋值

![](D:\typora\typora_note\标准数据类型.png)



**del语句删除一些对象的引用**

```python
del var1,var2...
```

- del也可以用来删除列表的元素 -----del list[2]、del tup--直接删除整个元组



![](D:\typora\typora_note\tips.png)



**python 使用\转译特殊字符，若不想让\发生转译，可以在字符串前面加一个r，表示原始字符串**

```python
print('Ru\noob')
print(r'Ru\noob')
#结果
Ru
oob

# Ru\noob
```



**列表**

![](D:\typora\typora_note\list.png)

- 加号+是列表连接运算符，星号*是重复操作

```python
list=[123,'runoob']
tiny=['abc']
print(list*2)
print(lsit+tiny)
#结果
[123,'runoob',123,'runoob']
[123,'runoob','abc']
```

- list中元素是可以改变的，可以被索引和切片
- python列表的截取可以接受第三个参数，参数作用是截取步长
- python列表函数&方法：

![](D:\typora\typora_note\list_fun.png)

![](D:\typora\typora_note\list_way.png)



- 下列实力用于翻转字符串

```python
def reverseWord(input):
    #通过空格将字符串分隔符，把各个单词分隔为列表
    inputWords=input.split(" ")
    #第一个参数-1表示最后一个元素
    #第二个参数为空，表示移动到列表末尾
    #第三个参数为步长，-1表示逆向
    inputWords=inputWords[-1::-1]
    output=' '.join(inputWords)
    return output

input='I like runoob'
rw=reverseWords(input)
print(rw)
#结果
runoob like I
```



**元组**

- 与列表类似，不同之处在于元组的元素不能修改

![](D:\typora\typora_note\tuple.png)

- 修改元组是不允许的，但是可以对元组进行连接组合

```python
tup1=(12,34,56)
tup2=('abc','xyz')
#创建一个新的元组
tup3=tup1+tup2
print(tup3)
#结果
(12,34.56,'abc','xyz')
```



- 元组与字符串类似，可以被索引且下标索引从0开始，-1为从末尾开始的位置
- 其实，可以把字符串看作一种特殊的元组

```python
tup1=()  #空元组
tup2=(20,)  #一个元素，需要在元素后面添加逗号
```

- 元组内置函数：

![](D:\typora\typora_note\tuple_fun.png)

- 关于元组是不可变的是指元组所指向的内存中的内容不可变



**注：**

- string、list、和tuple都属于sequence(序列)



**Set(集合)**

- 可以用大括号{ }或者set()函数创建集合，注意：创建一个空集合必须用set()而不是{ }，因为{ }是用来创建一个空字典

![](D:\typora\typora_note\srt.png)

- 添加元素：

```python
#语法：
s.add(x)
#样例：
thisset=set(("Google","Runoob","Taobao"))
thinset.add("Facebook")
print(thisset)
#结果
{'Taobao','Facebook','Google','Runoob'}

#还要一个方法，也可以添加元素，且参数可以是列表，元组，字典等，格式语法如下：
s.update(x)
#样例
thisset=set(("Google","Runoob","Taobao"))
thisset.update({1,3})
print(thisset)
#结果
{1,3,'Google','Taobao','Runoob'}
thisset.update([1,4],[5,6])
print(thisset)
#结果
{1,3,4,5,6,'Google','Taobao','Runoob'}
```

- 移除元素

```python
#语法
s.remove(x)		#将元素x从集合s中移除，如果元素不存在，则会发生错误
#样例
thisset=set(("Google","Runoob","Taobao"))
thisset.remove("Taobao")
print(thisset)
#结果
{'Google','Runoob'}
```

- 若删除元素不存在会报错

![](D:\typora\typora_note\set_remove_error.png)

- 还要一个删除方法，若删除元素不存在也不会报错----discard()函数

  ```python
  thisset=set(("Google","Runoob","Taobao"))
  thisset.discard("Facebook")		#不存在不会发生错误
  print(thisset)
  {'Taobao','Google','Runoob'}
  ```

- 我们也可以随机删除集合中的一个元素，语法如下：

```python
thisset=set(("Google","Runoob","Taobao","Facebook"))
x=thisset.pop()
print(x)
#结果
Runoob
#多次执行测试结果都不一样
#set集合的pop方法会对集合进行无序的排列，然后将这个无序排列集合的左面第一个元素进行删除
```

- 计算元素个数、清空集合、判断元素是否存在：

```python
thisset=set(("Google","Runoob","Taobao"))
print(len(thisset))
#结果
3

print("Runoob" in thisset)
print("Facebook" in thisset)
#结果
True
False

thisset.clear()
print(thisset)
#结果
set()
```

**集合内置函数方法完整列表**

![](D:\typora\typora_note\set_way.png)



**Dictionary(字典)**

![](D:\typora\typora_note\dict1.png)

- 变量名不建议命名为dict

- 列表是有序对象集合，字典是无序对象集合。两者之间的区别在于：字典当中的元素是通过键来存取的，而不是通过偏移存取
- 字典是一种映射类型，字典用{ }标识，它是一个无序的键（key）：值（value)的集合
- 键（key）必须使用不可变类型
- 在同一个字典中，键（key）必须是唯一的,但值则不必
- 如果字典哩没有键访问数据，会输出错误

```python
dict={}
dict['one']="1 - 菜鸟教程"
dict[2]="2 - 菜鸟工具"

tinydict={'name':'runoob','code':1,'site':'www.runoob.com'}
print(dict['one'])				#输出键为'one'的值
print(dict[2])					#输出键为2的值
print(tinydict)					#输出完整的字典
print(tinydict.keys())			#输出所有键
print(tinydict.values())		#输出所有值
```

![](D:\typora\typora_note\dict.png)

- 构造函数dict()可以直接从键值对序列中构造字典如下：

```python
dict([('Runoob',1),('Google',2),('Taobao',3)])
#结果
{'Runoob':1,'Google':2,'Taobao':3}

{x:x**2 for x in (2,4,6)}
#结果
{2:4,4:16,6:36}

dict(Runoob=1,Google=2,Taobao=3)
{'Runoob':1,'Google':2,'Taobao':3}
```

**修改字典**

```python
tinydict={'name':'Runoob','Age':7,'Class':'First'}
tinydict['Age']=8 		#更新Age
tinydict['School']='菜鸟教程'	#添加信息
print("tinydict['Age']:",tinydict['Age'])
print("tinydict['School']:",tinydict['School'])
#结果
tinydict['Age']: 8
tinydict['School']: 菜鸟教程
```



**删除字典元素**

```python
tinydict={'Name':'Runoob','Age':7,'Class':'First'}
del tinydict['Name']	#删除键'Name'
tinydict.clear()	#清空字典
del tinydict		#删除字典

```

- 字典键的特性：值可以是任何对象，包括用户定义的。键必须不可边，所以可以用数字，字符串或元组充当，而用列表就不行

![](D:\typora\typora_note\dict_error.png)

- 字典类型也有一些内置的函数，例如clear()、keys()、values()等
- 创建空字典使用{ }

**字典内置函数&方法**

![](D:\typora\typora_note\dict_fun.png)

![](D:\typora\typora_note\dict_way.png)

![](D:\typora\typora_note\dict_way2.png)

**python数据类型转换**

- 隐式类型转换：对两种不同类型的数据进行运算，较低数据类型（整数）就会转换为较高数据类型（浮点数）以免数据丢失

![](D:\typora\typora_note\数据类型转换.png)



**显式类型转换**

- 几个内置函数可以执行数据类型之间的转换。这些函数返回一个新的对象，表示转换的值

![](D:\typora\typora_note\数据类型转换函数.png)

- 一些转换示例

![](D:\typora\typora_note\转换eg.png)



**列表推导式**

- 列表推导式格式为：

```python
[表达式 for 变量 in 列表]
[out_exp_res for out_exp in input_list]		
#out_exp_res:列表生成元素表达式，可以是有返回值的函数
#for out_exp in input_list: 迭代input_list将out_exp传入到out_exp_res表达式中
#if condition: 条件语句，可以过滤掉列表中不符合条件的值
#或者

[表达式 for 变量 in 列表 if 条件]
[out_exp_res for out_exp in input_list if condition]
```



- 过滤掉长度小于或等于3的字符串列表，并将剩下的转换成大写字母：

```python
names=['Bob','Tom','alice','Jerry','Wendy','Smith']
new_names=[name.upper()for name in names if len(name)>3]
print(new_names)
#结果
['ALICE','JERRY','WENDY','SMITH']
```



- 计算30以内可以被3整除的整数

```python
multiples=[i for i in range(30) if i%3==0]
print(multiples)
#结果
[0,3,6,9,12,15,18,21,24,27]
```



**字典推导式**

- 基本格式：

```python
{key_expr:value_expr for value in collection}
#或
{key_expr:value_expr for value in collection if condition}
```



- 使用字符串及其长度创建字典：

```python
listdemo=['Google','Runoob','Taobao']
#将列表中各字符串值为键，各字符串的长度为值，组成键值对
newdict={key:len(key) for key in listdemo}
#结果
{'Google':6,'Runoob':6,'Taobao':6}

```

- 提供三个数字，以三个数字为键，三个数字的平方为值来创建字典：

```python
dic={x:x**2 for x in (2,4,6)}
#结果
{2:4,4:16,6:36}
```



**集合推导式**

- 基本格式：

```python
{expression for item in Sequence }
#或
{expression for item in Sequence if condition }
```

- 计算数字1，2，3的平方数：

```python
setnew={i**2 for i in (1,2,3)}
#结果
{1，4，9}
```

- 判断不是abc的字母并输出：

```python
a={x for x in 'abracadabra' if x not in 'abc'}
#结果
{'d','r'}
```



**元组推到式**

- 基本格式：

```python
(expression for item in Sequence)
#或
(expression for item in Sequence if condition )
```

- 元组推导式和列表推导式的用法也完全相同，只是元组推导式是用（）将各部分括起来，二列表推导式用的是中括号[ ]，另外元组推导式返回的是一个生成器对象
- 生成一个包含数字1~9的元组

```python
a=(x for x in range(1,10))
#结果
#返回的是一个生成器对象
tuple(a)
#结果       使用tuple（）函数，可以直接将生成器对象转换成元组
(1,2,3,4,5,6,7,8,9)
```



**运算符**

- 算术运算符：

![](D:\typora\typora_note\算术运算符.png)



- 比较运算符：

![](D:\typora\typora_note\比较.png)



- 赋值运算符：

![](D:\typora\typora_note\赋值.png)

- 位运算符：

```python
a=0011 1100
b=0000 1101
```

![](D:\typora\typora_note\位运算.png)

- 逻辑运算符：

![](D:\typora\typora_note\逻辑.png)

- 成员运算符：

![](D:\typora\typora_note\成员.png)

- 身份运算符

![](D:\typora\typora_note\身份.png)

- id()函数用于获取对象内存地址



- Python运算符优先级：

![](D:\typora\typora_note\python运算符优先级.png)

- 以下实例演示了Python所有运算符优先级的操作：

![](D:\typora\typora_note\运算符eg.png)

- and拥有更高优先级

![](D:\typora\typora_note\and拥用更高优先级.png)



### Python 数字（Number）

- 数据类型是不允许改变的，这意味着如果改变数字数据类型的值，将重新分配内存空间
- //得到的并不一定是整数类型的数，它与分子分母的数据类型有关系

![](D:\typora\typora_note\整除.png)

- 不同类型的数混合运算时会将整数转换为浮点数

- 交互

![](D:\typora\typora_note\交互.png)

- 数字常量 : pi --圆周率   e--自然常数
- 数学公式函数：

![](D:\typora\typora_note\数学函数.png) 

- 随机数函数：

![](D:\typora\typora_note\随机数函数.png)



- 三角函数：

![](D:\typora\typora_note\三角函数.png)



### Python---斐波那契数列

```python
#两个元素的总和确定了下一个数
a,b=0,1		#相当于是用了一个辅助的a=0
while b <10:
    print(b)
    a,b=b,a+b
```



### 条件控制

```python
#python 中的if语句一般形式如下：
if condition_1:
    statement_block_1
elif condition_2:
    statement_block_2
else:
    statement_block_3
```

![](D:\typora\typora_note\if_else.png)

```python
#实例
age=int(input("请输入你家狗狗的年龄："))
print("")
if age<=0:
    print("你是在逗我吧！")
elif age==1:
    print("相当于14岁的人")
elif age==2:
    print("相当于22岁的人")
elif age>2:
    human=22+(age-2)*5
    print("对应人类年龄：",human)
#退出提示
input("点击enter键退出")

#结果
#请输入你家狗狗的年龄：1
#相当于14岁的人
#点击enter键退出
```

- if嵌套

```python
#实例
num=int(input("输入一个数字："))
if num%2==0:
    if num%3==0:
        print("你输入的数字可以整除2和3")
    else:
        print("你输入的数字可以整除2，但不能整除3")
else:
    if num%3==0:
        print("你输入的数字可以整除3，但不能整除2")
    else:
        print("你输入的数字不能整除2和3")
        
#结果
#输入一个数字：6
#你输入的数字可以整除2和3
```



### while循环

```python
n=100
sum=0
counter=1
while counter<=n:
    sum=sum+counter
    counter+=1
print("1到%d之和为：%d"%(n,sum))
#结果
#1到100之和为：5050
```

- 无线循环用 CTRL+C来退出当前的无限循环

### while循环使用else语句

```python
while <expr>:
    <statement(s)>
else:
    <addition_statement>
```



### for语句--可以遍历任何可迭代对象，如一个列表或者一个字符串

```python
language=["C","C++","Perl","Python"]
for x in languages:
    print(x)
```



- range()函数--如果你需要遍历数组序列，可以使用内置range()函数，它会生成数列

```python
for i in range(5):

for i in range(5,9):
#还可以指定不同的增量：
for i in range(0,10,3):
#负数：
for i in range(-10,-100,-30):
#结果
-10
-40
-70

#还可以使用range()和len()函数来遍历一个序列的索引：
a=['Google','Baidu','Runoob','Taobao','QQ']
for i in range(len(a)):
    print(i,a[i])
#结果
0 Google
1 Baidu
2 Runoob
3 Taobao
4 QQ

```

- break和continue---类似c语言
- pass语句---空语句，不做任何事情，一般用做占位语句

```python
while True:
    pass    #等待键盘中断
```

