class FluentBuilderClass:
    def __init__(self, builder=None):
        self.status_a = builder.status_a
        self.status_b = builder.status_b

    def __str__(self):
        result_a = 'yes' if self.status_a else 'no'
        result_b = 'yes' if self.status_b else 'no'
        info = (f'Status_A: {result_a}', f'Status_B: {result_b}')
        return '\n'.join(info)

    class InnerBuilder:
        def __init__(self):
            print('InnerBuild->', end='')
            self.status_a = False
            self.status_b = False

        def a(self):
            print('a->', end='')
            self.status_a = True
            return self

        def b(self):
            print('b->', end='')
            self.status_b = True
            return self

        def build(self):
            print('build')
            return FluentBuilderClass(self)


# a, b의 순서에 상관없이 둘다 실행된다.
# 단, a와 b의 실행 순서가 프로그램에 영향을 미칠 경우 순서에 맞게 실행해야한다.
# builder_class = FluentBuilderClass.InnerBuilder().b().a().build()
builder_class = FluentBuilderClass.InnerBuilder().b().a().build()
print(builder_class)
