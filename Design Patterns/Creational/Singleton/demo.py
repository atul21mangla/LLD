import threading

class Singleton():

    __instance = None
    __lock = threading.Lock()

    def __new__(cls):
        if cls.__instance is None:
            with cls.__lock:
                if cls.__instance is None:
                    print("New instance created.")
                    cls.__instance = super().__new__(cls)

        return cls.__instance
    
    def get_message(self):
        return "Hello from Thread Safe Singleton..!!"
    

def main():

    s1 = Singleton()
    s2 = Singleton()

    print(s1 == s1)
    print(s1.get_message())


if __name__ == "__main__":
    main()

