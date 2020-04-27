from random import randint

answ = ['Да!', 'Нет!']
question = input('Задай мне вопрос :)\n')

while question != 'стоп':
    print(answ[randint(0, 1)])
    question = input('Задай мне вопрос :)\n')
