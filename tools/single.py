class Singleton(type):

    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super(
                Singleton, cls).__call__(*args, **kwargs)
        return cls._instances[cls]


class T(metaclass=Singleton):
# class T(object):
    def __init__(self):
        print('init')


test = T()
test = T()
test = T()
test = T()
test = T()
