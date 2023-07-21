import uuid
import jwt
import time
import os
import zhipuai
import sys

from utils import cmd_utils


zp_key = os.getenv("CHAT2CMD_KEY_ZP")


def generate_token(apikey: str, exp_seconds: int):
    """获取智谱AI的Authorization

    Args:
        apikey (str): 智谱密钥key
        exp_seconds (int): 失效时间

    Raises:
        Exception: _description_

    Returns:
        _type_: 智谱Ai所需要的Authorization
    """
    try:
        id, secret = apikey.split(".")
    except Exception as e:
        raise Exception("invalid apikey", e)
 
    payload = {
        "api_key": id,
        "exp": int(round(time.time() * 1000)) + exp_seconds * 1000,
        "timestamp": int(round(time.time() * 1000)),
    }
    return jwt.encode(
        payload,
        secret,
        algorithm="HS256",
        headers={"alg": "HS256", "sign_type": "SIGN"},
    )

def generate_stream(prompt:str):
    url="https://open.bigmodel.cn/api/paas/v3/model-api/chatglm_std/sse-invoke"
    user_prompt={
        "role":"user",
        "content":cmd_utils.get_standard_prompt(question=prompt)
    }
    #print(user_prompt)
    prompt=[]
    prompt.append(user_prompt)
    zhipuai.api_key=zp_key
    response=zhipuai.model_api.sse_invoke(model="chatglm_std",
                                         prompt=prompt,top_p=0.7,
        temperature=0.9)
    for event in response.events():
        if event.event == "add":
            #print(event.data)
            print(event.data, end='') # print并保留在同一行
            sys.stdout.flush() # 强制刷新标准输出
        elif event.event == "error" or event.event == "interrupted":
            print(event.data, end='') # print并保留在同一行
        elif event.event == "finish":
            print(event.data, end='') # print并保留在同一行
        else:
            print(event.data, end='') # print并保留在同一行

#zp_generation("curl如何发送文件")