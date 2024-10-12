import aiohttp
import random
import asyncio

async def add_user():
  async with aiohttp.ClientSession() as session:
    for i in range(11,15):
      async with session.post('http://localhost:8000/user/add',json={'user_name':f'user{i}', 'password':str(random.randint(100000,999999))}) as response:
        print(await response.text())

asyncio.run(add_user())