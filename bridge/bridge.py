import abc
import urllib.parse
import urllib.request


# 구현(abstraction)과 기능(implementator)을 분리
# Resource Content abstraction - 추상 객체를 받을 abstraction
class ResourceContent:
    """
    Define the abstraction's interface.
    Maintain a reference to an object which represents the Implementor.
    """

    def __init__(self, imp):
        self._imp = imp

    def show_content(self, path):
        self._imp.fetch(path)


# Implemenator - 실행을 위한 interface
class ResourceContentFetcher(metaclass=abc.ABCMeta):
    """
    Define the interface (Implementor) for implementation classes that help fetch content.
    """

    @abc.abstractmethod
    def fetch(path):
        pass


# implementation
class URLFetcher(ResourceContentFetcher):
    """
    Implement the Implementor interface and define its concrete
    implementation.
    """

    def fetch(self, path):
        # path is an URL
        req = urllib.request.Request(path)
        with urllib.request.urlopen(req) as response:
            if response.code == 200:
                the_page = response.read()
                print(the_page)


# implementation
class LocalFileFetcher(ResourceContentFetcher):
    """
    Implement the Implementor interface and define its concrete
    implementation.
    """

    def fetch(self, path):
        # path is the filepath to a text file
        with open(path) as f:
            print(f.read())


def main():
    url_fetcher = URLFetcher()
    iface = ResourceContent(url_fetcher)
    iface.show_content('http://python.org')

    print('===================')

    localfs_fetcher = LocalFileFetcher()
    iface = ResourceContent(localfs_fetcher)
    iface.show_content('file.txt')
    print(dir(ResourceContentFetcher))
    print(dir(iface))


if __name__ == "__main__":
    main()
