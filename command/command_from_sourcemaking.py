"""
Sourcemaking에서 제공하는 기본적인 command pattern 예제
Encapsulate a request as an object, thereby letting you parameterize
clients with different requests, queue or log requests, and support
undoable operations.
"""

import abc


# 주문을 받는 웨이터
class Invoker:
    """
    request에 대한 처리를 command에 요청
    """
    def __init__(self):
        # 볶음밥, 자장면, 만두 등..
        self._commands = []

    def store_command(self, command):
        self._commands.append(command)

    def execute_commands(self):
        for command in self._commands:
            command.execute()


# 주문서(command interface)
class Command(metaclass=abc.ABCMeta):
    """
    Declare an interface for executing an operation.
    """
    def __init__(self, receiver):
        self._receiver = receiver

    @abc.abstractmethod
    def execute(self):
        pass


# 요리 제작이 담긴 주문서
class ConcreteCommand(Command):
    """
    Receiver 객체와 동작에 대한 연결을 정의 - 주문서와 주문서에 적힌 요리법을 바인딩
    (ConcreteCommand(볶음밥) --binding--> Receiver(볶는다))
    -> execute()를 통해 일치하는 Receiver의 동작 실행
    """
    def execute(self):
        # 볶는다
        self._receiver.action()


# 실제 요리 제작
class Receiver:
    """
    요청에 대한 처리를 담고있는 클래스
    """
    # 볶는다
    def action(self):
        pass


def main():
    # 볶는 방법
    receiver = Receiver()
    # 볶는 방법(receiver)과 주문서에 적힌 볶음밥(ConcreteCommand)을 바인딩
    concrete_command = ConcreteCommand(receiver)
    # 웨이터 호출
    invoker = Invoker()
    # 명령: 밥을 볶아서 볶음밥을 만드시오
    invoker.store_command(concrete_command)
    invoker.execute_commands()


if __name__ == "__main__":
    main()
