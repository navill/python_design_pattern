# advanced python programming from
# https://legacy.python.org/workshops/1997-10/proceedings/savikko.html
class Event:
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return self.name


class Widget:
    def __init__(self, parent=None):
        self.parent = parent

    # event에 A가 들어왔을 경우
    def handle(self, event):
        # handler = handle_A
        handler = f'handle_{event}'
        # __dict__에 handle_A가 있는지 확인
        if hasattr(self, handler):
            # getattr(self, handler) -> handler_A와 일치하는 값을 __dict__로부터 가져옴
            method = getattr(self, handler)
            # method(event) == handler_A(event)
            method(event)
        elif self.parent is not None:
            # 부모 클래스가 있을 경우 부모 클래스에서 handle 메서드를 실행
            self.parent.handle(event)
        elif hasattr(self, 'handle_default'):
            self.handle_default(event)


class MainWindow(Widget):
    def handle_close(self, event):
        print(f'MainWindow: {event}')

    def handle_default(self, event):
        print(f'MainWindow Default: {event}')


class SendDialog(Widget):
    def handle_paint(self, event):
        print(f'SendDialog: {event}')


class MsgText(Widget):
    def handle_down(self, event):
        print(f'MsgText: {event}')


def main():
    mw = MainWindow()  # parent: Widget
    sd = SendDialog(mw)  # parent: MainWindow(widget)
    msg = MsgText(sd)  # parent: SendDialog(MainWindow(widget))

    for e in ('down', 'paint', 'unhandled', 'close'):
        evt = Event(e)
        print(f'Sending event -{evt}- to MainWindow')
        mw.handle(evt)
        print(f'Sending event -{evt}- to SendDialog')
        sd.handle(evt)
        print(f'Sending event -{evt}- to MsgText')
        msg.handle(evt)


if __name__ == '__main__':
    main()
