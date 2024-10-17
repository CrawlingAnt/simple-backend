import aiohttp
import random
import asyncio


def get_random_string(length):
    return ''.join(random.choices('abcdefghijklmnopqrstuvwxyz', k=length))


async def add_python_user():
    async with aiohttp.ClientSession() as session:
        for _ in range(10):
            body = {
                "user_name": get_random_string(5),
                "password": get_random_string(5),
            }
            async with session.post('http://127.0.0.1:8000/users/add', json=body) as response:
                print(await response.text())


# asyncio.run(add_python_user())

data = {
    "user_name": get_random_string(5),
    "password": get_random_string(5),
}

result = {i + '1': data[i] + '1' for i in data}
result_one = [[i, data[i]] for i in data]
result_two = '123'
print(result)
print(result_one)
print(result_two)
