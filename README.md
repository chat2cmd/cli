# Chat2cmd Cli

本项目为`chat2cmd`的客户端，`Cli`基于Rust开发，具有高性能、体积小和响应速度快等特点。用户可以通过[多种方式](#)下载、安装和使用，适用于Windows、Linux、Mac等主流操作系统。

------

> 关于Chat2cmd的详细信息，可访问:[https://chat2cmd.com](https://chat2cmd.com)（暂未开通）。

## 前置准备

目前[v0.0.1](https://github.com/chat2cmd/cli/releases/tag/v0.0.1)版本已经发布，是一个最小可用版本，不过有几个前置条件：

1、你需要有OpenAI的KEY，并且设置在你的**系统环境变量**中，变量名称为：`OPENAI_API_KEY`，值为KEY

2、保证能直接访问OpenAI的接口，如果不想走全局，可以设置代理

3、设置代理，如果国内用户可以将代理软件的IP、HOST也同样设置在**系统环境变量**中

- 代理HOST：变量:`OPENAI_PROXY_HOST`,设置为你本机或者VPN地址IP
- 代理PORT：变量：`OPENAI_PROXY_PORT`,设置为代理VPN的PORT值

## Getting Started

### 直接上手

在shell/cmd等工具上，直接使用.

````shell
[user@linux ~]# chat2cmd 如何将本地文件上传给远程服务器
````


### 介绍

技术栈：

- [requests](https://requests.readthedocs.io/en/latest/)
- [pyinstaller](https://pyinstaller.org/en/stable/)

### 安装

```python
pip freeze > requirements.txt
```


### 基本用法

#### 获取Auth_key

### 高级用法

### FAQ
