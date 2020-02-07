# Python

## 1. 命令行与交互模式

### 1.1 命令行模式

#### 1.1.1Windows下打开命令行

菜单选择‘命令行提示符’，或快捷键Windows+R选择cmd，它的提示符类似c:\>；

![命令行模式](E:\PythonNote\picture\命令行.png)

​	上图中的初始路径为C:\Users\杨扬>，是因为Windows增加了系统账户安全。要修改命令行初始路径可在“命令行提示符”的属性中修改。

若要获取管理员(Administrator)权限，则在cmd的绝对路径**C:\Windows\System32\cmd.exe**中**以管理员身份运行**cmd。若要在命令行里查找cmd(或其他文件)的绝对路径，可以输入**where + 文件名**：

~~~
$ C:\Users\Administrator>where cmd
C:\Windows\System32\cmd.exe
~~~

#### 1.1.2命令行操作指令

* **“cd”打开目录**
  1. 从C盘切换到其他盘：输入“d：”
  2. 打开该盘下的某个文件夹：输入“cd+文件夹名称”
  3. 返回上一级目录：输入“cd ..”
  4. 回到根目录：输入“cd\”

* **“dir”查看目录内容**

* **新建、复制、删除、重命名目录文件或文件夹**

  1. 输入命令“mkdir”或“md”创建文件夹
  2. 输入命令“type nul>[想要命名的文件名.类型]”创建空文件夹，输入命令“echo [文件内容]>[想要命名的文件名.类型]”创建非空文件
  3. 输入命令“copy test.txt test2.txt”把test.txt文件中的内容复制到test2.txt文件中，若test2.txt不存在，则会创建一个test2.txt

  4. “xcopy D:\test D:\test2 /s /e”把D盘中的test文件夹中的文件复制到test2中，其中可以选择test2为文件或目录
    5. 输入命令“del [文件名]”删除文件
    6. 输入命令“rd [文件夹名]”删除文件夹

* **重命名文件**
      1. 输入命令“ren test1.txt test4.txt”重命名test1.txt文件为test4.txt
      2. 输入命令“ren test2 test4”重命名test2文件夹为test 

* **查看文件内容**

  输入命令‘type test.txt’显示文本内容

* **清屏**

  输入命令**‘cls’**

### 1.2 Python交互模式

- 命令行模式下敲命令==`python`==，就进入到Python交互模式，它的提示符是>>>. 在Python交互模式下输入exit（）并回车就退出Python交互模式，并回到命令行模式
- 也可以直接通过打开IDLE解释器进入Python交互模式，但输入exit（）后窗口直接关闭，不会回到命令行模式

## 2. 输入和输出

### 2.1 print函数

* print函数括号中遇到逗号“，”会输出一个空格，下图的例子可以形象地解释![逗号](C:/Users/杨扬/Pictures/typython/逗号.png)

  `print()`也可以打印整数，或输出计算结果，`print(100+200)`的结果为300， 因此对print('100+200=', 100+200)运行结果的解释为，'100+200='部分print函数视为字符串，直接打印出来，然后遇到逗号输出一个空格，然后输出100+200的计算结果

* ==`print()`默认输出内容结尾为换行==，若要改变输出内容结尾，则要在输出内容后加上`,end=?`，问号内容是你想要的结尾，例如

  ```python
  
  """
  输出乘法口诀表(九九表)
  """
  
  for i in range(1, 10):
      for j in range(1, i + 1):
          print('%d*%d=%d' % (i, j, i * j), end='\t') #输出乘法公式后结尾为制表符
      print() #只输出换行
  ```

  因此在只需要输出换行的时候我们只用写`print()`即可

  经典实例

  ```python
  """
  打印三角形
      *
     ***
    *****
   *******
  *********
  """
  row = int(input('请输入行数'))
  for i in range(row):
      for _ in range(row - i - 1):
          print(' ', end='')
      for _ in range(2 * i + 1):
          print('*', end='')
      print() 
  ```


### 2.2 input函数

* 我们可以通过input函数允许用户输入字符串并存放到一个变量里。`name = input()`语句运行后等待用户输入，输入并按下回车后，输入的字符串就存放到`name`变量里。如果在Python交互模式下执行上述步骤，会回>>>状态。因为交互模式会输入一行执行一行，相当于解释器，因此在>>>后输入name按下回车就可以查看变量内容。除了直接写`name`然后按回车外，还可以用print()函数。
* input函数：若要在用户输入之前显示一个提示字符串，可以把想要用来提示的字符串写在input()括号里，例如

```python
name = input('please enter your name')
print('hello,', name)
```

​	运行这个程序会首先打印出`please enter your name`,程序就会友好一些。

## 3. 变量

### 3.1 Python变量的封装：

变量命名规则与C语言相同，不再赘述。

等号`=`是赋值语句，可以把任意数据类型赋值给变量。

同一个变量可以反复赋值，==而且可以是不同类型的变量==

当写下a=‘ABC’时python解释器干了两件事情：

1. 在内存中创建了一个‘ABC’的字符串
2. 在内存中创建了一个名为‘a’的变量，并把它指向‘ABC’。

这种变量本身类型不固定的语言称之为动态语言，与之对应的是静态语言。静态语言在定义变量时必须指定变量类型（定义），如果赋值是类型不匹配，就会报错。例如Java、C就是静态语言。

### 3.2 变量指向数据的详细操作

