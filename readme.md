# 说明文档

这个文档是对于本小组设计的分布式温控系统的一点简单说明，包括简单的使用手册，以及从宏观上的系统总体功能实现和设计框架文件说明两个方面的简单阐述。

## 0. 使用说明
在mysql数据库里创建名为hotel的database，然后使用 `建表sql语句.txt`中的内容进行建表。与数据库连接相关的代码可在 `database.py`里看到，如下：

```python
db = py.connect(
    host="127.0.0.1",
    port=3306,
    user="root",
    password="123456",
    database="hotel",
    charset="utf8"
)
```

准备好相应数据库后，安装代码中所需要的python第三方模块，然后运行 `main.py` 便可直接启动我们的分布式温控系统，时间线推进，真实时间每30s对应一个系统时间单位（min）。

## 1．系统总体功能实现
本组6个人通力合作，在要求的时间范围之内，撰写设计文档，不断调整与改善，成功开发出了满足系统需求的酒店分布式
温控系统，该系统满足如下各个用户的不同使用需求，也就是在用例模型设计中的各个用例，可以说是功能比较完备。
- 客户的入住退房，调节空调参数用例
- 空调管理员的监控酒店空调状态，房间空调状态的用例
- 酒店前台的查询账单详单用例
- 酒店经理的查询报表用例

## 2. 设计框架与文件解释
本组使用的开发语言是python，在前端使用pyqt库设计了图形化界面作为UI层，用户可以选择不同的身份登录，并选择不同功能的服务进行对应的实现；
在后端使用pymysql库连接本地搭建了的mysql数据库服务，并通过数据表单来存储在程序运行调度算法执行的过程中的各种数据的实时更新。沟通
前端和后端的是控制器层和应用层这两层，程序最为核心的服务器和调度器就位于应用层，通过调度器执行调度算法完成各个时刻正确的送风调度，在
调度的同时会向数据库持久化，完成相应表单数据的插入与更新。文件部分，图像界面主要是各个对应的UI文件，这个是整个UI中的各个页面，共同
拼接组成我们的前端界面，界面与界面之间根据用户选择进行灵活跳转。Py文件的话是我们开发代码的文件，一共是四个，具体内容与功能如下所示。

- `main.py`: UI层对应的文件。使用转换工具pyunic将qt设计的各个页面都转换成python的类进行存放，存放用户类，完成分布式温控系统的配置和初始化。
运行 `main.py` 即可直接启动我们的分布式温控系统，时间线推进 真实时间每30s对应一个系统时间单位（min）。
-  `controller.py`: 控制器层对应的文件。存放各种控制器类。
-  `application.py`: 应用层对应的文件。存放空调子机，空调主机，服务对象和调度对象的类，调度对象对应会执行对应的调度算法。
-  `database.py`: 持久化层对应的文件。存放DBMapper类，连接本地对应数据库，封装各种与数据库表单之间的CRUD函数，便于前面
几层在程序执行，系统时间线推进，调度算法执行的同时完成和本地数据库的交互。
