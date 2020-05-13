import abc


class AbstractFactroy(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def func_a(self):
        pass

    @abc.abstractmethod
    def func_b(self):
        pass


class ConcreteClassA(AbstractFactroy):
    def func_a(self):
        print('func_a from ConcreteClassA')

    def func_b(self):
        print('func_b from ConcreteClassA')


class ConcreteClassB(AbstractFactroy):
    def func_a(self):
        print('func_a from ConcreteClassB')

    def func_b(self):
        print('func_b from ConcreteClassB')


class OperatorClass:
    def __init__(self, factory):
        self.a = factory.func_a
        self.b = factory.func_b

    def play(self):
        self.a()
        self.b()


if __name__ == '__main__':
    sc_a = ConcreteClassA()
    sc_b = ConcreteClassB()

    abc_factory = OperatorClass(sc_b)
    abc_factory.play()
