class Singleton(type):
    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super(Singleton, cls).__call__(*args, **kwargs)
            print('a', cls._instances)
        else:
            cls._instances[cls].__init__(*args, **kwargs)
            print('b', cls._instances)

        return cls._instances[cls]


class Database(metaclass=Singleton):

    def __init__(self):
        self.var = None


a = Database()
b = Database()
print(id(a), id(b))
