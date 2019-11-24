class LazyProperty:
    def __init__(self, method):
        self.method = method
        self.method_name = method.__name__
        print('b', self.method)
        # print(f"function overriden: {self.fget}")
        # print(f"function's name: {self.func_name}")

    # self : LazyProperty object
    # obj : Test object
    # cls : Test
    def __get__(self, obj, cls):
        if not obj:
            return None
        # self.method(obj) == LazyProperty.resource(Test object)
        value = self.method(obj)
        # print(f'value {value}')
        setattr(obj, self.method_name, value)  # 3
        # class Test:
        #     self.resource = value
        print('a',self.method)
        return value


class Test:
    def __init__(self):
        self.x = 'foo'
        self.y = 'bar'
        self._resource = None
        # self.resource <= setattr(Test, LazyProperty.method_name, tuple(range(5))  # 4

    @LazyProperty
    def resource(self):
        print(f'initializing self._resource which is: {self._resource}')
        self._resource = tuple(range(5))  # expensive
        return self._resource


def main():
    t = Test()  # 1
    print(t.x)
    print(t.y)
    # do more work...
    # @LazyProperty 실행 -> return tuple(range5))
    print(t.resource)  # 2, 5
    print(t.resource)  # 6


if __name__ == '__main__':
    main()
