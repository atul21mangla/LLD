# Singleton Pattern

The Singleton Design Pattern is a creational pattern that ensures a class has only one instance throughout the application and provides a global point of access to it.

It is useful for shared resources such as:

- Database connections
- Logging services
- Configuration managers
- Caches

## Why Use It?

- You want to prevent multiple instances of an object.
- You need a single shared point of access.
- You want to manage global state in a controlled way.

## Core Idea

The class controls its own instance creation and returns the same object every time it is requested.

In Python, there are a few common ways to implement a Singleton:

1. Module-level singleton
1. Overriding `__new__`
1. Decorator-based singleton
1. Thread-safe singleton

## 1. Module-Level Singleton

In Python, modules are singletons by default. When a module is imported, Python loads it once and reuses the same module object on later imports.

```python
# database_config.py
class DatabaseConfig:
    def __init__(self):
        self.connection_string = "localhost:5432"


db_config = DatabaseConfig()
```

```python
# main.py
from database_config import db_config

print(db_config.connection_string)
```

This is often the simplest and most Pythonic approach.

## 2. Singleton Using `__new__`

If you want Singleton behavior directly on a class, you can override `__new__` so every call returns the same instance.

```python
class ClassicSingleton:
    _instance = None

    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    def __init__(self):
        if not hasattr(self, "_initialized"):
            self.data = []
            self._initialized = True
```

### Verification

```python
s1 = ClassicSingleton()
s2 = ClassicSingleton()

print(s1 is s2)  # True
```

## 3. Thread-Safe Singleton

If your application runs in a multithreaded environment, two threads could create separate instances at the same time. A lock prevents that race condition.

```python
import threading


class ThreadSafeSingleton:
    _instance = None
    _lock = threading.Lock()

    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            with cls._lock:
                if cls._instance is None:
                    cls._instance = super().__new__(cls)
        return cls._instance
```

## `__new__` vs `__init__`

- `__new__` creates the instance.
- `__init__` initializes the already-created instance.

When you call `MyClass()`, Python runs `__new__` first, then passes the created object to `__init__`.

## Quick Summary

Use Singleton when one shared instance is exactly what your design needs, but avoid it when dependency injection or plain object instances would make the code simpler and easier to test.


## Eager Initialization Singleton

An eager initialization singleton creates its single instance immediately when the module or class is loaded, rather than waiting for the first time it is explicitly requested (lazy initialization).

An eager initialization singleton creates its single instance immediately when the module or class is loaded, rather than waiting for the first time it is explicitly requested (lazy initialization).