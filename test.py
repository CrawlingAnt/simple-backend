from time import sleep

def test():
    for i in range(1, 5):
        print(i)
        yield i


s = test()
while True:
    try:
        next(s)
        sleep(2)
    except StopIteration:
        break
