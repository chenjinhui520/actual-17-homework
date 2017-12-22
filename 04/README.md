### 第四次作业
####基于文件存储的交互式用户登录注册系统
1. 用户注册 
> 用户注册，将注册信息写入文件，供用户登录读取使用。 
> 文件保存用户格式：users.txt
>nick:111
2. 要求如下：
> 输入用户名不能为空，否则提示错误信息并退出，
> 用户名正确后，提示用户输入两次密码，
> 两次密码不一致，提示错误，
> 以上都ok则将用户注册信息保存到文件中。 （目前不考虑用户名重复问题）
#### 根据列表里每个元组中最大值进行排序（简单）
1. 题目
> [(1, 3), (4, 7), (2, 5), (2, 1), (6, 2), (4, 1)]
> 期待结果：[(2, 1), (1, 3), (4, 1), (2, 5), (6, 2), (4, 7)]
2. 要求：用sorted和lambda完成
> 级别1：用lambda中用max
> 级别2：lambda中不用max	（思路：自己写一个max函数）