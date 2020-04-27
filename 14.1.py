class NewInt(int):
    def __init__(self, a):
        self.a = a

    def __add__(self, b):
        if self.a == 2 and b == 2:
            return 5


x = NewInt(2)
x += 2
print(x)
