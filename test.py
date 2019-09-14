import time

def test():
    print('hello from the testing world')
    print('it is ' + str(time.time()))
    if 2 > 1:
        return 0
    else:
        return 1

test()
