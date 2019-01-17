class Sample:
    __instance = None

    def __init__(self):
        if not Sample.__instance:
            print("__init__ method ")
        else:
            print("instance already created")

    @classmethod
    def getInstance(cls):
        if not cls.__instance:
            cls.__instance = Sample()
        return cls.__instance


s1 = Sample()
print("Object created here ", Sample.getInstance())
s2 = Sample()

