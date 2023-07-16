# Chat2cmd Cli

本项目为`chat2cmd`的客户端，`Cli`基于Rust开发，具有高性能、体积小和响应速度快等特点。用户可以通过[多种方式](#)下载、安装和使用，适用于Windows、Linux、Mac等主流操作系统。

------

> 关于Chat2cmd的详细信息，可访问:[https://chat2cmd.com](https://chat2cmd.com)（暂未开通）。

## 前置准备

目前v0.0.1版本已经发布，是一个最小可用版本，不过有几个前置条件：

1、你需要有OpenAI的KEY，并且设置在你的**系统环境变量**中，变量名称为：`OPENAI_API_KEY`，值为KEY

2、保证能直接访问OpenAI的接口，如果不想走全局，可以设置代理

3、设置代理，如果国内用户可以将代理软件的IP、HOST也同样设置在**系统环境变量**中

- 代理HOST：变量:`OPENAI_PROXY_HOST`,设置为你本机或者VPN地址IP
- 代理PORT：变量：`OPENAI_PROXY_PORT`,设置为代理VPN的PORT值

## Getting Started

### 直接上手

在shell/cmd等工具上，直接使用.

````shell
[user@linux ~]# cc -c 如何将本地文件上传给远程服务器
````

在shell/cmd等工具的下一行开始，返回结果，结果一般有三类：

#### 01.准确结果

返回直接可以使用的prompt，用户回车即可执行。注：非幂等prompt需要用户输入`y`确认。

```shell
[user@linux ~]# du -h --max-depth=0   //查看当前目录使用的总空间大小
```

```shell
[user@linux ~]# mkdir log_dir ?  //需要输入y才能执行命令
```

#### 02.建议结果

返回建议内容，可能包含多个选择，或者需要用户自行选择的结果，不直接产生效用。

#### 03.填空结果

返回prompt，但其中几个变量需要用户自行填写，如`scp -r {files} {user}@{remote_url}:/{remote_path}`；



### 初次登录需要授权

#### 获取auth_key

在https://www.chat2cmd.com 注册之后，可以在任何可联网的shell/cmd上使用以下命令获取`auth_key`.

```shell
[user@linux ~]# cc -u username -p
[chat2cmd:username]password:
```

prompt会提示输入隐藏状态的密码。如果验证正确，系统会返回:

```shell
[user@linux ~]# auth_key(username):1nc889hWc810plx2jhfhaksqwyd73r123jfbuqgca
```



#### 设置auth_key

将获得的auth_key进行授权设置，可以让用户该IP所在的shell/cmd上使用chat2cmd时无需再进行验证。

```shell
[user@linux ~]# cc -a 1nc889hWc810plx2jhfhaksqwyd73r123jfbuqgca
```

也可以在获取auth_key的时候直接授权，如下：

```shell
[user@linux ~]# cc -u username -p -a
[chat2cmd:username]password:
```

【未完待续】

### 介绍

技术栈：

- [LangChain](https://github.com/hwchase17/langchain)
- [Rich](https://github.com/Textualize/rich)
- [python-prompt-toolkit](https://github.com/prompt-toolkit/python-prompt-toolkit)

### 安装

```python
pip freeze > requirements.txt
```


### 基本用法

#### 获取Auth_key

### 高级用法

### FAQ
