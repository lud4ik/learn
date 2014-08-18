# -*- coding: utf-8 -*-


class Singleton(type):

    def __init__(cls, name, bases, dst):
        super(Singleton, cls).__init__(name, bases, dst)
        cls._instance = None

    def __call__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = super(Singleton, cls).__call__(*args, **kwargs)
        return cls._instance


class Example(object):
    __metaclass__ = Singleton


def rev(s):
    return s[-1] + rev(s[:-1]) if s else ''


if __name__ == "__main__":
    print rev('123456789')
    for i in range(10):
        obj = Example()
        print obj, id(obj)
