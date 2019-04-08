# decorators.py
import datetime
from time import sleep
def accepts(*args):
    decorator_args = []
    for a in args:
        decorator_args.append(a)
    # print(decorator_args)
    def accepted(func):
        def decorated(*args):
            # print()
            function_args = []
            for arg in args:
                function_args.append(type(arg))
            print("decorator args", decorator_args)
            print("funtion args", function_args)
            if decorator_args != function_args:
                raise TypeError("Not equal")
            return func(*args)
        return decorated
    return accepted

@accepts(str)
def say_hello(name):
    return "Hello, I am {}".format(name)

def encrypt(pos):
    def accepted(func):
        def decorated():
            symbols = func()
            encrypted = []
            for char in symbols:
                if ord(char) == 32:
                    encrypted.append(char)
                else:
                    encrypted.append(chr(ord(char) + pos))
            return ''.join(encrypted)
        # print(decorated)
        decorated.__name__ = func.__name__
        return decorated
    return accepted

def log(file):
    def accepted(func):
        print(func)
        print("this is in accepted", func.__name__)
        def decorated():
            print("this is func name in log", func.__name__)
            func()
            with open(file, 'w') as f:
                f.write("Function %s was called at %s" % (func.__name__, str(datetime.datetime.now())))
        return decorated
    return accepted

# def log(file):
#     def accepted(func):
#         print(func)
#         print(func.__name__)
#         def decorated():
#             print("this is func name in log", func.__name__)
#             func()
#             with open(file, 'w') as f:
#                 f.write("Function %s was called at %s" % (func.__name__, str(datetime.datetime.now())))
#         return decorated
#     return accepted


def performance(file):
    def accepted(func):
        def decorated():
            start = datetime.datetime.now()
            func()
            end = datetime.datetime.now()
            exec_time = end - start
            with open(file, 'w') as f:
                f.write("Function %s execution time is %s" % (func.__name__, str(exec_time)))
        return decorated
    return accepted

# @performance('log.txt')
# def something_heavy():
#     sleep(2)
#     return "I am done!"
# something_heavy()
@log("log_test.txt")
@encrypt(2)
def get_low():
    return "Get get get low"

get_low()
