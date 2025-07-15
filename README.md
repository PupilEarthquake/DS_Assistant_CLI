# DS on Terminal（EN）

![demo](demo.gif)

A tool for invoking DeepSeek's API and chatting in the terminal on Linux platforms.

## Requirements

`Python 3` with the following libraries installed:
```
opneai
numpy
prompt_tookit
```
See `requirements.txt` for details (or just install it).

## Installation

1. Download the source code and install required libraries.
2. Create a symbolic link: `sudo ln -s /path/to/your/ds.py /usr/local/bin/ds`.

## Usage

Simple commands:
1. `ds ls` lists historical chats.
2. `ds load -d <chat date> -n <chat title>` loads a chat to provide AI with conversation memory.
3. `ds new -n <chat title>` creates a new chat session.
4. `ctrl + d` to send the message.


## Features
Chat records are stored in both `.json` and `.md` formats within the `messages` directory, located in the same path as `/path/to/your/ds.py`



# 中文版介绍

一个Linux平台下在终端调用DEEPSEEK的API并且聊天的工具.

## 要求

Python3且安装了如下库：
```
openai
numpy
prompt_toolkit
```

具体可见requirements.txt

## 安装

1. 下载源代码, 安装需要的库.
2. 创建符号链接: `sudo ln -s /path/to/your/ds.py /usr/local/bin/ds`


## 使用

命令很简单:
1. `ds ls`可以列出历史聊天.
2. `ds load -d <chat date> -n <chat title>`可以加载一个聊天, 以使AI获取聊天记忆.
3. `ds new -n <chat title>`可以创建一个新的聊天. 
4. `ctrl + d`发送信息


## 特性
聊天记录分别以`.json`和`.md`格式储存. 放置在与`/path/to/your/ds.py`同一路径下的`messages`中.




