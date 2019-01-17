class Sample:
    def __new__(cls):
        print("__new__ Method")
        if not hasattr(cls, 'instance'):
            cls.instance = super(Sample, cls).__new__(cls)
        return cls.instance

    def __init__(self):
        print("__init__ Method")


class Sample1:
    pass


s = Sample()
print("Object : ", s)

s1 = Sample()
print("Object : ", s1)

s2 = Sample1()
print("Object : ", s2)

s3 = Sample1()
print("Object : ", s3)
