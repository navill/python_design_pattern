# Python Design Pattern

##### packt 출판사의 [advanced python programming](https://subscription.packtpub.com/book/application_development/9781838551216)을 참고하였습니다.



디자인 패턴에 대한 완전한 이해보다는 개념을 정리하고 추후 개발 시 필요한 부분을 적용할 수 있도록 정리하였습니다. 

- 디자인 패턴에 대한 개념 이해
- 여러 예제를 통해 파이썬의 다양한 구현 방법 분석

**[Reference Site]**

[https://www.packtpub.com](https://www.packtpub.com/): 각종 프로그래밍에 대한 E-book 및 동영상 강의 제공

https://sourcemaking.com: 디자인 패턴 뿐만 아니라 안티패턴, 리팩토링 등 좋은 프로그램을 개발하기 위해 필요한 이론 및 예제들을 다양한 언어로 정리한 사이트

https://en.wikipedia.org



##### 디자인 패턴에 대한 세부 내용은 Notion으로 정리하였습니다.

### Creational Pattern: 객체 생성

- [Factory method](https://www.notion.so/afmadadans/Creational-Design-Pattern-Factory-b9e488cdce01496fa5b1a3dce378549b#f34ee2ac74594a319d6f2fef08d7714c) & [Abstract Factory](https://www.notion.so/afmadadans/Creational-Design-Pattern-Factory-b9e488cdce01496fa5b1a3dce378549b#6b3621da32ab49188faed856c04eea23): 객체 생성 작업을 처리하기 위해 작성된 단일 함수
- [Builder](https://www.notion.so/afmadadans/Creational-Design-Pattern-Builder-f7e8b75c7b6c4bf9ad466d3fdaf603fa): 하나의 객체를 여러 단계로 나누어 작성해야하고, 각 단계를 구성하는 내용이 다른 표현(출력)을 요구할 때 사용
- [Prototype](https://www.notion.so/afmadadans/Other-Creational-Patterns-Singleton-Prototype-a20e99d8a07444a7bde94d463b689e28#3d0c54ed1c134f7fa5e89f15613a256c): 기존의 객체를 유지한 상태로 사본 객체의 일부를 수정해야 할 경우 사용
- [Singleton](https://www.notion.so/afmadadans/Other-Creational-Patterns-Singleton-Prototype-a20e99d8a07444a7bde94d463b689e28#d96e8b120d75466c98f1a3688cccb75a): 클래스를 하나의 객체로 제한해야 할 경우 사용



### Structural Pattern: 객체의 구조

- [Adapter](https://www.notion.so/afmadadans/Structural-Design-Pattern-Adapter-b63889d59c8a49fd9d43487d00726d59): 호환되지 않는 두 개의 인터페이스를 호환시키기 위한 구조 설계 패턴
- [Decorator](https://www.notion.so/afmadadans/Structural-Design-Pattern-Decorator-c20f194c37ed4ee2b25f6cd0a85670bf): 기존 객체에 영향을 미치지 않으면서 객체의 기능을 확장하기 위해 사용
- [Bridge](https://www.notion.so/afmadadans/Structural-Design-Pattern-Bridge-599cb46a7ad2454781ab14afa01797f0): 기능과 구현을 별도의 클래스로 나누어 독립성을 확보
- [Facade](https://www.notion.so/afmadadans/Structural-Design-Pattern-Facade-7fdb9c8375e24aa8b4911d0482c6218f): 복잡한 시스템을 클라이언트에 노출시키지 않고 단일 진입점을 만들기 위해 사용
- [Flyweight](https://www.notion.so/afmadadans/Other-Structural-Patterns-flyweight-model-view-controller-MVC-and-proxy-f29651efd91e4c24b31004baa1fd83f4#bf2eb5cd4dcd4055b3300fcf3cdb4855): 가능한 유사한 객체의 리소스를 공유하여 메모리 사용을 최소화 하는 기법
- [MVC](https://www.notion.so/afmadadans/Other-Structural-Patterns-flyweight-model-view-controller-MVC-and-proxy-f29651efd91e4c24b31004baa1fd83f4#1bc8e9669c3f4f4f91cc7b5390471b60): model-view-controller를 분리시켜 개발하는 방식(django의 MTV - model, template, view와 유사함)
- [Proxy](https://www.notion.so/afmadadans/Other-Structural-Patterns-flyweight-model-view-controller-MVC-and-proxy-f29651efd91e4c24b31004baa1fd83f4#b8fba02498134ec8aa0bb7ff6c50ec0e): 실제 객체에 접근하기 전에 중요한 작업을 수행시키고자 할 때 사용

### Behavioral Pattern: 객체의 동작

- [Chain of Responsibility](https://www.notion.so/afmadadans/Behavioral-Design-Pattern-Chain-of-Responsibility-9486451cbc764ecfb7a262d34c83c2a1): 단일 요청을 충족시키기 위해 여러 객체에게 기회를 주거나 특정 객체를 처리해야 하는 객체를 미리 알 수 없는 경우에 사용
- [Command](https://www.notion.so/afmadadans/Behavioral-Design-Pattern-Command-37d547760fe640b2954042466cb0c743): 요청을 객체의 형태로 캡슐화하여 사용자가 보낸 요청을 나중에 이용할 수 있도록 메서드 이름, 매개변수 등 요청에 필요한 정보를 저장 또는 로깅, 취소할 수 있게 하는 패턴
- [Observer](https://www.notion.so/afmadadans/Behavioral-Design-Pattern-Observer-7d4a75f7a74044fbb33142fb5bdf4fe8): 한 개의 모델(publisher)에 여러 뷰(subsriber)가 사용될 경우, 모델이 수정되면 이를 여러 뷰에 알리거나 수정사항을 적용할 때 사용

