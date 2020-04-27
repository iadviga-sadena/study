class NewList(list):
    def __init__(self, li):
        if len(li) > 10:
            print('Недопустимая длина!')
        else:
            super().__init__(li)

    def append(self, obj):
        if len(self) == 10:
            print('Недопустимая длина!')
        else:
            super().append(obj)
