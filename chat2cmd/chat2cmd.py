import sys

from utils import cmd_utils
from ai import zp_call,openai_call
from core.core import Assistant


def query(prompt):
  ai=cmd_utils.ai_factory()
  if ai==Assistant.UNKOWN:
    cmd_utils.printSetKeyError()
    return
  if prompt.strip():
    try:
      if ai==Assistant.OPENAI:
        openai_call.generate_stream(prompt=prompt)
      elif ai==Assistant.ZP:
        zp_call.generate_stream(prompt=prompt)
    except:
      print("该问题无法获取答案或网络异常,请重试.")
    #换一行
    print("\n")

def main():
  if len(sys.argv) > 1:
    # 直接调用模式
    query(' '.join(sys.argv[1:]))
  else:
    # chat2cmd 模式
    #print("Enter chat2cmd mode. Type quit to exit.") 
    cmd_utils.printWelcome()
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