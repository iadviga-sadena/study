from pprint import pprint


class Person:
    def __init__(self, category, name, age, sex):
        self.category, self.name, self.age, self.sex = category, name, age, sex
        self.key = (category, name, age)

    def __repr__(self):
        return "Person('%s', '%s', %s, '%s')" % (self.category, self.name, self.age, self.sex)


class Employee:
    def __init__(self, category, name, age, sex, position):
        self.category, self.name, self.age, self.sex, self.position = category, name, age, sex, position
        self.key = (category, name, age)

    def __repr__(self):
        return "Worker('%s', '%s', %s, '%s', '%s')" % (self.category, self.name, self.age, self.sex, self.position)


class Student:
    def __init__(self, category, name, age, sex, stage):
        self.category, self.name, self.age, self.sex, self.stage = category, name, age, sex, stage
        self.key = (category, name, age)

    def __repr__(self):
        return "Student('%s', '%s', %s, '%s', '%s')" % (self.category, self.name, self.age, self.sex, self.stage)


sergey = Student('Студент', "Сергей", 20, "М", 3)
alexey = Student('Студент', "Алексей", 19, "М", 2)
evgenyi = Employee('Сотрудник', "Евгений", 25, "М", 'Инженер')
anjela = Employee('Сотрудник', "Анжела", 25, "Ж", 'Менеджер')
oksana = Person('Остальные', "Оксана", 35, "Ж")

people = {
    sergey.key: sergey,
    alexey.key: alexey,
    evgenyi.key: evgenyi,
    anjela.key: anjela,
    oksana.key: oksana
}

pprint(people)
