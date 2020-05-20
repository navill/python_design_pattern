from __future__ import annotations
from abc import abstractmethod, ABCMeta
from typing import Any


class Builder(metaclass=ABCMeta):
    """
    builder는 product의 일부를 생성하기 위해 필요한 메서드를 갖는다.
    a + b + c -> product
    """

    def product(self) -> None:
        pass

    @abstractmethod
    def produce_part_a(self) -> None:
        pass

    @abstractmethod
    def produce_part_b(self) -> None:
        pass

    @abstractmethod
    def produce_part_c(self) -> None:
        pass


class ConcreteBuilder1(Builder):
    def __init__(self) -> None:
        """
        __init__이 실행될 때 새로운 Product()로 갱신
        """
        self.reset()

    def reset(self) -> None:
        self._product = Product1()

    @property
    def product(self) -> Product1:
        """
        reset(): 일반적으로 클라이언트가 결과값을 반환하면, builder instance는 새로운 product를 생성할 준비 상태가 되어야한다.
        product 또는 클라이언트에서 reset을 실행
        """
        product = self._product
        self.reset()
        return product

    def produce_part_a(self) -> None:
        self._product.add("PartA1")

    def produce_part_b(self) -> None:
        self._product.add("PartB1")

    def produce_part_c(self) -> None:
        self._product.add("PartC1")


class Product1:
    """
    Product가 복잡하고 클 경우 Builder 패턴을 사용
    - builder가 동일한 product를 생성하지 않음
    - product가 다른 형태의 결과를 생성해도 무방하다(다른 creational pattern과 다름)
    """

    def __init__(self) -> None:
        self.parts = []

    def add(self, part: Any) -> None:
        self.parts.append(part)

    def list_parts(self) -> None:
        print(f"Product parts: {', '.join(self.parts)}", end="")


class Director:
    """
    Driector는 concrete builder를 (순서에 맞게)실행하기 위해 사용됨: 선택사항
    - Concrete builder는 Director뿐만 아니라 Client에서 실행할 수 있음
    """

    def __init__(self) -> None:
        self._builder = None

    @property
    def builder(self) -> Builder:
        return self._builder

    @builder.setter
    def builder(self, builder: Builder) -> None:
        self._builder = builder

    def build_minimal_viable_product(self) -> None:
        self.builder.produce_part_a()

    def build_full_featured_product(self) -> None:
        self.builder.produce_part_a()
        self.builder.produce_part_b()
        self.builder.produce_part_c()


if __name__ == "__main__":
    """
    Client -> Builder object -> Director로 전달 -> product 생성
    """

    director = Director()
    builder = ConcreteBuilder1()
    director.builder = builder

    print("Standard basic product: ")
    director.build_minimal_viable_product()
    builder.product.list_parts()

    print("\n")

    print("Standard full featured product: ")
    director.build_full_featured_product()
    builder.product.list_parts()

    print("\n")

    # Remember, the Builder pattern can be used without a Director class.
    print("Custom product: ")
    builder.produce_part_a()
    builder.produce_part_b()
    builder.product.list_parts()
