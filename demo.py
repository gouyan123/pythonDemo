# def lazy_sum(*args):
#     def sum():  ## 当调用lazy_sum(*args)函数时，sum()函数并不会执行，因为lazy_sum(*args)里面只是定义了sum()函数，并没有调用sum()函数
#         a = 0
#         for n in args:
#             a = a + n
#         return a
#     return sum  ## sum是一个变量，指向sum()函数体
#
# f = lazy_sum(1,2,3,4,5) ## f是一个变量，指向sum()函数体；
# print(f())

# l = list(map(lambda x : x * x,[1,2,3]))
# print(l)

import time
def timer(func):
    def deco():
        start = time.time()
        func()
        stop = time.time()
        print(stop - start)
    return deco

@timer
def test():
    time.sleep(2)
    print('test is running')
test()
