class EagerSingleton:

    __instance = None

    def __new__(cls):
        if cls.__instance is None:
            cls.__instance = super().__new__(cls)
            cls.__instance.__initialized = False

        return cls.__instance
    
    def __init__(self):
        if not self.__initialized:
            print("New instance created.")
            self.__initialized = True
        else:
            return  # Prevent re-initialization of the instance


    def get_message(self):
        return "Hello from Eager Singleton..!!"
    

_eager_instance = EagerSingleton()  # Create the instance eagerly