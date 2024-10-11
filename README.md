aerich init -t settings.orm.tortoise_orm
aerich init-db
aerich migrate --name 'init'
aerich upgrade
aerich downgrade

alembic init alembic
alembic revision --autogenerate -m "Initial migration"
alembic upgrade head
alembic downgrade

## 部署说明

1. 确保已安装 Docker

2. 构建 Docker 镜像：
   ```
   docker build --build-arg DOCKER_REGISTRY_MIRROR=https://docker.mirrors.ustc.edu.cn -t simple-backend .
   ```
   注意：你可以根据需要更改镜像加速器的 URL。

3. 运行 Docker 容器：
   ```
   docker run -d -p 8000:8000 simple-backend
   ```

4. 访问 http://localhost:8000 验证应用是否正在运行

## 故障排除

如果在构建过程中仍然遇到网络问题，可以尝试以下方法：

1. 重新运行 `docker build` 命令
2. 尝试使用不同的镜像加速器，例如：
   ```
   docker build --build-arg DOCKER_REGISTRY_MIRROR=https://hub-mirror.c.163.com -t simple-backend .
   ```
3. 使用缓存：`docker build --cache-from python:3.11 -t simple-backend .`
4. 尝试使用不同的基础镜像，如 `python:3.11-alpine`
5. 重启 Docker 守护进程

## 常见问题

yield 配合next使用，遇到yield会暂停代码，等待下次的执行再继续执行。

```python
from time import sleep


def fun_a():
    while True:
        print("a函数")
        yield
        sleep(10)


def fun_b(obj):
    while True:
        print("b函数")
        next(obj)
        print("b函数结束")


a = fun_a()
fun_b(a)
```

lambda函数适用于简短的操作，最好不要赋值给一个变量，再去调用，这样不容易解读，下面的使用场景是可以的。lambda x, y: x +
y。这个lambda函数接受两个参数x和y，并返回它们的和。

```python
numbers = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]
sorted_numbers = sorted(numbers, key=lambda x: x % 2)
```


# asyncio的出现是因为Python默认就是同步的和js是反的，asyncio的出现就是为了解决这个问题。 下面的fun1和main2是同步的，如果fun1需要5秒，main2需要等待fun1执行完再执行。
```python
import requests

def fun1():
    result = requests.get("http://127.0.0.1:8000/user/test")
    print(result.json())


def main2():
    result = requests.get("http://127.0.0.1:8000/user")
    print(result.json())


fun1()
main2()
```

# requests 是同步的，aiohttp 是异步的，request是会阻塞进程，除非获取到返回结果，不然会一直阻塞
```python
import asyncio
import aiohttp

async def func1():
    print(1)
    async with aiohttp.ClientSession() as session:
        await session.get("http://127.0.0.1:8000/user/test")
    print('func1 end')

async def func2():
    print(2)
    async with aiohttp.ClientSession() as session:
        await session.get("http://127.0.0.1:8000/user")
    print('func2 end')


async def main():
    task1 =  asyncio.create_task(func1())
    task2 =  asyncio.create_task(func2())

    # result = await asyncio.gather(func1(), func2()) 类似于promise.all
    await task1
    await task2

if __name__ == "__main__":
    asyncio.run(main())
```


