import os
import requests
import json
import sys
import re


openai_key = os.getenv("OPENAI_API_KEY")
model_engine = "text-davinci-003"


def getProxy():
    """获取代理信息
    """
    openai_proxy_host = os.getenv("OPENAI_PROXY_HOST")
    openai_proxy_port = os.getenv("OPENAI_PROXY_PORT")
    #print('host:',openai_proxy_host,"port:",openai_proxy_host)
    if openai_proxy_host is not None and openai_proxy_port is not None:
       host_url="http://"+openai_proxy_host+":"+openai_proxy_port
       return {
          "http":host_url,
          "https":host_url
       }
    return {}

def isQuestionEnd(s:str):
  """判断是否问号结尾

  Args:
      prompt (str): _description_
  """
  if s[-1] == '?' or s[-1] == '?':
    return s
  else:
     return s+"?"

def generate_stream(prompt):
  url = f"https://api.openai.com/v1/engines/{model_engine}/completions"

  headers = {
    "Content-Type": "application/json",
    "Authorization": f"Bearer {openai_key}"
  }
  endPrompt=isQuestionEnd(prompt)

  target_prompt="""
  下面是一些问题,对于以下领域涉及的事件或者人物以及相关的问题请你不要作答:
  政治、军事、种族、肤色、性别、性取向、色情、暴力
  只回答技术问题，无需补全用户的意图,不要猜测！
  内容如下：
  """
  target_prompt=target_prompt+endPrompt
  #print(target_prompt)
  data = {
    "prompt": target_prompt,
    "max_tokens": 1024,
    "temperature": 0.5,
    "top_p": 1,
    "frequency_penalty": 0,
    "presence_penalty": 0,
    "stream": True       
  }
  host_proxy=getProxy()

  #print('host_proxy:',host_proxy)

  with requests.post(url, headers=headers, json=data,
  proxies=getProxy(), stream=True) as response:
    line_arr=[]
    for line in response.iter_lines():
      if line:
        stream = line.decode("utf-8")[6:]
        if stream == "[DONE]":
            break
        json_response = json.loads(stream)
        text = json_response['choices'][0]['text']
        print(text, end='') # print并保留在同一行
        sys.stdout.flush() # 强制刷新标准输出
        
#prompt = "scp命令如何上传本地文件到服务器"  

#generate_stream(prompt)