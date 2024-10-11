import asyncio
import aiohttp


async def func1():
    print(1)
    async with aiohttp.ClientSession() as session:
        await session.get("http://127.0.0.1:8000/user/test")
    print('func1 end')
    return 'func1'


async def func2():
    print(2)
    async with aiohttp.ClientSession() as session:
        await session.get("http://127.0.0.1:8000/user")
    print('func2 end')
    return 'func2'


async def main():
    result = await asyncio.gather(func1(), func2())
    print(result)


if __name__ == "__main__":
    asyncio.run(main())
