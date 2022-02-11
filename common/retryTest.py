# coding=utf-8
import sys
import functools
import traceback
import inspect
import unittest


def retry(target=None, max_n=1, func_prefix="test"):
    """
    一个装饰器，用于unittest执行测试用例出现失败后，自动重试执行

# example_1: test_001默认重试1次
class ClassA(unittest.TestCase):
    @retry
    def test_001(self):
        raise AttributeError


# example_2: max_n=2,test_001重试2次
class ClassB(unittest.TestCase):
    @retry(max_n=2)
    def test_001(self):
        raise AttributeError


# example_3: test_001重试3次; test_002重试3次
@retry(max_n=3)
class ClassC(unittest.TestCase):
    def test_001(self):
        raise AttributeError

    def test_002(self):
        raise AttributeError


# example_4: test_102重试2次, test_001不参与重试机制
@retry(max_n=2, func_prefix="test_1")
class ClassD(unittest.TestCase):
    def test_001(self):
        raise AttributeError

    def test_102(self):
        raise AttributeError


    :param target: 被装饰的对象，可以是class, function
    :param max_n: 重试次数，没有包含必须有的第一次执行
    :param func_prefix: 当装饰class时，可以用于标记哪些测试方法会被自动装饰
    :return: wrapped class 或 wrapped function
    """

    def decorator(func_or_cls):
        if inspect.isfunction(func_or_cls):
            @functools.wraps(func_or_cls)
            def wrapper(*args, **kwargs):
                n = 0
                while n <= max_n:
                    try:
                        n += 1
                        func_or_cls(*args, **kwargs)
                        if not n == 1:
                            print('经过第', n, '次重试',func_or_cls)
                        return
                    except Exception:
                        if n <= max_n:
                            trace = sys.exc_info()
                            traceback_info = str()
                            for trace_line in traceback.format_exception(trace[0], trace[1], trace[2], 3):
                                traceback_info += trace_line
                            print(traceback_info)
                            args[0].tearDown()
                            args[0].setUp()
                        else:
                            raise

            return wrapper
        elif inspect.isclass(func_or_cls):
            for name, func in list(func_or_cls.__dict__.items()):
                if inspect.isfunction(func) and name.startswith(func_prefix):
                    setattr(func_or_cls, name, decorator(func))
            return func_or_cls
        else:
            raise AttributeError

    if target:
        return decorator(target)
    else:
        return decorator


class Retry(object):
    """
    类装饰器, 功能与Retry一样


# example_1: test_001默认重试1次
class ClassA(unittest.TestCase):
    @Retry
    def test_001(self):
        raise AttributeError


# example_2: max_n=2,test_001重试2次
class ClassB(unittest.TestCase):
    @Retry(max_n=2)
    def test_001(self):
        raise AttributeError


# example_3: test_001重试3次; test_002重试3次
@Retry(max_n=3)
class ClassC(unittest.TestCase):
    def test_001(self):
        raise AttributeError

    def test_002(self):
        raise AttributeError


# example_4: test_102重试2次, test_001不参与重试机制
@Retry(max_n=2, func_prefix="test_1")
class ClassD(unittest.TestCase):
    def test_001(self):
        raise AttributeError

    def test_102(self):
        raise AttributeError

    """

    def __new__(cls, func_or_cls=None, max_n=1, func_prefix="test"):
        self = object.__new__(cls)
        if func_or_cls:
            self.__init__(func_or_cls, max_n, func_prefix)
            return self(func_or_cls)
        else:
            return self

    def __init__(self, func_or_cls=None, max_n=1, func_prefix="test"):
        self._prefix = func_prefix
        self._max_n = max_n

    def __call__(self, func_or_cls=None):
        if inspect.isfunction(func_or_cls):
            @functools.wraps(func_or_cls)
            def wrapper(*args, **kwargs):
                n = 0
                while n <= self._max_n:
                    try:
                        n += 1
                        func_or_cls(*args, **kwargs)
                        return
                    except Exception:  # 可以修改要捕获的异常类型
                        if n <= self._max_n:
                            trace = sys.exc_info()
                            traceback_info = str()
                            for trace_line in traceback.format_exception(trace[0], trace[1], trace[2], 3):
                                traceback_info += trace_line
                            print(traceback_info)  # 输出组装的错误信息
                            args[0].tearDown()
                            args[0].setUp()
                        else:
                            raise

            return wrapper
        elif inspect.isclass(func_or_cls):
            for name, func in list(func_or_cls.__dict__.items()):
                if inspect.isfunction(func) and name.startswith(self._prefix):
                    setattr(func_or_cls, name, self(func))
            return func_or_cls
        else:
            raise AttributeError

    # TODO 重试机制需配合重新打开APP相关函数(配合判断APP状态)解决卡死相关问题