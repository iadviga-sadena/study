class NewList(set):
    def __init__(self, li):
        super().__init__(li)


x = NewList([1, 2, 2, 2, 1, 1, 1, 2, 23, 3])
print(x)
