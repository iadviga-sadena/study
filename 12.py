"""
Объект человека имеющий самые базовые параметры как имя, возраст и пол. Также несколько возможных действий: пройтись,
поесть и поспать
"""


class Human:
    def __init__(self, name, age, sex):
        pass

    def walk(self):
        pass

    def eat(self):
        pass

    def sleep(self):
        pass


"""
Cоответственно объект студента и несколько основных базовых параметров, т.к. нет смысла пытаться описать все возможные
реальные писущие характеристики. Это производная объекта человека и поэтому он имеет все его возможности + несколько
своих особенных. Так добавляются курс и название учебного заведения и несколько возможных дейтвий данного объекта:
пойти на учёбу, учиться.
"""


class Student(Human):
    def __init__(self, name, age, sex, stage, university):
        pass

    def go_to_study(self):
        pass

    def study(self):
        pass


"""
Ну и объект сотрудника также происходит от изначального человека, но добавляются:
категория работника(инженерно-технический работник, медперсонал, научный и т.д.),
должность, заработная плата и место работы. Соответственно сотрудник может получить зарплату, сделать
какую-то работу, пойти на работу или вернуться домой.
"""


class Employee(Human):
    def __init__(self, category, name, age, sex, position, salary, company):
        pass

    def get_payment(self):
        pass

    def do_work(self):
        pass

    def go_to_work(self):
        pass

    def go_back_home(self):
        pass
