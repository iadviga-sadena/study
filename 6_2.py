
class Person:
    def __init__(self, category, name, surname, age, sex):
        self.category, self.name, self.surname, self.age, self.sex = category, name, surname, age, sex
        self.key = (category, name, surname)

    def __repr__(self):
        return "Person('%s', '%s', '%s', %s, '%s')" % (self.category, self.name, self.surname, self.age, self.sex)

    def __eq__(self, obj):
        if type(obj) == str:
            return obj in [self.category, self.name, self.surname, self.sex]
        elif type(obj) == int:
            if self.age == obj:
                return obj

    def __lt__(self, obj):
        if self.age < obj:
            return obj

    def __gt__(self, obj):
        if self.age > obj:
            return obj

    def __getitem__(self, key):
        if key == 'имя':
            return self.name
        elif key == 'фамилия':
            return self.surname
        elif key == 'категория':
            return self.category
        elif key == 'возраст':
            return self.age
        elif key == 'пол':
            return self.sex


sergey = Person('Студент', "Сергей", 'Иванов', 20, "М")
alexey = Person('Студент', "Алексей", 'Петров', 19, "М")
evgenyi = Person('Сотрудник', "Евгений", 'Сидоров', 25, "М")
anjela = Person('Сотрудник', "Анжела", 'Карпова', 25, "Ж")
oksana = Person('Остальные', "Оксана", 'Сидрова', 35, "Ж")

people = {
    sergey.key: sergey,
    alexey.key: alexey,
    evgenyi.key: evgenyi,
    anjela.key: anjela,
    oksana.key: oksana
}

params = input('Введите запрос: ').lower().split()

eq = {
    'равно': lambda a, b: a == b,
    'больше': lambda a, b: a > b,
    'меньше': lambda a, b: a < b
}


if len(params) == 3:
    for person in people.values():
        if eq[params[1]](person[params[0]], int(params[2])):
            print(person)
elif len(params) == 2:
    for person in people.values():
        if person[params[0]].lower() == params[1]:
            print(person)
