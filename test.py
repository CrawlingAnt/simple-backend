import aiohttp
import random
import asyncio

def get_random_string(length):
    return ''.join(random.choices('abcdefghijklmnopqrstuvwxyz', k=length))

async def add_java_user():
  async with aiohttp.ClientSession() as session:
    for _ in range(10):
      body = {
        "status": 1,
        "mchCode": get_random_string(5),
        "organizationId": get_random_string(5),
        "storeNo": get_random_string(5),
        "systemId": get_random_string(5),
        "paymentKey": get_random_string(5),
        "interfaceKey": get_random_string(5),
      }
      async with session.put('https://managementtestpay.cmskscy.com/stage-api/open/mch',json=body,headers={"Authorization": "eyJhbGciOiJIUzUxMiJ9.eyJsb2dpbl91c2VyX2tleSI6IjEzY2M4NDRjLTRlMTYtNGIxYS05ZTRhLWM1Mjc5NzJiNjQ3NyJ9.3WNup2gXT1I0xhkPDqfkMDIAaPtIm9NecqZzaZwq09fMI9ZId0iM67OCaPdI08dQfEbmIfUZiY9K7bBSsCbOww"}) as response:
        print(await response.text())
  print("done")


async def add_python_user():
  async with aiohttp.ClientSession() as session:
    for _ in range(10):
      body = {
        "user_name": get_random_string(5),
        "password": get_random_string(5),
      }
      async with session.post('http://127.0.0.1:8000/user/add',json=body) as response:
        print(await response.text())
