from random import randint

answ = ['Да!', 'Нет!']
question = input('Задай мне вопрос :)\n').lower()
was_asked = {
    '': '',
}

while question != 'стоп':
    if was_asked.get(question) is not None:
        print('Мой ответ был - {}'.format(was_asked.get(question)))
        question = input('Задай мне вопрос :)\n').lower()
    else:
        an = answ[randint(0, 1)]
        was_asked[question] = an
        print(an)
        question = input('Задай мне вопрос :)\n').lower()