* 在a = 'ABC'操作后，可以把一个变量`a`赋值给另一个变量`b`，这个操作实际上是把变量`b`指向变量`a`所指向的数据，那么再执行以下代码后

  ~~~python
  a = 'ABC'
  b = a
  a = 'XYZ'
  print(b)
  ~~~

  ==最后一句打印变量`b`的内容到底是`'ABC'`呢还是`'XYZ'`？==

  让我们一行一行地执行代码，就可以看到到底发生了什么事：

  执行`a = 'ABC'`，解释器创建了字符串`'ABC'`和变量`a`，并把`a`指向`'ABC'`：

  ![py-var-code-1](https://www.liaoxuefeng.com/files/attachments/923791878255456/0)

  执行`b = a`，解释器创建了变量`b`，并把`b`指向`a`指向的字符串`'ABC'`：

  ![py-var-code-2](https://www.liaoxuefeng.com/files/attachments/923792058613440/0)

  执行`a = 'XYZ'`，解释器创建了字符串'XYZ'，并把`a`的指向改为`'XYZ'`，但`b`并没有更改：

  ![py-var-code-3](https://www.liaoxuefeng.com/files/attachments/923792191637760/0)

  所以，最后打印变量`b`的结果自然是`'ABC'`了。

  总结：在计算机内部，可以把任何数据都看成一个“对象”，==而变量就是再程序中用来指向这些数据对象的==，对变量的赋值就是把数据和变量给关联起来。==对变量赋值`x = y`是把变量`x`指向真正的对象，该对象是变量`y`所指向的==。随后对变量`y`的赋值*不影响*变量`x`的指向。这在Python面试题[0.4.1章节](# 1. 不可变数据类型分析)有更加详细的解释。

#### 3.2.1 一个值得注意的例外：list操作

![python list get wrong](E:\PythonNote\picture\python_list_wrong.png)

将`listA`赋值给`listB`之后，`listA.append`操作会同时改变`listA`和`listB`，因此使用`list`时切勿直接用一个`list`对另一个list赋值。为了避免这种情况，可采用`list.copy()`进行赋值：

![python list copy](E:\PythonNote\picture\python_list_copy.png)

由Python面试题[0.4 Python中的可变和不可变数据类型](# 0.4 Python中的可变和不可变数据类型)可知，这个例外是由于**`list`数据类型属于可变数据类型**引起的，两者的差别也就反应了Python中两类数据类型：不可变数据类型和可变数据类型的区别。

### 3.3 字符串变量

#### 3.3.1字符串变量：

Python的数据类型除了包括与C语言相同的整型和浮点型数据类型，还有一个特殊的类型：字符串。Python中将字符串封装成一个变量，就如同上面提到的`a='ABC'`，单个变量a即可存放字符串ABC。	字符串是以单引号或双引号括起来的任意文本，但==单引号或双引号本身并不是字符串的一部分==，而只是一种表示方式。因此，字符串'abc'只有`a`,`b`,`c`,三个字符

#### 3.3.2 字符串的特殊表示和**转义字符**：

1. 如果字符串需要包含单引号==`'`==而不能被当成表示方式，可以用`""`括起来，比如`I'm OK`包含的字符是`I`，`'`，`m`，空格，`O`，`K`这6个字符。

2. 如果字符串内部既包含`'`又包含`"`，可以用**转义字符**`\`来标识比如：

   ```
   'I\'m \"OK\"!'
   ```

   表示的字符串内容是：

   ```
   I'm "OK"!
   ```

   转义字符`\`可以转义很多字符，比如`\n`表示换行，`\t`表示制表符，**字符`\`本身也要转义，所以`\\`表示的字符就是`\`。**

3. Python还允许用`r''`表示`''`内部的字符串**默认不转义**，例如

   ```python
   >>> print('\\\t\\')
   \       \
   >>> print(r'\\\t\\')
   \\\t\\
   ```

4. 若字符串里有多行，为了避免太多`\n`的使用而降低阅读性，还可以使用`'''...'''`的格式表示多行内容，例如

   ```python
   >>> print('''line1
   ... line2
   ... line3''')
   line1
   line2
   line3
   ```

   上面是在交互式命令行内输入，==注意在输入多行内容时，提示符由`>>>`变为`...`，提示你可以接着上一行输入，注意`...`是提示符，不是代码的一部分==：

   ```ascii
   ┌────────────────────────────────────────────────────────┐
   │Command Prompt - python                           _ □ x │
   ├────────────────────────────────────────────────────────┤
   │>>> print('''line1                                      │
   │... line2                                               │
   │... line3''')                                           │
   │line1                                                   │
   │line2                                                   │
   │line3                                                   │
   │                                                        │
   │>>> _                                                   │
   │                                                        │
   │                                                        │
   │                                                        │
   └────────────────────────────────────────────────────────┘
   ```

   但在交互模式或.py文件中就没有`...`提示符。

## 4. 数据与数据类型

### 4.1 数据类型：复数

​	形如`3+5j`，跟数学上的复数表示一样，唯一不同的是虚部的`i`换成了`j`。

### 4.2 Python布尔值、布尔运算、与或非运算：

* 一个布尔值只有有`True`、`False`两种值，要么是`True`，要么是`False`，在Python中，可以直接用`True`、`False`表示布尔值（请注意大小写），也可以通过布尔运算计算出来：

```python
>>> True
True
>>> False
False
>>> 3 > 2 #布尔运算得到布尔值
True      #因此也可以说 3>2 会产生布尔值True
>>> 3 > 5
False
```

- 下面与或非运算的例子更可以说明 ==3>2会产生布尔值True==，布尔值可以用`and`、`or`和`not`运算。

​	`and`运算是**与运算**，只有所有都为`True`，`and`运算结果才是`True`：	

```python
>>> True and True
True
>>> True and False
False
>>> False and False
False
>>> 5 > 3 and 3 > 1 #说明 5>3、3>1会产生布尔值
True
```

​	`or`运算是或运算，只要其中有一个为`True`，`or`运算结果就是`True`：

```python
>>> True or True
True
>>> True or False
True
>>> False or False
False
>>> 5 > 3 or 1 > 3
True
```

​	`not`运算是非运算，它是一个==单目运算符==，把`True`变成`False`，`False`变成`True`：

```python
>>> not True
False
>>> not False
True
>>> not 1 > 2
True
```

​	`and`、`or`和`not`运算是C语言中`&&`,`||`,`-`的完美、形象的封装。

- 布尔值经常用在条件判断中，比如：

```python
if age >= 18:
    print('adult')
else:
    print('teenager')
```

### 4.3 Python除法运算

#### 4.3.1 浮点除`/`

```python
>>> 10 / 3
3.3333333333333335
```

`/`除法计算结果是浮点数，即使是两个整数恰好整除，结果也是浮点数：

```python
>>> 9 / 3
3.0
```

#### 4.3.2 地板除`//`

地板除的结果永远是整数，即使除不尽，即使是两个非整数相除。因为`//`只取结果的整数部分

```python
>>> 10 // 3
3
```

因此要做精确的除法，使用`/`就可以。

#### 4.3.3 取余`%`

可以得到两个数相除的余数

### 4.4 Python幂运算

​	`a**b`表示a的b次方

### 4.5 type()函数

​	检查变量的类型

```python
>>>a=100
>>>print(type(a))
<class 'int'>
>>>classmates=['Michael','Tom','Alice']
>>>print(type(classmates))
<class 'list'>
```

### 4.6 数据类型转换

- `int()`：将一个数值或字符串转换成整数，可以指定进制。

- `float()`：将一个字符串转换成浮点数。

- `str()`：将指定的对象转换成字符串形式，可以指定编码。

- `chr()`：将整数转换成该编码对应的字符串（一个字符）。

- `ord()`：将字符串（一个字符）转换成对应的编码（整数）。

  **这些并不是真正意义上的函数，而是创建对象的构造方法（之后会讲到）**

### 4.7 运算符

下表大致按照优先级从高到低的顺序列出所有运算符

| 运算符                                        | 描述                           |
| --------------------------------------------- | ------------------------------ |
| `[]` `[:]`                                    | 下标，切片                     |
| `**`                                          | 指数                           |
| `~` `+` `-`                                   | 按位取反, 正负号               |
| `*` `/` `%` `//`                              | 乘，除，模，整除               |
| `+` `-`                                       | 加，减                         |
| `>>` `<<`                                     | 右移，左移                     |
| `&`                                           | 按位与                         |
| `^` `|`                                       | 按位异或，按位或               |
| `<=` `<` `>` `>=`                             | 小于等于，小于，大于，大于等于 |
| `==` `!=`                                     | 等于，不等于                   |
| `is` `is not`                                 | 身份运算符                     |
| `in` `not in`                                 | 成员运算符                     |
| `not` `or` `and`                              | 逻辑运算符                     |
| `=` `+=` `-=` `*=` `/=` `%=` `//=` `**=` `&=` | 与C语言中用法相同              |

### 4.8 数据大小范围

* Python的整数没有大小限制，而某些语言的整数根据其存储长度是有大小限制的，例如Java对32位整数的范围限制在`-2147483648`-`2147483647`。

* Python的浮点数也没有大小限制，但是超出一定范围就直接表示为`inf`（无限大）。

### 4.9 字符编码

* 总的来说，使用编码就是把字符串转换成数据。解码就是把数据转换成字符串。而各种编码之间的转换是因为在不同应用或支持场景下需要的数据处理方式不同。Unicode编码保证了各种语言都能被转换为计算机能够处理的数据，而UTF-8编码保证了英文字符的数据的空间节省。因此在需要节省空间的传输数据和存储数据的场景下，就要使用UTF-8编码；在计算机内存中进行的，需要支持各种语言的编辑操作场景下，Unicode编码就非常需要。

* ASCII编码：仅支持英文字母、数字和一些符号的编码

* Unicode编码：把所有语言统一到一套编码里，常用的是一个字符用==两个字节（即八个位bit）==表示，字母`A`用ASCII编码是十进制的`65`，二进制的`01000001`；

  字符`0`用ASCII编码是十进制的`48`，二进制的`00110000`，注意字符`'0'`和整数`0`是不同的；

  汉字`中`已经超出了ASCII编码的范围，用Unicode编码是十进制的`20013`，二进制的`01001110 00101101`。

  你可以猜测，如果把ASCII编码的`A`用Unicode编码，只需要在前面补0就可以，因此，`A`的Unicode编码是`00000000 01000001`。可以注意到比ASCII编码多出一倍的存储空间。

* UTF-8编码：为了省去Unicode编码对英文字母的存储和传输需要的多出的一倍的空间，出现了把Unicode编码转化为“可变长编码”的`UTF-8`编码。UTF-8编码把一个Unicode字符根据不同的数字大小编码成1-6个字节，常用的英文字母被编码成1个字节，汉字通常是3个字节，只有很生僻的字符才会被编码成4-6个字节。如果你要传输的文本包含大量英文字符，用UTF-8编码就能节省空间：

  | 字符 | ASCII    | Unicode           | UTF-8                      |
  | :--- | :------- | :---------------- | :------------------------- |
  | A    | 01000001 | 00000000 01000001 | 01000001                   |
  | 中   | x        | 01001110 00101101 | 11100100 10111000 10101101 |

  从上面的表格还可以发现，UTF-8编码有一个额外的好处，就是ASCII编码实际上可以被看成是UTF-8编码的一部分，所以，大量只支持ASCII编码的历史遗留软件可以在UTF-8编码下继续工作。

* 由上可以看出：

  1. 当需要保存到硬盘或者需要传输时，就转换为UTF-8编码。在计算机内存中统一使用Unicode编码。

  2. 用记事本编辑，编辑完成后保存到硬盘时把Unicode转换为UTF-8保存到文件，再从文件中读取时，读取的UTF-8字符被转换成Unicode字符到内存里以便编辑。![rw-file-utf-8](https://www.liaoxuefeng.com/files/attachments/923923787018816/0)

  3. 浏览网页的时候，服务器会把动态生成的Unicode内容转换为UTF-8再传输到浏览器：

     ![web-utf-8](https://www.liaoxuefeng.com/files/attachments/923923759189600/0)

     所以你看到很多网页的源码上会有类似`<meta charset="UTF-8" />`的信息，表示该网页正是用的UTF-8编码。

### 4.10 Python字符串

* python 3版本中，字符串是以Unicode编码的，所以python的字符串支持多种语言

* 对于单个字符的编码，python提供了`ord()`函数获取字符的整数表示，`chr()`函数把编码转换为对应的字符，都是支持十进制、八进制、十六进制（只要是整型的参数）到字符的转换：

  ```python
  >>> ord('A')
  65
  >>> ord('中')
  20013
  >>> chr(66)
  'B'
  >>> chr(25991)
  '文'
  >>> chr(0x6587)
  '文'
  >>> chr(0b110010110000111)
  '文'
  >>> chr(0o62607)
  '文'
  ```

  如果知道字符的整数编码，还可以用十六进制这么写`str`：

  ```python
  >>> '\u4e2d\u6587'
  '中文'
  ```

  两种写法完全是等价的。

* python的字符串类型是`str`，在内存中以Unicode表示，一个字符对应若干个字节。如果要在网络上传输，或者保存到磁盘上，就需要把`str`变为以字节为单位的`bytes`。

  Python对`bytes`类型的数据用带`b`前缀的单引号或双引号表示：

  ```
  x = b'ABC'
  ```

  要注意区分`'ABC'`和`b'ABC'`，前者是`str`，后者虽然内容显示得和前者一样，==但`bytes`的每个字符都只占用一个字节。==

  以Unicode表示的`str`通过`encode()`方法可以编码为指定的`bytes`，例如：

  ```python
  >>> 'ABC'.encode('ascii')
  b'ABC'
  >>> '中文'.encode('utf-8')
  b'\xe4\xb8\xad\xe6\x96\x87'
  >>> '中文'.encode('ascii')
  Traceback (most recent call last):
    File "<stdin>", line 1, in <module>
  UnicodeEncodeError: 'ascii' codec can't encode characters in position 0-1: ordinal not in range(128)
  ```

  纯英文的`str`可以用`ASCII`编码为`bytes`，内容是一样的，含有中文的`str`可以用`UTF-8`编码为`bytes`。==含有中文的`str`无法用`ASCII`编码，因为中文编码的范围超过了`ASCII`编码的范围==，Python会报错。

* 如果我们从网络或磁盘上读取了字节流，那么读到的数据就是`bytes`。要把`bytes`变为`str`，就需要用`decode()`方法：

  ```python
  >>> b'ABC'.decode('ascii')
  'ABC'
  >>> b'\xe4\xb8\xad\xe6\x96\x87'.decode('utf-8')
  '中文'
  ```

  如果`bytes`中包含无法解码的字节，`decode()`方法会报错：

  ```python
  >>> b'\xe4\xb8\xad\xff'.decode('utf-8')
  Traceback (most recent call last):
    ...
  UnicodeDecodeError: 'utf-8' codec can't decode byte 0xff in position 3: invalid start byte
  ```

  如果`bytes`中只有一小部分无效的字节，可以传入==`errors='ignore'`==忽略错误的字节：

  ```python
  >>> b'\xe4\xb8\xad\xff'.decode('utf-8', errors='ignore')
  '中'
  ```

* `str`和`bytes`的互相转换非常频繁。为了避免乱码问题，==应当始终坚持使用UTF-8编码对`str`和`bytes`进行转换==。

* 因为python源代码是一个文本文件，可能包含中文，所以在保存源代码和解释器读取源代码是，为了不出现乱码，我们需要以下步骤指定使用UTF-8编码进行保存和读取

  1. 指定使用UTF-8编码读取：我们通常在文件开头写上这两行：

     ```python
     #!/usr/bin/env python3
     # -*- coding: utf-8 -*-
     ```

     第一行注释是为了告诉Linux/OS X系统，这是一个Python可执行程序，Windows系统会忽略这个注释；

     第二行注释是为了告诉Python解释器，按照UTF-8编码读取源代码

  2. 指定使用UTF-8编码保存`.py`文件：确保文本编辑器正在使用UTF-8 without BOM编码：

     ![set-encoding-in-notepad++](https://www.liaoxuefeng.com/files/attachments/1008802356788736)

#### 4.10.1 str trick

```python
def main():
    str1 = 'hello, world!'
    # 通过len函数计算字符串的长度
    print(len(str1))  # 13
    # 获得字符串首字母大写的拷贝，注意是拷贝，不会改变str1
    print(str1.capitalize())  # Hello, world!
    # 获得字符串每个单词首字母大写的拷贝
    print(str1.title()) # Hello,World!
    # 获得字符串变大写后的拷贝
    print(str1.upper())  # HELLO, WORLD!
    # 从字符串中查找子串所在位置
    print(str1.find('or'))  # 8
    print(str1.find('shit'))  # -1
    # 与find类似但找不到子串时会引发异常
    # print(str1.index('or'))
    # print(str1.index('shit'))
    # 检查字符串是否以指定的字符串开头
    print(str1.startswith('He'))  # False
    print(str1.startswith('hel'))  # True
    # 检查字符串是否以指定的字符串结尾
    print(str1.endswith('!'))  # True
    # 将字符串以指定的宽度居中并在两侧填充指定的字符
    print(str1.center(50, '*'))
    # 将字符串以指定的宽度靠右放置左侧填充指定的字符
    print(str1.rjust(50, ' '))
    str2 = 'abc123456'
    # 从字符串中取出指定位置的字符(下标运算)
    print(str2[2])  # c
    # 字符串切片(从指定的开始索引到指定的结束索引)
    print(str2[2:5])  # c12
    print(str2[2:])  # c123456
    print(str2[2::2])  # c246
    print(str2[::2])  # ac246
    print(str2[::-1])  # 654321cba
    print(str2[-3:-1])  # 45
    print(str2[-1:]) # 6
    print(str2[:-1]) # abc12345
    # 检查字符串是否由数字构成
    print(str2.isdigit())  # False
    # 检查字符串是否以字母构成
    print(str2.isalpha())  # False
    # 检查字符串是否以数字和字母构成
    print(str2.isalnum())  # True
    str3 = '  jackfrued@126.com '
    print(str3)
    # 获得字符串修剪左右两侧空格的拷贝
    print(str3.strip())


if __name__ == '__main__':
    main()
```

例题 ：利用切片操作，实现一个trim()函数，去除字符串首尾的空格，注意不要调用str的`strip()`方法：==下例高明在于利用切片进行自身迭代==

```python
# -*- coding: utf-8 -*-

def trim(s):

    while s[0:1]==' ':

        s=s[1:]

    while s[-1:]==' ':

        s=s[:-1]

    return s
# 测试:
if trim('hello  ') != 'hello':
    print(1,trim('hello  '))
    print('测试失败!')
elif trim('  hello') != 'hello':
    print(2,trim('  hello'))
    print('测试失败!')
elif trim('  hello  ') != 'hello':
    print(3,trim('  hello  '))
    print('测试失败!')
elif trim('  hello  world  ') != 'hello  world':
    print(4,trim('  hello  world  '))
    print('测试失败!')
elif trim('') != '':
    print(5,trim(''))
    print('测试失败!')
elif trim('    ') != '':
    print(6,trim('    '))
    print('测试失败!')
elif trim('hello') != 'hello':
    print(7,trim('hello'))
    print('测试失败!')    
else:
    print('测试成功!')    
```

==时刻要记住字符串也是一个序列==

### 4.11 len()函数

1. 对==`list`==数据类型的变量使用len()函数，可以得到`list`元素的个数：

   ```python
   >>> len(classmates)
   3
   ```

2. 对==`str`==数据类型的变量使用len()函数，可以计算`str`的字符数：

   ```python
   >>> len('ABC')
   3
   >>> len('中文')
   2
   ```

3. 对==`bytes`==数据类型的变量，`len()`函数就计算字节数：

   ```python
   >>> len(b'ABC')
   3
   >>> len(b'\xe4\xb8\xad\xe6\x96\x87')
   6
   >>> len('中文'.encode('utf-8'))
   6
   ```

   可见，1个中文字符经过UTF-8编码后通常会占用3个字节，而1个英文字符只占用1个字节。

### 4.12 格式化输出

​	格式化输出字符串，即按照一定的格式化顺序，文本位置输出数据。

#### 4.12.1 `%`运算符格式化字符串：

常见的占位符有：

| 占位符 | 替换内容     |
| :----- | :----------- |
| %d     | 整数         |
| %f     | 浮点数       |
| %s     | 字符串       |
| %x     | 十六进制整数 |

字符串内部有几个`%?`占位符，后面就跟几个变量或者值，数量、顺序、替换内容与占位符对应。如果只有一个`%?`，括起变量或者值的待替换内容的括号可以省略。举例如下：

```python
>>> 'Hello, %s' % 'world'
'Hello, world'
>>> 'Hi, %s, you have $%d.' % ('Michael', 1000000) #注意%s是字符串占位符，替换内											容是要加上双引号或者单引号的字符串
'Hi, Michael, you have $1000000.'
```

格式化整数和浮点数还可以指定是否补0、整数和小数的位数

```python
>>> print('%2d-%02d' % (3, 1))
 3-01
>>> print('%.2f' % 3.1415926)
3.14
```

如果不确定应该用什么，==`%s`永远起作用，它会把任何数据类型转换为字符串==：

```python
>>> 'Age: %s. Gender: %s' % (25, True)
'Age: 25. Gender: True'
```

有些时候，字符串里面的`%`是一个普通字符怎么办？这个时候就需要转义，==用`%%`来表示一个`%`==：

```python
>>> 'growth rate: %d %%' % 7
'growth rate: 7 %'
```

#### 4.12.2 `format()`函数：

`format()`方法会用传入的参数(当然是传入format函数的参数)==依次==替换==字符串内的占位符`{0}`、`{1}`……==（注意这也是另一种占位符），不过这种方式写起来比%要麻烦得多：

```python
>>> 'Hello, {0}, 成绩提升了 {1:.1f}%'.format('小明', 17.125)
'Hello, 小明, 成绩提升了 17.1%'
```

可以注意到使用`format()`函数若要控制输出位数，可在占位符`{0}`、`{1}`……的`{}`内的占位数字后写下，类似于上述例子`{1:.1f}`表示小数点后输出一位。

* ==注意格式化输入与C语言的不同点==：格式句式后面==没有逗号`,`==，只有`%()`。`()`中是按顺序要输出的值。

### 4.13 数据类型list

​	python内置数据类型list，可以理解为C语言的结构体或者数组，是一种有序的集合。

#### 4.13.1 创建一个list：

```python
>>> classmates = ['Michael', 'Bob', 'Tracy']
>>> classmates
['Michael', 'Bob', 'Tracy']
```

变量classmates就是一个list。

#### 4.13.2 键盘输入一个list：

```python
a_list = eval(input('plz enter a list: '))
```

如果输入 1,2,3,4,5，a_list = [1,2,3,4,5]

如果没有加上`eval()`，a_list的输入就会把逗号也会当成list元素。

#### 4.13.3 获得list元素的个数：

```python
>>> len(classmates)
3
```

使用`len()`函数

#### 4.13.4 访问list中每一个位置的元素：

```python
>>> classmates[0]
'Michael'
>>> classmates[1]
'Bob'
>>> classmates[2]
'Tracy'
>>> classmates[3]
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
IndexError: list index out of range
```

**注意使用中括号`[]`！！**

中括号`[]`中的数字称为**索引**，可以理解为一个目录，要找到对应元素，就从目录里找到元素的相应位置，这个位置就叫做索引。**索引从`0`开始**。当索引超出了范围时，Python会报一个`IndexError`错误（索引错误），要确保索引不要越界，记得最后一个元素的索引是**`len(classmates) - 1`**。

**可以用`-1`做索引，理解为倒数第一个元素**：

```python
>>> classmates[-1]
'Tracy'
```

以此类推，可以获取倒数第2个、倒数第3个：

```python
>>> classmates[-2]
'Bob'
>>> classmates[-3]
'Michael'
>>> classmates[-4]
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
IndexError: list index out of range
```

到倒数第4个，就出现了`IndexError`

#### 4.13.5 `list`方法

##### 4.13.5.1 追加函数`append()`

**（追加元素到==末尾==）：**

```python
>>> classmates.append('Adam')
>>> classmates
['Michael', 'Bob', 'Tracy', 'Adam']
```

##### 4.13.5.2 插入函数`insert()`

用索引号指明插入位置，如在**索引号**为`1`的位置插入：

```python
>>> classmates.insert(1, 'Jack')
>>> classmates
['Michael', 'Jack', 'Bob', 'Tracy', 'Adam']
```

##### 4.13.5.3 删除函数`pop()`

* 删除list**末尾**的元素，直接用`pop()`方法：

  ```python
  >>> classmates.pop()
  'Adam'
  >>> classmates
  ['Michael', 'Jack', 'Bob', 'Tracy']
  ```

* 删除指定位置的元素，用`pop(i)`方法，其中`i`是索引位置：

  ```python
  >>> classmates.pop(1)
  'Jack'
  >>> classmates
  ['Michael', 'Bob', 'Tracy']
  ```

##### 4.13.5.4 删除函数`remove()`

* ```python
  >>>classmates = ['Michael', 'Bob', 'Tracy']
  >>>classmates.remove('Tracy')
  >>>classmates
  ['Michael', 'Bob']
  >>> classmates.remove()
  Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
  TypeError: remove() takes exactly one argument (0 given)
  ```

  `remove()`与`pop()`不同在于`pop()`通过索引删除元素且未输入索引时默认删除末尾元素，而函数`remove()`则通过指定想要删除的元素来删除，且未指定时python解释器会出错。

##### 4.13.5.5 切片操作

* ~~~python
  fruits = ['grape', 'apple', 'strawberry', 'waxberry']
      fruits += ['pitaya', 'pear', 'mango']
      # 循环遍历列表元素
      for fruit in fruits:
          print(fruit.title()"""首字母大写""", end=' ')
      print()
      # 列表切片
      fruits2 = fruits[1:4]
      print(fruits2)# ['apple', 'strawberry', 'waxberry']
      # fruit3 = fruits  # 没有复制列表只创建了新的引用
      # 可以通过 完整切片 操作来复制列表
      fruits3 = fruits[:]
      print(fruits3)# ['grape', 'apple', 'strawberry', 'waxberry', 'pitaya', 'pear', 'mango']
      fruits4 = fruits[-3:-1]
      print(fruits4)# ['pitaya', 'pear']
      # 可以通过反向切片操作来获得倒转后的列表的拷贝
      fruits5 = fruits[::-1]
      print(fruits5)# ['mango', 'pear', 'pitaya', 'waxberry', 'strawberry', 'apple', 'grape']
  
  ~~~

  **所有切片操作都是基于索引**

  **字符串`'xxx'`也可以看成是一种list**，每个元素就是一个字符，因此字符也可以用切片操作和索引访问操作，操作结果仍是字符串。
  
  **注意：当你仅仅想对一个list做拷贝操作到另一个list去的时候，千万不要`list1 = list2`，因为这个操作会让你的两个list指向同一个对象，之后你仅对list1做改变时list2也会跟着改变。拷贝操作是`list1 = list2[:]`                                     或`list1 = list2.copy()`。这样不会引发意外的指向操作**

##### 4.13.5.6 排序操作`sorted()`

* ~~~python
  list1 = ['orange', 'apple', 'zoo', 'internationalization', 'blueberry']
  list2 = sorted(list1)
  list3 = sorted(list1, reverse=True)# 排序之后翻转顺序
  # 通过key关键字参数指定根据字符串长度进行排序而不是默认的字母表顺序
  list4 = sorted(list1, key=len)
  print('list1=',list1)
  print('list2=',list2)
  print('list3=',list3)
  print('list4=',list4)
  # 给列表对象发出排序消息直接在列表对象上进行排序
  list1.sort(reverse=True)
  print('list1=',list1)
  ~~~

  sorted函数返回列表排序后的**拷贝**==不会修改传入的列表==

  函数的设计就应该像sorted函数一样尽可能的不产生副作用，若要对列表本身修改而不是进行拷贝，就要在list内使用sorted函数即`list.sort()`

##### 4.13.5.7 替换list元素

可以==直接赋值==给对应的索引位置：

```python
>>> classmates[1] = 'Sarah'
>>> classmates
['Michael', 'Sarah', 'Tracy']
```

##### 4.13.5.8 返回元素索引

```python
>>> test = [5,2,3,4,1]
>>> test.index(5)
0
>>> test.index(4)
3
```

##### 4.13.5.9 判断list中是否包含某个元素：

```python
>>> a = [1,2,3]
>>> 1 in a
True
>>> 4 in a
False
>>> 4 not in a
True
```

##### 4.13.5.10 `list`元素特性：

* 元素数据类型可以不同：

  ```python
  >>> L = ['Apple', 123, True]
  ```

  也可以是另一个list：

  ```python
  >>> s = ['python', 'java', ['asp', 'php'], 'scheme']
  >>> len(s)
  4
  ```

  ==要注意`s`只有4个元素==，其中`s[2]`又是一个list，如果拆开写就更容易理解了：

  ```python
  >>> p = ['asp', 'php']
  >>> s = ['python', 'java', p, 'scheme']
  ```

  ==要拿到`'php'`可以写`p[1]`或者`s[2][1]`，因此`s`可以看成是一个二维数组==

  如果一个list中一个元素也没有，就是一个空的list，它的长度为0：

  ```python
  >>> L = []
  >>> len(L)
  0
  ```

#### 4.13.6 两个list的求交集、并集、差集

python中求两个list的交集并集差集，大体两种思路：

1. 使用**列表解析式**，比for循环更快，更pythonic。
2. 将list转成set，再利用set的方法处理

~~~python
def intersection_list(listA: 'list', listB: 'list')->'list':
    intersection_AB = [i for i in listA if i in listB] #利用列表解析式
    # 或用转成set，用set的内置的intersection方法求交集，再转化回list
    # intersection_AB = list(set(listA).intersection(set(listB)))
    return intersection_AB

def union_list(listA: 'list', listB: 'list')->'list':
    union_AB = list(set(listA).union(set(listB))) # 利用set的union方法
    return union_AB

def difference_list(listA: 'list', listB: 'list')->'list':
    difference_AB = [i for i in listA if i not in listB] # 列表解析式，求A对B的差集
    # set内置difference函数
    # difference_AB = list(set(listA).difference(set(listB)))
    return difference_AB
~~~

### 4.14 生成式语法与生成器

​	本节主要讲的是生成式语法创建列表以及简单介绍生成器对象

#### 4.14.1 生成式语法创建list

~~~python
>>>f = [x for x in range(1,10)]
>>>print(f)
[1,2,3,4,5,6,7,8,9]
>>>f = [x+y for x in 'abcde' for y in '12345'] # 生成全排列
>>>print(f)
['a1', 'a2', 'a3', 'a4', 'a5', 'b1', 'b2', 'b3', 'b4', 'b5', 'c1', 'c2', 'c3', 'c4', 'c5', 'd1', 'd2', 'd3', 'd4', 'd5', 'e1', 'e2', 'e3', 'e4', 'e5']
>>>f = [x ** 2 for x in range(1,1000)]
>>>import sys
>>>print(sys.getsizeof(f))
9024
~~~

#### 4.14.2 生成式语法创建生成器对象（generator）

~~~python
>>>f = (x ** 2 for x in range(1,1000))
>>>import sys
>>>print(sys.getsizeof(f))
88
>>>print(f)
<generator object <genexpr> at 0x000001FBBD8A00A0>
 >>>for val in f:
 ...    print(val)
>>>next(g) # 还可以通过next（g）访问每一个生成器元素
1
>>>next(g)
4
~~~

1. 注意生成器与生成式语法创建列表的区别：列表在`[]`里使用生成式语法；生成器对象则通过在`()`中使用生成式语法来创建。

2. 由上面可以看出生成器对象所占空间远远小于列表，但可以访问生成器对象的每一个数据，这些数据和列表中的一样。**这是因为通过生成器对象可以获得数据但它不占用额外的空间来存储数据**，每次需要数据的时候就通过内部的运算得到数据(这需要花费额外的时间)

3. 生成器generator获得内部数据需要通过运算，这是因为生成器保存的是算法，每次调用`next(g)`，就计算出g的下一个元素的，直到计算到最后一个元素，没有下一个元素时，抛出`StopIteration`的错误。
4. 虽然`next(g)`可以做到访问每一个元素，但这太麻烦了，所以一般使用循环来迭代它，并且不需要关心`StopIteration`的错误。

#### 4.14.3 `yield`关键字生成生成器对象

除了生成器语法，我们还可以通过在函数中借助`yield`关键字把迭代的数==传入容器==，借此把这个函数改造成生成器函数。例：生成**斐波拉切数列**的生成器：

```python
def fib(n):
    a, b = 0, 1
    for _ in range(n):
        a, b = b, a + b
        yield a


def main():
    for val in fib(20):
        print(val)


if __name__ == '__main__':
    main()
```

`yield`与关键字`return`很相似，都是把一个值返回，但是`return`是单纯返回一个值并结束整个函数，而`yield`是返回一个值进入容器，使得函数本身成为一个容器generator function，调用这个函数时，遇到`yield`语句返回，并且不会结束函数，而是==从`yield`语句的下一条语句继续执行==。

例：定义一个generator，依次返回数字1,3,5,

~~~python
def odd():
    print('step 1')
    yield 1
    print('step 2')
    yield(3)
    print('step 3')
    yield(5)
~~~

调用该generator时，==首先要生成一个generator对象==，然后用`next()`函数不断获得下一个返回值

```python
>>> o = odd()
>>> next(o) # 对一个对象才能使用next（）
step 1
1
>>> next(o)
step 2
3
>>> next(o)
step 3
5
>>> next(o)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
StopIteration
```

### 4.15 迭代器

`Iterable`与`Iterator`

#### 4.15.1 `Iterable` 可迭代对象

即可直接作用于for循环的对象，能在循环中不断迭代。类似的包括如`list`、`tuple`、`dict`、`set`、`str`等以及上文提到的`generator`，包括生成器和带`yield`的generator function，都是可迭代对象。

可以使用`isinstance()`判断一个对象是否是`Iterable`对象：

```python
>>> from collections import Iterable
>>> isinstance([], Iterable)
True
>>> isinstance({}, Iterable)
True
>>> isinstance('abc', Iterable)
True
>>> isinstance((x for x in range(10)), Iterable)
True
>>> isinstance(100, Iterable)
False
```

#### 4.15.2 `Iterator` 迭代器

表示一个==数据流==，Iterator对象可以被`next()`函数调用并不断返回下一个数据，直到没有数据时抛出`StopIteration`错误。==可以把这个数据流看做是一个有序序列，但我们却不能提前知道序列的长度，只能不断通过`next()`函数实现按需计算下一个数据==，所以`Iterator`的计算是**惰性**的，只有在需要返回下一个数据时它才会计算。

生成器generator都是迭代器对象，但`list`、`dict`、`str`虽然是`Iterable`，却不是`Iterator`。

同样的可以用`isinstance()`判断一个对象是否是`Iterator`对象：

```python
>>> from collections import Iterator
>>> isinstance((x for x in range(10)), Iterator)
True
>>> isinstance([], Iterator)
False
>>> isinstance({}, Iterator)
False
>>> isinstance('abc', Iterator)
False
```

把`list`、`dict`、`str`等`Iterable`变成`Iterator`可以使用`iter()`函数：

```python
>>> isinstance(iter([]), Iterator)
True
>>> isinstance(iter('abc'), Iterator)
True
```

由于迭代器具有数据流的性质，因此甚至可以表示一个无限大的序列，例如全体自然数。==而使用list是永远不可能存储全体自然数的==。可以打个比方，如果你要存储一片海洋的量的数据，你就需要一片海洋那么大的存储空间，但如果你仅仅是以流的形式不断获得这大量的数据，那么你需要的只是一条河流让他不断流进来。

* 总结：凡是可作用于`for`循环的对象都是`Iterable`类型；

  凡是可作用于`next()`函数的对象都是`Iterator`类型，它们表示一个惰性计算的序列；

  集合数据类型如`list`、`dict`、`str`等是`Iterable`但不是`Iterator`，不过可以通过`iter()`函数获得一个`Iterator`对象。

  ==Python的`for`循环本质上就是通过不断调用`next()`函数实现的==，例如：

  ```python
  for x in [1, 2, 3, 4, 5]:
      pass
  ```

  实际上完全等价于：

  ```python
  # 首先获得Iterator对象:
  it = iter([1, 2, 3, 4, 5])
  # 循环:
  while True:
      try:
          # 获得下一个值:
          x = next(it)
      except StopIteration:
          # 遇到StopIteration就退出循环
          break
  ```

  ==实际上就是：非迭代器的可迭代对象在进行for循环时，先把非迭代器用`iter()`转换成迭代器，再不断循环调用`next()`获得返回值。==

### 4.16 数据类型tuple

​	tuple与list类似，是一种有序列表加元组，但与list不同的是==tuple一旦初始化就不能修改==，因此你可以像访问list元素一样通过索引访问tuple元素，如`classmates[0]`，`classmates[-1]`。但因为它的不可改变，也就==没有append()，insert()这样的方法，也不能对tuple元素赋值成另外的元素==。但相对来说tuple的不可变保证了代码更加安全。==如果可能，能用tuple代替list就尽量用tuple==。在设计函数的时候如果要返回多个值，使用元组也是一个不错的选择。

* 定义一个tuple：

  在定义的时候，tuple的元素就必须被确定下来，比如：

  ```python
  >>> t = (1, 2)
  >>> t
  (1, 2)
  ```

  如果要定义一个空的tuple，可以写成`()`：

  ```python
  >>> t = ()
  >>> t
  ()
  ```

  但是，要定义一个只有1个元素的tuple，如果你这么定义：

  ```python
  >>> t = (1) #定义只有一个元素的tuple的错误示例
  >>> t
  1
  ```

  定义的不是tuple，而是`1`这个数！这是因为括号`()`既可以表示tuple，又可以表示数学公式中的小括号，这就产生了歧义，因此，Python规定，==这种情况下，按小括号进行计算，计算结果自然是`1`。==

  所以，只有1个元素的tuple定义时必须加一个逗号`,`，来消除歧义：

  ```python
  >>> t = (1,) #√正确示例
  >>> t
  (1,)
  ```

  ==Python在显示只有1个元素的tuple时，也会加一个逗号`,`，以免你误解成数学计算意义上的括号。==

* `tuple`元素是不可修改的，因此当然也不能像列表一样使用索引对某个位置的索引重新赋值：

  ```python
  t = ('骆昊', 38, True, '四川成都')
  # 重新给元组赋值
  # t[0] = '王大锤'  # TypeError
  t = ('王大锤', 20, True, '云南昆明')
  print(t)
  # 结果：('王大锤',20,True,'云南昆明')
  ```

重新赋值会出错，而`t = ('王大锤', 20, True, '云南昆明')`操作是==变量t重新引用了另一个新的元组==，即王大锤元组，而原来的元组将被垃圾回收。元组不可改变，上面看起来的改变不过是变量t指向了一个新的元组罢了。

* tuple元素的不可变性是指：==tuple的指向不可变==。如果你的tuple中包含一个数据类型为list的元素，tuple的不可变性可解释为：tuple的某一位置一直指向这个list，这个位置上的元素不能改变成一个值或者另一个list之类的其他对象，但被指向的这个list本身仍保留其特性，是可变的，图解如下：  

  ```python
    >>> t = ('a', 'b', ['A', 'B'])
    >>> t[2][0] = 'X'
    >>> t[2][1] = 'Y'
    >>> t
    ('a', 'b', ['X', 'Y'])
  ```

这个tuple定义的时候有3个元素，分别是`'a'`，`'b'`和一个list。

  先看看定义的时候tuple包含的3个元素：

  ![tuple-0](https://www.liaoxuefeng.com/files/attachments/923973516787680/0)

  当我们把list的元素`'A'`和`'B'`修改为`'X'`和`'Y'`后，tuple变为：

  ![tuple-1](https://www.liaoxuefeng.com/files/attachments/923973647515872/0)

  表面上看，tuple的元素确实变了，但其实变的不是tuple的元素，而是list的元素。tuple一开始指向的list并没有改成别的list，所以，**tuple所谓的“不变”是说，tuple的每个元素，指向永远不变。**

### 4.17 总结list和tuple

* 创建一个变量`i`，无论`i`的数据类型是`list`还是`tuple`，若写入`print(i)`，打印结果都是整个以集合形式呈现的有序集合`i`。

* tuple的不可变性让它在许多情况下被优先考虑：

  1. 多线程环境下，不变对象更容易维护且更关键的是没有任何一个线程能够改变不变对象的内部状态，一个不变对象自动就是线程安全的。因此在多线程的状态下一个不变对象可以方便被共享访问。

  2. 元组在创建时间和占用的空间上都优于列表

     ~~~py
     >>> test_list = [x for x in range(1,100)]
     >>> test_tuple = (x for x in range(1,100))
     >>> import sys
     >>> print('size of list is %d and size of tuple is %d' 
               %(sys.getsizeof(test_list),sys.getsizeof(test_tuple)))
     size of list is 912 and size of tuple is 88
     ~~~

  ![img](https://github.com/jackfrued/Python-100-Days/raw/master/Day01-15/res/ipython-timeit.png)

  （注：上图是在ipython中使用魔法指令%timeit来分析创建同样内容的元组和列表所花费的时间）

## 5. 数据结构

### 5.1 分支结构

#### 5.1.1 if语句的使用

* 构造分支结构可以使用`if`、`elif`和`else`==关键字==（关键字即有特殊含义的单词，显然不能用作标识符），例：

  ```python
  
  """
  用户身份验证
  """
  
  username = input('请输入用户名: ')
  password = input('请输入口令: ')
  # 如果希望输入口令时 终端中没有回显 可以使用getpass模块的getpass函数
  # import getpass
  # password = getpass.getpass('请输入口令: ')
  if username == 'admin' and password == '123456':
      print('身份验证成功!')
  else:
      print('身份验证失败!')
  ```

  python与C、Java等语言不同在于，Python没有使用花括号来构造代码块，而是使用缩进的方式来区分代码层次结构。若要多条==连续的==语句构成一个代码块，这些语句使用相同的缩进即可。

* 若要构造出更多的分支，可以使用`if…elif…else…`结构，例如下面的分段函数求值。

  ```Python
  """
  分段函数求值
  
          3x - 5  (x > 1)
  f(x) =  x + 2   (-1 <= x <= 1)
          5x + 3  (x < -1)
  """
  
  x = float(input('x = '))
  if x > 1:
      y = 3 * x - 5
  elif x >= -1:
      y = x + 2
  else:
      y = 5 * x + 3
  print('f(%.2f) = %.2f' % (x, y))
  ```

* 根据实际开发的需要，可以使用嵌套的分支结构，即在`if`/`elif`/`else`的内部构造新的分支结构，也就是说上面的代码也可以写成下面的样子。

  ```Python
  """
  分段函数求值
  		3x - 5	(x > 1)
  f(x) =	x + 2	(-1 <= x <= 1)
  		5x + 3	(x < -1)
  """
  
  x = float(input('x = '))
  if x > 1:
      y = 3 * x - 5
  else:
      if x >= -1:
          y = x + 2
      else:
          y = 5 * x + 3
  print('f(%.2f) = %.2f' % (x, y))
  ```

  值得一提，Python之禅中有这么一句话“Flat is better than nested.”，之所以提倡代码“扁平化”是因为嵌套结构的嵌套层次多了之后会严重的影响代码的可读性，所以==能使用扁平化的结构时就不要使用嵌套。==

* Python100在这一章节提到的几个常用的`import`：

  1. ```python
     from random import randint
     
     side = randint(1,6)
     ```

     产生整型随机数，还可以调用`randint()`函数指定产生随机数的范围，上面的`randint(1,6)`指的是随机产生从1~6的数（包括1和6在内）

  2. ```python
     # 计算圆和三角形的面积
     import math
     
     radius = float(input('请输入圆的半径：'))
     circlearea = math.PI * (radius**2)
     a = float(input('a = '))
     b = float(input('b = '))
     c = float(input('c = '))
     if a + b > c and a + c > b and b + c > a:
          p = (a + b + c) / 2
         # 利用math.sqrt()实现海伦公式的计算
         trianglearea = math.sqrt(p * (p - a) * (p - b) * (p - c))
     ```

  3. ~~~python
     import getpass
     
     password = getpass.getpass('请输入口令: ') #使用getpass模块的getpass函数可以                                            使终端不会回显你的输入
     ~~~

     类似于上面的math、random、getpass的称为模块，`import` 关键字可以导入指定的模块，之后会提到。

### 5.2 循环结构

#### 5.2.1 for-in循环

* 适用环境：知道循环执行的次数或者要对一个容器进行迭代（后面会讲到）例如下面代码中计算1~100求和的结果（$\displaystyle \sum \limits_{n=1}^{100}n$）。

  ```python
  """
  用for循环实现1~100求和
  
  Author: 骆昊
  """
  
  sum = 0
  for x in range(101):
      sum += x
  print(sum)
  ```

  需要说明的是上面代码中的`range`类型，`range`可以用来产生一个不变的数值序列，而且这个序列通常都是用在循环中的，例如：

  - `range(101)`可以产生一个0到100的整数序列。
  - `range(1, 100)`可以产生一个1到99的整数序列。
  - `range(1, 100, 2)`可以产生一个1到99的奇数序列，==其中的2是步长==，==即数值序列的增量==。

  知道了这一点，我们可以用下面的代码来实现1~100之间的偶数求和。

  ```python
  """
  用for循环实现1~100之间的偶数求和
  """
  
  sum = 0
  for x in range(2, 101, 2):
      sum += x
  print(sum)
  ```

  也可以通过在循环中使用分支结构的方式来实现相同的功能，代码如下所示。

  ```python
  """
  用for循环实现1~100之间的偶数求和
  """
  
  sum = 0
  for x in range(1, 101):
      if x % 2 == 0:
          sum += x
  print(sum)
  ```

#### 5.2.2 while循环

* 适用环境：构造不知道具体循环次数的循环结构。
* 特点：`while`循环通过一个能够产生或转换出`bool`值的表达式来控制循环，表达式的值为`True`循环继续，表达式的值为`False`循环结束。==在实际应用中我们通常使用`while True:`加`break`来实现和控制循环。==

#### 5.2.3 总结两个循环

* 和分支结构一样，循环结构也是可以嵌套，下面的例子演示了如何通过嵌套的循环来输出一个九九乘法表。

  ```python
  """
  输出乘法口诀表(九九表)
  Author: 骆昊
  """
  
  for i in range(1, 10):
      for j in range(1, i + 1):
          print('%d*%d=%d' % (i, j, i * j), end='\t')
      print()
  ```

* `for-in`和`while`关键字都要==加上冒号`:`==。

* `while`循环注意不要写成死循环。

## 6. 函数与模块

“**代码有很多种坏味道，重复是最坏的一种！**”

定义函数：

**使用`def`关键字来定义函数**。函数名后的圆括号内放置传递给函数的参数，参数相当于数学上的自变量，而函数执行完后通过`return`关键字来返回一个值，这相当于数学上的因变量。

### 6.1 Python函数的特殊性

**函数的参数可以有默认值，也支持可变参数==**，例子：

```python
from random import randint


def roll_dice(n=2):
    """
    摇骰子
    
    :param n: 骰子的个数
    :return: n颗骰子点数之和
    """
    total = 0
    for _ in range(n):
        total += randint(1, 6)
    return total


def add(a=0, b=0, c=0):
    return a + b + c


# 如果没有指定参数那么使用默认值摇两颗色子
print(roll_dice())
# 摇三颗色子
print(roll_dice(3))
print(add())
print(add(1))
print(add(1, 2))
print(add(1, 2, 3))
# 传递参数时可以不按照设定的顺序进行传递
print(add(c=50, a=100, b=200))
```

上面的两个函数都设定了默认值，**意味着如果在调用函数时如果没有传入对应的参数的值时将使用该参数的默认值。**

### 6.2 设置默认值

1. 是必选参数在前，默认参数在后，否则Python的解释器会报错；

2. 当函数有多个参数时，优先把变化小的参数设置默认值。

3. 设置多个参数默认值的函数在调用时，如下图

   ```python
   def enroll(name, gender, age=6, city='Beijing'):
       print('name:', name)
       print('gender:', gender)
       print('age:', age)
       print('city:', city)
   
   enroll('Bob', 'M', 7)
   enroll('Adam', 'M', city='Tianjin')
   ```

   调用`enroll('Bob', 'M', 7)`，==其中的参数按照顺序提供默认参数==，意思是，除了`name`，`gender`这两个参数外，最后1个参数应用在参数`age`上，`city`参数由于没有提供，仍然使用默认值。

   也可以不按顺序提供部分默认参数。==当不按顺序提供部分默认参数时，需要把参数名写上。==比如调用`enroll('Adam', 'M', city='Tianjin')`，意思是，`city`参数用传进去的值，其他默认参数继续使用默认值。

4. 默认参数的陷阱：当使用一个变量作为函数的默认参数时，若函数中有对参数做出改变的操作，那么每一次使用默认参数调用函数后，默认参数的默认值都会改变，例：

```python
def add_end(L=[]):
    L.append('END')
    return L
>>> add_end()
['END']
>>> add_end()
['END', 'END']
>>> add_end()
['END', 'END', 'END']
```

上述的结果的原因是：==首先，默认参数`L`是个可变的`list`，==，一开始指向对象`[]`，但一经函数调用后`L`指向的对象改变，==即默认参数的内容就改变，不再是函数定义时的`[]`。==

因此==定义默认参数要牢记：默认参数必须指向不变对象==

要修改上面的例子，我们可以用`None`这个不变对象来实现：

```python
def add_end(L=None):
    if L is None:
        L = []
    L.append('END')
    return L
```

现在，无论调用多少次，都不会有问题：

```python
>>> add_end()
['END']
>>> add_end()
['END']
```

### 6.3 可变参数

实际应用中我们传入函数的参数可能不确定，因此就可以利用可变参数

~~~python
def calc(*numbers):
    sum = 0
    for n in numbers:
        sum = sum + n * n
    return sum

>>> calc(1, 2, 3) # 这样我们就可以传入数量不定的参数
14
>>> calc(1, 3, 5, 7)
84
~~~

在参数名前面加上`*`表示numbers是一个可变参数，即在调用calc时可以传入0个或多个参数。实际上在函数内部，==参数`numbers`接收到的是一个tuple。==

如果已经有一个现有的list或者tuple，要把这个作为参数传进去呢？==Python允许你在list或tuple前面加一个`*`号，把list或tuple的元素变成可变参数传进去：==

```python
>>> nums = [1, 2, 3]
>>> calc(*nums)
14
```

`*nums`表示把`nums`这个list的所有元素作为可变参数传进去。这种写法相当有用，而且很常见。

## 7. 栈和栈溢出(简介)

​	在计算机中，函数调用时通过**栈**这种数据结构实现的，每当进入一个函数调用，栈就会加一层**栈帧**，每当函数返回，栈就会减少一层栈帧。由于栈的大小不是无限的，所以在使用递归的时候需注意防止递归次数过多导致**栈溢出**

## 8. 函数式编程

### 8.1 高阶函数概述

* ==变量可以指向函数==，指向函数后可以通过该变量调用这个函数：

  ```python
  >>> f = abs
  >>> f(-10)
  10
  ```

* ==函数名也是变量==，例如对于`abs()`函数，完全可以把函数名abs看出变量，他指向一个可以计算绝对值的函数！如果把`abs`指向其他对象，会有什么情况发生？

  ```python
  >>> abs = 10
  >>> abs(-10)
  Traceback (most recent call last):
    File "<stdin>", line 1, in <module>
  TypeError: 'int' object is not callable
  ```

  把`abs`指向`10`后，就无法通过`abs(-10)`调用该函数了！因为`abs`这个变量**已经不指向求绝对值函数**而是指向一个整数`10`！

  当然实际代码绝对不能这么写，这里是为了说明函数名也是变量。要恢复`abs`函数，请重启Python交互环境。

  注：由于`abs`函数实际上是定义在`import builtins`模块中的，所以要让修改`abs`变量的指向在其它模块也生效，要用`import builtins; builtins.abs = 10`。

  理解函数名为指向函数的变量之后，我们就会想到能否把指向函数的变量当成参数传入另一个函数里呢，因此就出现了**高阶函数**，所谓的高阶函数，就是函数的参数能接收别的函数。而函数式编程就是指这种高度抽象的编程范式。

### 8.2 sorted函数

​	sorted函数中将key指定的函数作用于list的==每一个元素==上，并根据key函数返回的结果进行排序，因此key指定的函数关键在于，你想要根据什么属性筛选，那么key指定的函数作用于每个list元素上后，只返回你想要的那个属性，例：假设我们用一组tuple表示学生名字和成绩：

```
L = [('Bob', 75), ('Adam', 92), ('Bart', 66), ('Lisa', 88)]
```

​	请用`sorted()`对上述列表分别**按名字**排序：

```python
# -*- coding: utf-8 -*-

L = [('Bob', 75), ('Adam', 92), ('Bart', 66), ('Lisa', 88)]
def by_name(t):
    return t[0]
L2 = sorted(L, key=by_name)
print(L2)
```

​	**按成绩从高到低**排序

~~~python
# -*- coding: utf-8 -*-

L = [('Bob', 75), ('Adam', 92), ('Bart', 66), ('Lisa', 88)]
def by_score(t):
    return -t[1]
L2 = sorted(L, key=by_score)
print(L2)
~~~

### 8.3 返回函数

​	返回函数就是把函数作为返回值，而当用一个变量接收这个返回值时，这个变量就指向了这个被返回的函数，因此直接输出该变量会显示他是一个函数，而要用变量名加括号如`f()`才能调用函数，调用后输出才能输出这个函数的返回值。例如我们定义一个函数，返回值是一个求和函数：

~~~python
def lazy_sum(*args):
    def sum():
        ax = 0
        for n in args:
            ax = ax + n
        return ax
    return sum
~~~

当我们调用`lazy_sum()`时，返回的并不是求和结果，而是求和函数：

```python
>>> f = lazy_sum(1, 3, 5, 7, 9)
>>> f
<function lazy_sum.<locals>.sum at 0x101c6ed90>
```

调用函数`f`时（此时调用f就是调用sum），才真正计算求和的结果：

```python
>>> f()
25
```

在这个例子中，函数`lazy_sum`中又定义了函数`sum`，并且，内部函数`sum`可以引用外部函数`lazy_sum`的参数和局部变量，当`lazy_sum`返回函数`sum`时，==相关参数和变量都保存在返回的函数中，这种称为“闭包（Closure）”的程序结构拥有极大的威力。==

注意：当我们调用`lazy_sum()`时，每次调用都会返回一个新的函数，即使传入相同的参数：

```
>>> f1 = lazy_sum(1, 3, 5, 7, 9)
>>> f2 = lazy_sum(1, 3, 5, 7, 9)
>>> f1==f2
False
```

`f1()`和`f2()`的调用结果互不影响。

#### 8.3.1 闭包

​	返回的函数在其内部引用了局部变量args，==所以函数被返回后还在引用局部变量，且需要注意的是返回的函数还没有立刻执行，而是直到被调用时才被执行，这就有可能导致在真正调用时其内部引用的局部变量发生了改变==，比如下例中返回函数内部引用了循环变量：

~~~python
def count():
    fs = []
    for i in range(1, 4):
        def f():
             return i*i
        fs.append(f)
    return fs

f1, f2, f3 = count() #期待f1(),f2(),f3()分别输出1,4,9
~~~

```python
#但三个都输出9
>>> f1()
9
>>> f2()
9
>>> f3()
9
```

上例代码的操作是==每次返回一个`f`都存放在一个`list`里（即`fs`），是想要用一个list存放三个有不同返回值的函数==，因此才有`f1, f2, f3 = count()`，f1, f2, f3 分别对应`fs`这个列表里的三个函数。==但**闭包**的特性就在于返回的函数在真正调用到他们时（也就是`f1(),f2(),f3()`时）执行，而这三个返回的函数里都有引用变量`i`，变量`i`在真正调用到他们时早已是`3`啦！==所以三个函数执行`i*i`后都有相同的返回值。这就是为什么操作`print(f1(),f2(),f3())`都有相同的三个输出`9`，是因为他们都用了相同的变量`i`并且都是在`i=3`的时候执行并返回值。因此，返回闭包的时候要牢记：返回函数不要引用任何循环变量，或者后续会发生变化的变量。

如果一定要引用循环变量怎么办？方法是再创建一个函数，用该函数的参数绑定循环变量当前的值，无论该循环变量后续如何更改，已绑定到函数参数的值不变：

```python
def count():
    def f(j):
        def g():
            return j*j
        return g
    fs = []
    for i in range(1, 4):
        fs.append(f(i)) # f(i)立刻被执行，因此i的当前值被传入f()
    return fs
```

再看看结果：

```
>>> f1, f2, f3 = count()
>>> f1()
1
>>> f2()
4
>>> f3()
9
```

而解决办法的操作是，既然一定要引用循环变量，那就==利用已绑定到函数参数的值不变的规则，在返回函数前再加一级函数，把这个循环变量当成上一级函数的参数传入，和参数绑定，再利用这个参数计算返回值，这样在之后调用返回函数时，返回函数的返回值就不会因为循环变量的改变而改变了。==（ 而要注意的就是后续一定要为那个上一级函数传入循环变量作为参数。）后续的操作是一样的，把返回函数每一次返回都存入一个list中。

缺点是代码较长，可利用lambda函数缩短代码。例如上面的代码可以改成这样：

~~~python
def count():
    def f(j):
        return lambda : j*j
    fs = []
    for i in range(1, 4):
        fs.append(f(i))
    return fs
~~~

可以借个例子来体会返回函数滞后执行的妙处：写一个decrator(之后会详细介绍装饰器decrator)，它作用于所有函数，并计算该函数的执行时间

~~~python
# -*- coding: utf-8 -*-
import time, functools
def metric(func):
    @functools.wraps(func)
    def wrapper(*args, **kw):
        start=time.time()
        r=func(*args, **kw)
        end=time.time()
        print('%s executed in %s ms' % (func.__name__, end-start))
        return r
    return wrapper 

# 测试
@metric
def fast(x, y):
    time.sleep(0.0012)
    return x + y;

@metric
def slow(x, y, z):
    time.sleep(0.1234)
    return x * y * z;

f = fast(11, 22)
s = slow(11, 22, 33)
print(fast.__name__)

if f != 33:
    print('测试失败!')
elif s != 7986:
    print('测试失败!')
else:
    print('测试成功！')
~~~

可以看到装饰器`metric`里返回一个函数`wrapper`，即wrapper作为返回函数，并不立即执行，==而是在调用的时候（即后来的`f=fast(11,22)`）再执行wrapper函数，执行时wrapper函数里的start、func（*args，**kw）、end才会被计算，就计算出运行函数所用的时间==，这一例就体现了返回函数被真正调用后才执行的妙处

#### 8.3.2 小结

* 一个函数可以返回一个计算结果，也可以返回一个函数
* 返回一个函数时，牢记该函数并未执行，返回函数中不要引用任何可能会变化的变量

### 8.4 匿名函数

​	上节提到了匿名函数的关键字`lambda`，并且特殊地作为返回函数返回且引用了上一级参数，简化了代码，相当于定义了一个==没有参数传入==的函数`g()`返回`j*j`，只不过这个函数并没有名字。

> 缺点是代码较长，可利用lambda函数缩短代码。例如上面的代码可以改成这样：
>
> ```python
> def count():
>     def f(j):
>         return lambda : j*j
>     fs = []
>     for i in range(1, 4):
>         fs.append(f(i))
>     return fs
> ```

这就叫做**匿名函数**，例如匿名函数`lambda x: x * x`实际上就是：

```python
def f(x):
    return x * x
```

关键字`lambda`表示匿名函数，冒号前面的`x`表示函数参数。

匿名函数有个限制，就是==只能有一个表达式==，不用写`return`，返回值就是该表达式的结果。

用匿名函数有个好处，因为函数没有名字，不必担心函数名冲突。此外，匿名函数也是一个函数对象，也可以把匿名函数赋值给一个变量，再利用变量来调用该函数：

```python
>>> f = lambda x: x * x
>>> f
<function <lambda> at 0x101c6ef28>
>>> f(5)
25
```

同样，也可以把匿名函数作为返回值返回，比如：

```python
def build(x, y):
    return lambda: x * x + y * y
```

注意，此时返回的是一个函数，并不是`x*x+y*y`的值。返回一个匿名函数的方法也在过滤器中应用广泛，例如埃氏筛法求素数的实现：

~~~python
# -*- coding: utf-8 -*-

def _odd_iter():
    n = 1
    while True:
        n = n + 2
        yield n
        
def _not_divisible(n):
    return lambda x: x % n > 0

def primes():
    yield 2
    it = _odd_iter() # 初始序列
    while True:
        n = next(it) # 返回序列的第一个数
        yield n
        it = filter(_not_divisible(n), it) # 构造新序列

# 打印1000以内的素数:
for n in primes():
    if n < 1000:
        print(n,end = ' ')
    else:
        break   
~~~

在定义`_not_divisible(n)`函数中，返回一个匿名函数，也就相当于返回一个`g(x): x % n > 0`，因此在之后的`primes`函数中的`it = filter(_not_divisible(n), it)`就是把`it`中的每个元素都放入这个匿名函数`g(x)`去过滤了，每次获得`it`的下一个值`n=next(it)`都会通过filter把n的倍数筛去获得一个新的`it`序列，逐渐逐渐获得全体素数，这就是**埃氏筛法**。

### 8.5 函数注解表达式

注解表达式便于函数使用者了解函数参数的数据类型，具体如下：

~~~python
def demo(name: str, age: 'int > 0'=20)->str:  # ->str 表示该函数的返回值是str类型的
    print(name, type(name))
    print(age, type(age))
    return "hello world"

demo(1, 2)
# 1 <class 'int'>
# 2 <class 'int'>

demo('Yang Yang', 2)
# Yang Yang <class 'str'>
# 2 <class 'int'>

print(demo.__annotations__)
# {'name': <class 'str'>, 'age': 'int >0 ', 'return': <class 'str'>}
~~~

1. 函数声明中的各个参数可以在：后增加注解表达式。

2. 如果参数由默认值，注解放在参数名和 = 号之间。

3. 如果注解有返回值，在 ) 和函数末尾的：之间增加 -> 和一个表达式。那个表达式可以是任何类型.
4. 注解中最常用的类型是类（如 str 或 int）和字符串（如 'int > 0'）.

**对于注解，python解释器不会做任何检查或验证处理，仅会将注解存储在函数的`demo.__annotations__`属性里。换言之，注解对于python解释器没有意义，仅是为了方便函数使用者**

例如上例代码块，将int类型的1传入demo函数的name参数仍可正常运行；再如，将`return "hello world" `换成`return 1`，函数返回值就变为int类型的1，不会受`->str`注解的影响

## 9. 面对对象编程

### 9.1 作用域

* public：模块中可以被直接引用的，如正常的函数和变量，比如：`abc`，`x123`，`PI`等；

* private：仅仅希望在模块内部被使用，不应该直接被引用的函数和变量，通过`_`前缀来实现，如`_abc`，`__abc`等；之所以我们说，private函数和变量**“不应该”**被直接引用，而不是“不能”被直接引用，是因为Python并没有一种方法可以完全限制访问private函数或变量，但是，从编程习惯上不应该引用private函数或变量。

* 特殊变量：还有可以被直接引用但有特殊用途的，比如模块的`__author__`变量用于写入作者姓名，`__name__`用于存放模块名，`hello`模块定义的文档注释也可以用特殊变量`__doc__`访问，我们自己的变量一般不要用这种变量名；

  private函数或变量不应该被别人引用，那它们有什么用呢？请看例子：

  ```python
  def _private_1(name):
      return 'Hello, %s' % name
  
  def _private_2(name):
      return 'Hi, %s' % name
  
  def greeting(name):
      if len(name) > 3:
          return _private_1(name)
      else:
          return _private_2(name)
  ```

  我们在模块里公开`greeting()`函数，而把内部逻辑用private函数隐藏起来了，这样，**调用`greeting()`函数不用关心内部的private函数细节**，这也是一种非常有用的代码封装和抽象的方法，即：**外部不需要引用的函数全部定义成private，只有外部需要引用的函数才定义为public。**
  

## 10. 装饰器

### 10.1 hello，装饰器

装饰器的使用方法很固定

1. 先定义一个装饰器（帽子）
2. 再定义你的业务函数或者类（人）
3. 最后把这装饰器（帽子）扣在这个函数（人）头上

下例是个简单的装饰器，没有任何特定功能

```python
def decorator(func):
    def wrapper(*args, **kw):
        return func()
    return wrapper

@decorator
def function():
    print("hello, decorator")
```

装饰器对于我们的编程并不是必须的，而是应用在编程中使我们的代码

* 更加优雅，代码结构更加清晰
* **将实现特定的功能代码封装成装饰器，提高代码复用率，增强代码可读性**

### 10.2 入门：日志打印器

首先是**日志打印器**。
实现的功能：

1. 在函数执行前，先打印一行日志告知一下主人，我要执行函数了。
2. 在函数执行完，也不能拍拍屁股就走人了，咱可是有礼貌的代码，再打印一行日志告知下主人，我执行完啦。

```python
# 这是装饰器函数，参数 func 是被装饰的函数
def logger(func):
    def wrapper(*args, **kw):
        print('主人，我准备开始执行：{} 函数了:'.format(func.__name__))

        # 真正执行的是这行。
        func(*args, **kw)

        print('主人，我执行完啦。')
    return wrapper
```

假如，我的业务函数是，计算两个数之和。写好后，直接给它带上帽子。

```
@logger
def add(x, y):
    print('{} + {} = {}'.format(x, y, x+y))
```

然后执行一下 add 函数。

```
add(200, 50)
```

输出：

```
主人，我准备开始执行：add 函数了:
200 + 50 = 250
主人，我执行完啦。
```

实际上，上例中自己写的装饰器logging蕴含了返回函数和函数参数的知识

* 返回函数：装饰器返回函数`wrapper`，而返回函数在真正调用时（即add（200,50））才执行，因此才可以在运行前后打印出执行日志。利用这个返回函数和装饰器组合的特性，我们还可以加上导入time模块来计算执行时间（即利用time.time()获得当前时间从而获得执行前后的时间差）具体代码在返回函数一节
* 返回函数的参数是参数`(*args, **kw)`，这个参数的性质就是适用于任何函数的参数，因此返回函数的参数设置为此可以最大限度保留函数特质，**因此注意要把最终返回的函数的参数设置为参数`(*args, **kw)`**

### 10.3 进阶：带参数的函数装饰器

实现**传参**，就需要两层嵌套

```python
def say_hello(contry):
    def wrapper(func):
        def deco(*args, **kwargs):
            if contry == "china":
                print("你好!")
            elif contry == "america":
                print('hello.')
            else:
                return

            # 真正执行函数的地方
            func(*args, **kwargs)
        return deco
    return wrapper
```

==重要的是把真正执行的函数放入最里层的嵌套中，再通过返回函数一层层返回，来实现函数的执行和其余的装饰==

参数在装饰器最外层传入，这样就可以直接在使用装饰器的时候传入，执行函数在第二层传入，而因为三层嵌套最终返回的是最里层函数，因此函数在最里层执行且最里层函数参数设置为参数`(*args, **kw)`

### 10.4 高阶：不带参数的类装饰器

基于类装饰器的实现，必须实现`__call__`和`__init__`两个内置函数：

* `__init__`函数：接收被装饰函数，即把被装饰函数当做类的属性，便于在类的内部方法里应用。
* `__call__`函数：==实现装饰逻辑==，装饰函数的内部逻辑都在`__call__`函数里规定。

下例仍是日志打印，在实际编程中当然不会动用类装饰器来实现如此简单的功能，在这里只是为了简要了解其方法

~~~python
class logger(object):
    def __init__(self,func):
        self.func = func
    
    def __call__(self):
        print("[INFO]: the function {func}'''format特殊占位符''' () is running....."\
        	.format(func'''呼应上面的占位符''' = self.func.__name__))
        return self.func(*args,**kwargs)
    
@logger
def say(something):
    print("say {}! ".format(something))
    
say('hello!')
~~~

执行

~~~py
[INFO]: the function say() is running...
say hello!
~~~

### 10.5 高阶：带参数的类装饰器

上例不带参数，只能打印一类日志`[INFO]`，但通常情况下我们还需打印`DEBUG` `WARNING`等级别的日志。这就需要给类装饰器传入参数，给这个函数指定级别了。

带参数和不带参数的类装饰器有很大的不同。

`__init__` ：不再接收被装饰函数，==而是接收传入参数。==
`__call__` ：接收被装饰函数，实现装饰逻辑。==并且嵌套函数并返回该函数==。

```python
class logger(object):
    def __init__(self, level='INFO'):
        self.level = level

    def __call__(self, func): # 接受函数
        def wrapper(*args, **kwargs):
            print("[{level} '''format特殊占位符''' ]: the function {func}() is running..."\
                .format(level=self.level, func=func.__name__))
            func(*args, **kwargs)
        return wrapper  #返回函数

@logger(level='WARNING')
def say(something):
    print("say {}!".format(something))

say("hello")
```

我们指定`WARNING`级别，运行一下：

```
[WARNING]: the function say() is running...
say hello!
```

#### 10.5.1 使用偏函数与类实现装饰器

==在这里也顺便介绍了如何用类构造偏函数实例==

在之前的了解中，偏函数通过`functools.partial(func,parameter=?)`来实现对函数参数默认值的改变。而通过类构造偏函数，实际上是通过`functools.partial(func,parameter=?)`构造类的实例，且传入其属性的值。

于传入参数的类装饰器**不同**的是==类之中不需要在`__call__`嵌套函数进行返回==，`__call__`中只需写入装饰器逻辑即可，从而代码更为简便。可以这么说，偏函数的使用将类的负担减轻，例：

~~~python
import time
import functools

class DelayFunc:
    def __init__(self,  duration, func):
        self.duration = duration
        self.func = func

    def __call__(self, *args, **kwargs):
        print(f'Wait for {self.duration} seconds...')
        time.sleep(self.duration)
        return self.func(*args, **kwargs)

    def eager_call(self, *args, **kwargs):
        print('Call without delay')
        return self.func(*args, **kwargs)

def delay(duration):
    """
    装饰器：推迟某个函数的执行。
    同时提供 .eager_call 方法立即执行
    """
    # 此处为了避免定义额外函数，
    # 直接使用 functools.partial 帮助构造 DelayFunc 实例
    return functools.partial(DelayFunc, duration)
~~~

delay函数作为装饰器返回一个偏函数，正是分担了**传入参数的类装饰器**的嵌套函数的负担。

执行：

~~~python
@delay(duration=2)
def add(a, b):
    return a+b

>>> add    # 可见 add 变成了 Delay 的实例
<__main__.DelayFunc object at 0x107bd0be0>
>>> 
>>> add(3,5)  # 直接调用实例，进入 __call__
Wait for 2 seconds...
8
>>> 
>>> add.func # 实现实例方法
<function add at 0x107bef1e0>
~~~

可以观察到由于delay装饰器返回的是类的实例，因此add变为类的实例。

该方法的生僻之处在于比较抽象，是通过==返回的一个偏函数（类的实例）来接收我们的业务函数，而不是像前几例一样直接作为参数或属性接收==

#### 10.5.2 能装饰类的装饰器

~~~python
instances = {}

def singleton(cls):
    def get_instance(*args, **kw):
        cls_name = cls.__name__
        print('===== 1 ====')
        if not cls_name in instances:
            print('===== 2 ====')
            instance = cls(*args, **kw)
            instances[cls_name] = instance
        return instances[cls_name]
    return get_instance

@singleton
class User:
    _instance = None

    def __init__(self, name):
        print('===== 3 ====')
        self.name = name
~~~

可以看到我们用singleton 这个装饰函数来装饰 User 这个类。装饰器用在类上，并不是很常见，但只要熟悉装饰器的实现过程，就不难以实现对类的装饰。在上面这个例子中，装饰器就只是实现对类实例的生成的控制而已。

## 11. 定制类

* `__getitem__`将类的实例允许list操作(廖雪峰定制类`__getitem__`方法)

```python
class Fib(object):
    def __getitem__(self, n):
        if isinstance(n, int): # n是索引
            a, b = 1, 1
            for x in range(n):
                a, b = b, a + b
            return a
        if isinstance(n, slice): # n是切片
            start = n.start
            stop = n.stop
            if start is None:
                start = 0
            a, b = 1, 1
            L = []
            for x in range(stop):
                if x >= start:
                    L.append(a)
                a, b = b, a + b
            return L
```

注意切片的相应操作：先取得切片的`n.start`、`n.stop`，再判断如果`n.start`是空的话就把开始的start设成0，接着利用循环创造斐波拉契数列并在循环操作的第一个步骤设为检测x与start的关系（因为start=0就需要立刻存入list）

## 12. 图形用户界面与游戏开发

### 12.1 基于tkinter模块的GUI（图形用户界面）

* 使用tkinter来开发GUI应用需要以下5个步骤：

  1. 导入tkinter模块中我们需要的东西
  2. 创建一个顶层窗口对象并用它来承载整个GUI应用
  3. 在顶层窗口对象上添加GUI组件
  4. 通过代码将这些GUI组件的功能组织起来
  5. 进入主事件循环（mainloop）

  因为GUI应用通常是事件驱动式，因此进入主事件循环就是要监听鼠标、键盘等各种事件的发生并执行对应的代码对事件进行处理，而事件会持续发生，所以需要这样的一个循环一直运行着等待下一个事件的发生。

  另一方面，Tk为控件的摆放提供了三种布局管理器，通过布局管理器可以对控件进行定位，这三种布局管理器分别是：Placer（开发者提供控件的大小和摆放位置）、Packer（自动将控件填充到合适的位置）和Grid（基于网格坐标来摆放控件）

# 实际中遇到的问题

### 1. 在对`<class 'numpy.ndarray'>`类型的变量，例如x，做`x *= 0.1`或`x += 0.1`时，numpy 1.16.0版本会报错:

~~~
Traceback (most recent call last):
  File ".\new.py", line 8, in <module>
    image[:,:,0] *= random.uniform(0.5, 1.5)
TypeError: Cannot cast ufunc multiply output from dtype('float64') to dtype('uint8') with casting rule 'same_kind'
~~~

解决：诸如此类的 `a+=b, a*=b`语句需要写成`np.add(a, b, out=a, casting="unsafe")`或`np.mutiply(a, b, out=a, casting="unsafe")`。

# Python面试题

## 0.

### 0.1 列出 5 个常用 Python 标准库

#### 0.1.1 datetime -- 基本的日期和时间类型

datetime是python处理日期和时间的标准库，下面主要介绍较为常用的类`class datetime.datetime`

##### 1. 获取当前日期和时间

~~~python
from datetime import datetime
now = datetime.now()
print(now)
# 2020-02-06 20:20:47.662129
~~~

1. **注意到获取的时间是毫秒级的**。
2. 注意到datetime是模块，datetime模块包含着datetime类，通过`from datetime import datetime`导入`datetime`这个类。

##### 2. 创建一个datetime实例

~~~python
from datetime import datetime
dt = datetime(2020, 2, 2, 20, 20)
print(dt)
# 2020-02-02 20:20:00
~~~

用参数可以直接实例化一个datetime类

##### 3. datetime转换为timestamp

在计算机中，时间实际上是用数字表示的。**把1970年1月1日 00:00:00 UTC+00:00时区的时刻称为epoch time，记为`0`**（1970年以前的时间timestamp为负数），**当前时间就是相对于epoch time的秒数，称为timestamp**。

`timestamp = 0 = 1970-1-1 00:00:00 UTC+0:00`

对应北京时间：`timestamp = 0 = 1970-1-1 08:00:00 UTC+8:00`，因此`timestamp`和时区无关。因为timestamp一旦确定其UTC时间即确定，转化到任意时区的时间也是确定的。

**一个datetime类实例可以直接调用`timestamp()`方法：**

~~~python
from datetime import datetime
now = datetime.now()
print(now.timestamp())
# 1580993170.957051
~~~

1. **注意到，python的timestamp是一个浮点数。如果有小数位，则小数位表示毫秒数**。
2. **若碰到用整数表示timestamp且已知timestamp精确到毫秒级的情况，需要把timestamp除以1000才能得到python的浮点表示方法表示的timestamp（也才能用python的`datetime.fromtimestamp()`方法将该timestamp转化成datetime，否则会因超出范围报错）**。

##### 4. timestamp转换为datetime

使用`datetime.timestamp()`方法：

~~~python
from datetime import datetime
t = 1580993170.957051
print(datetime.fromtimestamp(t))
# 2020-02-06 20:46:10.957051
~~~

注意到timestamp是一个浮点数，它没有时区的概念，而datetime是有时区的。**上述转换是在timestamp和本地时间做转换。本地时间是指当前操作系统设定的时区。例如北京时区是东8区，则本地时间实际上是UTC+8：00**

timestamp也可以直接被转换到UTC标准时区的时间：

~~~python
from datetime import datetime
t = 1580993170.957051
print(datetime.fromtimestamp(t))
# 2020-02-06 20:46:10.957051
print(datetime.utcfromtimestamp(t))
# 2020-02-06 12:46:10.957051
~~~

##### 5. str转换为datetime

使用`datetime.strptime()`方法，需要一个日期和时间的格式化字符串：

~~~python
from datetime import datetime
cday = datetime.strptime('2020-02-02 20:20:02', '%Y-%m-%d %H:%M:%S')
print(cday)
~~~

格式化字符串形如`'%Y-%m-%d %H:%M:%S'`详细见[Python文档](https://docs.python.org/3/library/datetime.html#strftime-strptime-behavior)

##### 6. datetime转换为str

转换方法是通过`strftime()`实现的，同样需要一个日期和时间的格式化字符串：

```python
from datetime import datetime
now = datetime.now()
print(now.strftime('%a, %b %d %H:%M'))
# Mon, May 05 16:28
```

**可以对datetime对象组成的列表进行排序**

```python
from datetime import datetime
dt1 = datetime(2020, 2, 6, 20, 20)
dt2 = datetime(2020, 2, 7, 20, 20)
dt3 = datetime(2020, 2, 2, 20, 20)
day_list = [dt1, dt2, dt3]
print(sorted(day_list))
#[datetime.datetime(2020, 2, 2, 20, 20), datetime.datetime(2020, 2, 6, 20, 20), datetime.datetime(2020, 2, 7, 20, 20)]
```



#### 0.1.2 collections -- 容器数据类型

##### 1. namedtuple

`namedtuple`是一个函数，用来创建一个自定义的`tuple`对象并且规定了`tuple`元素的个数，并可以用属性而不是索引来引用其中的某个元素。这样创建的对象具备`tuple`的不变性，又能根据属性来引用，**相当于创建了一个继承`tuple`的新的子类型**。

例如利用`namedtuple`创建一个用于表示坐标的`tuple`子类`Point`：

~~~python
from collections import namedtuple
Point = namedtuple('Point', ['x','y'])
p = Point(1,2)
print(p.x, p.y) # 根据属性引用
# 1 2
~~~

##### 2. deque

`deque`是为了高效实现插入和删除操作的**双向列表**，适合用于队列和栈，相比于线性存储的`list`在数据量大时效率更高

```python
from collections import deque
q = deque(['a','b','c'])
q.append('x')
q.appendleft('y')
print(q)
# deque(['y', 'a', 'b', 'c', 'x'])
```

所谓双向列表，即如上所示，支持list的`append()`和`pop()`（右边添加和删除）外，还支持`appendleft()`和`popleft()`（左边）

##### 3. defaultdict

`defaultdict`和`dict`大部分特性相同，但`defaultdict`可以规定**引用不存在的key时返回的默认值**而避免产生`KeyError`,**默认值通过调用函数返回**，函数在创建`defaultdict`对象时传入，如：

```python
from collections import defaultdict
dd = defaultdict(lambda: 'N/A') # 传入匿名函数lambda，默认值即函数值'N/A'
dd['key1'] = 'abc'
print(dd['key1']) # 引用的key1存在
# 'abc'
print(dd['key2']) # key2不存在，返回默认值
# 'N/A'
```

##### 4. ChainMap

`ChainMap`可以把一组`dict`串起来并组成一个逻辑上的`dict`。`ChainMap`本身也是一个dict，但是查找的时候，会按照顺序在内部的dict依次查找。

举个例子：应用程序往往都需要传入参数，参数可以通过命令行传入，可以通过环境变量传入，还可以有默认参数。我们**可以用`ChainMap`实现参数的优先级查找，即先查命令行参数，如果没有传入，再查环境变量，如果没有，就使用默认参数。**

下面的代码演示了如何查找`user`和`color`这两个参数：

```python
from collections import ChainMap
import os, argparse

# 构造缺省参数:
defaults = {
    'color': 'red',
    'user': 'guest'
}

# 构造命令行参数:
parser = argparse.ArgumentParser()
parser.add_argument('-u', '--user')
parser.add_argument('-c', '--color')
namespace = parser.parse_args()
command_line_args = { k: v for k, v in vars(namespace).items() if v }

# 组合成ChainMap:
combined = ChainMap(command_line_args, os.environ, defaults)

# 打印参数:
print('color=%s' % combined['color'])
print('user=%s' % combined['user'])
```

没有任何参数时，打印出默认参数：

```python
$ python3 use_chainmap.py 
color=red
user=guest
```

当传入命令行参数时，优先使用命令行参数：

```python
$ python3 use_chainmap.py -u bob
color=red
user=bob
```

同时传入命令行参数和环境变量，命令行参数的优先级较高：

```python
$ user=admin color=green python3 use_chainmap.py -u bob
color=green
user=bob
```

##### 5. OrderedDict

`OrderedDict`的`popitem()`方法可以实现FIFO（先入先出），利用这个可以创建一个**当容量超出限制时先删除最早添加的key的FIFO的dict**。

```python
from collections import OrderedDict

class LastUpdatedOrderedDict(OrderedDict):

    def __init__(self, capacity):
        super(LastUpdatedOrderedDict, self).__init__()
        self._capacity = capacity # 最大长度限制

    def __setitem__(self, key, value):
        '''分为 set 和 add 两种情况：当添加的key在原有的dict中已经存在，则containsKey = True，不删除最早添加项，改变已存在的key的value为新value，长度不变，完成'set'；当添加的key在原有dict中不存在，则containsKey = False，如果超出限制长度，删除最早项，添加最新项, 长度不变，完成'add'，如果未超出限制长度，则不删除最早项，添加最新项，长度增加，完成'add; 添加项沿用父类super().__setitem__(key, value) '''
        containsKey = True if key in self else False
        if len(self) - containsKey >= self._capacity:
            last = self.popitem(last=False)
            print('remove:', last)
        if containsKey:
            del self[key]
            print('set:', (key, value))
        else:
            print('add:', (key, value))
        super().__setitem__(key, value)
```



### 0.2 Python 内建数据类型

Python3 中有六个标准的数据类型：

- Number（数字）包括int、float、[bool](# 4.2 Python布尔值、布尔运算、与或非运算)、[complex](# 4.1 数据类型：复数)
- [String（字符串）](# 4.10 Python字符串)
- [List（列表）](# 4.13 数据类型list)
- [Tuple（元组）](# 4.16 数据类型tuple)
- Set（集合）
- Dictionary（字典）

Python3 的六个标准数据类型中：

- **不可变数据（3 个）：**Number（数字）、String（字符串）、Tuple（元组）；
- **可变数据（3 个）：**List（列表）、Dictionary（字典）、Set（集合）。

### 0.3 简述 with 方法打开处理文件帮我们做了什么？

with 方法打开文件的代码：

```python
with open('/path/to/file', 'r') as f:
    print(f.read())
```

如果文件成功打开，`with`语句会**自动**帮我们调用`close()`方法，保证了只要打开了文件都能正确的关闭文件，避免未关闭的文件对象占用操作系统的资源（且操作系统同一时间能打开的文件数量是有限的）

### 0.4 Python中的可变和不可变数据类型

在0.2中提到，不可变数据类型包括Number(int、float、bool、complex)、String、Tuple，可变数据类型包括List、Dict、Set。分别以`int`和`list`为例，分析两者的**区别**：

#### 1. 不可变数据类型分析

以下面这段对`int`类型数据进行操作的程序为例：

<img src="E:\PythonNote\picture\Id_int.png" alt="id int" style="zoom:80%;" />

`id()`查看的是当前变量的地址值。

由上面例子可以看到：

1. `x=1`、`y=1`两个赋值操作对应的`x`和`y`的地址是一样的，**即`x`和`y`是对同一个对象`1`的引用，也就是说内存中无论有多少引用指向`1`，对象`1`只占用一个地址，且有一个固定的地址值**（Python中有一个引用计数的记录，记录了有多少个引用指向这个地址）；
2. 又注意到，`x=2`的赋值操作，会带来`x`所引用的地址值的改变，因此可以说明，**`x=2`的操作在内存中创建了一个新的对象---`2`，并将`x`指向了这个内存地址，`x`指向的地址值改变**，之后的`y=2`和`z=y`将`x,y,z`指向了同一个对象`2`，因此`x,y,z`的地址值都一样。
3. 当`x`和`y`都被赋值`2`后，**`1`这个对象已经没有引用指向它了，所以`1`这个对象占用的内存，即1627679776地址要被“垃圾回收”**，即1这个对象在内存中已经不存在了。
4. 最后，`x+=2`创建了新的对象`4`，x引用了`4`这个新的对象，而不再引用2这个对象。

上述过程和在[3.2节](# 3.2 变量指向数据的详细操作)用图阐述的过程一样，但更加详细。因此，**不可变**类型可以理解为，**变量引用的地址所代表的这块内存区域存放的值不能被改变**，就像在被回收之前，1627679776地址存放的数据一直是1。为变量赋新值或通过加减的方法改变值等**引起变量指向的值改变的操作，都会引起：另开辟内存区域→更改地址值→创建新的对象→将变量指向新的内存区域→变量引用的地址更改、地址值改变这一系列操作。**

不可变数据类型的优点在于：内存中不管有多少引用，都指向同一个对象，只占用了一块内存；不必担心内存中的值被改变。缺点在于任何改变变量引用的值的操作都必须创建新的对象，导致频繁开辟内存创建对象的可能（不过不再使用的内存会被垃圾回收）。

#### 2. 可变数据类型分析

以下面这段对`list`类型数据进行操作的程序为例：

<img src="E:\PythonNote\picture\id_list.png" alt="id list" style="zoom:80%;" />

1. 两次`a=[1,2,3]`赋值操作，`a`引用的地址值不同，即**创建了两个不同的对象**，这一点明显不同于不可变数据类型，所以对可变对象来说，**具有相同值的对象是不同的对象，在保存在多个不同内存区域中**。这一点也是基于可变数据类型的**可变**考虑的，**因为内存中的值是可变的，但在改变一个对象的值时，避免具有相同值的对象的值也一起改变，因此即便多个对象具有相同的值，也需要放在不同的内存区域里**。

2. 对列表`a`进行`a.append(4)`和`a += [2]`的添加操作，`a`引用对象的值发生了改变，但`a`指向的地址2097021478472不变。说明内存地址不变，对象所占内存中存储的内容已经改变。

3. 更具有代表性的例子在[3.2.1节：一个值得注意的例外：list操作](# 3.2.1 一个值得注意的例外：list操作)中提到，如下图：

   <img src="E:\PythonNote\picture\python_list_wrong.png" alt="python list get wrong" style="zoom:80%;" />

   `listB=listA`操作将l`istA`、`listB`指向同一个对象，当`listA.append(5)`直接改变了内存中存储的值（也就是对象的值），因此必然引起了`listA`、`listB`变量指向的值的同时改变。

因此可变数据类型中的**可变**表示的是，对一个变量进行操作时，**可直接对其引用的对象进行改变而不必创建新的对象**，即地址是不会变的，只是**地址中的内容变化了或者地址得到了扩充**。

#### 3. 总结

不可变数据类型，不允许变量引用的对象的值发生变化，如果改变了变量的值，相当于是新建了一个对象，而对于相同的值的对象，在内存中则只有一个对象，内部会有一个引用计数来记录有多少个变量引用这个对象；

可变数据类型，允许变量的值发生变化，即如果对变量进行append、+=等这种操作后，只是改变了变量的值，而不会新建一个对象，变量引用的对象的地址也不会变化，不过对于具有相同的值的不同对象，则在内存中会开辟不同的区域，即每个对象都有自己的地址，**相当于内存中对于同值的对象保存了多份，这里不存在引用计数，是实实在在的对象**。

总的来说，在Python中，**“一切皆为对象，一切皆为对象的引用”**

### 0.5 Python获取当前日期

使用内置模块[datetime](# 0.1.1 datetime -- 基本的日期和时间类型)

```python
import datetime
today=datetime.date.today()
print(today)
# 2018-01-17
formatted_today=today.strftime('%y%m%d') #datetime类型数据的strftime()方法
print(formatted_today)
# 180117
```

### 0.6 统计字符串每个单词出现的次数













