import asyncio


async def fun(i):
    print(i)


loop = asyncio.run(fun(1))
