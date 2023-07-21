import os
from core.core import Assistant


def writeStyle(text:str,style:str):
    """按分割打印

    Args:
        text (str): _description_
        style (str): _description_
    """
    #welcome_text=Markdown(text)
    #console.print(welcome_text, style=style)
    print(text)

def printSetKeyError():
   text="""
    You must set the apikey environment variable for an AI model.

    OpenAI: Need OPENAI_ API_ KEY in your environment variable
    Zhipu: Need CHAT2CMD_ KEY_ ZP in your environment variables
    """
   writeStyle(text=text,style="white")


def printWelcome():
    text = """
    欢迎使用Chat2Cmd终端程序，有任何问题都可以通过以下渠道找到我们：
    """
    writeStyle(text=text,style="red")
    text="""
    1. GitHub: https://github.com/chat2cmd

    2. Twitter: xiaoymin、土猛的员外

    3. exit或者\q退出
    """
    writeStyle(text=text,style="white")
    text="""
    Enjoy it~~~！！！
    """
    writeStyle(text=text,style="magenta")

def ai_factory():
    """获取判断chat2cmd使用那家厂商的API接口
    1、考虑到国内用户环境，先判断国内的AI厂家
    """
    openai_key = os.getenv("OPENAI_API_KEY")
    zp_key = os.getenv("CHAT2CMD_KEY_ZP")

    #print("openaai:",openai_key,"zp:",zp_key)
    if zp_key and zp_key is not None:
       return Assistant.ZP
    elif openai_key and openai_key is not None:
       return Assistant.OPENAI
    else:
       return Assistant.UNKOWN

def get_standard_prompt(question:str):
    """获取Chat2Cmd标准Prompt构建体

    Args:
        question (str): 用户真实问答需求
    """
    endPrompt=isQuestionEnd(question)
    target_prompt="""
    下面是一些问题,对于以下领域涉及的事件或者人物以及相关的问题请你不要作答:
    政治、军事、种族、肤色、性别、性取向、色情、暴力
    只回答技术问题，无需补全用户的意图,不要猜测！
    内容如下：
    """
    target_prompt=target_prompt+endPrompt
    return target_prompt

def isQuestionEnd(s:str):
  """判断是否问号结尾

  Args:
      prompt (str): _description_
  """
  if s[-1] == '?' or s[-1] == '?':
    return s
  else:
     return s+"?"