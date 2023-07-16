import os
import sys
#from rich.console import Console
#from rich.markdown import Markdown

from openai_call import generate_stream

#console = Console()

def writeStyle(text:str,style:str):
    """按分割打印

    Args:
        text (str): _description_
        style (str): _description_
    """
    #welcome_text=Markdown(text)
    #console.print(welcome_text, style=style)
    print(text)


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

def query(prompt):
  openai_key = os.getenv("OPENAI_API_KEY")
  #print('prompt:',prompt)
  if not openai_key:
    print("OPENAI_API_KEY environment variable not set")
    return
  if prompt.strip():
    generate_stream(prompt=prompt)
    #换一行
    print("\n")

def main():
  if len(sys.argv) > 1:
    # 直接调用模式
    query(' '.join(sys.argv[1:]))
  else:
    # chat2cmd 模式
    #print("Enter chat2cmd mode. Type quit to exit.") 
    printWelcome()
    while True:
      try:
        user_input = input("chat2cmd->")
        if user_input.lower() == 'quit' or user_input=="exit" or user_input=="\q":
          break
        
        query(user_input)

      except (KeyboardInterrupt, EOFError):
        print('error')
        break

if __name__ == '__main__':
  main()