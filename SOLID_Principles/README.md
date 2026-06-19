
1. S -> Single Responsibility Principle (SRP)
2. O -> Open/Closed Principle (OCP)
3. L -> Liskov Substitution Principle (LSP)
4. I -> Interface Segregation Principle (ISP)
5. D -> Dependency Inversion Principle (DIP)


### Single Responsibility Principle (SRP)
- A class should have only one reason to change, meaning it should have only one responsibility or job. This promotes separation of concerns and makes the code easier to maintain and understand.


### Open/Closed Principle (OCP)
- Software entities (classes, modules, functions, etc.) should be open for extension but closed for modification. This means that you should be able to add new functionality without changing existing code, which helps to prevent bugs and maintain stability.

### Liskov Substitution Principle (LSP)
- Subtypes must be substitutable for their base types. This means that objects of a superclass  should be replaceable with objects of a subclass without affecting the correctness of the program. This promotes the use of inheritance and polymorphism in a way that ensures that derived classes can be used interchangeably with their base classes.

### Interface Segregation Principle (ISP)
- Clients should not be forced to depend on interfaces they do not use. Better to have many specific interfaces than one fat interface.

### Dependency Inversion Principle (DIP)
- High-level modules should not depend on low-level modules. Both should depend on abstractions (e.g., interfaces). Abstractions should not depend on details. Details should depend on abstractions. This promotes loose coupling and makes the code more flexible and easier to maintain.