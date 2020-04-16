people_list = [
    ['Студенты', ['Сергей', 20, "М", 3], ['Алексей', 19, "М", 3], ['Владимир', 19, "М", 3]],
    ['Работники', ['Евгений', 25, "М", "Инженер"], ['Алексей', 21, "М", "Техник"], ['Вячеслав', 35, "М", "Зав.хозяйством"]],
    ['Остальные', ['Оксана', 35, "Ж"], ['Анжела', 25, "Ж"], ['Владимир', 19, "М"]]
]

oldest = [0, 'Имя', 'Категория']

for i in people_list:
    for k in i[1::]:
            if k[1] > oldest[0]:
                oldest.clear()
                oldest.append(k[1])
                oldest.append(k[0])
                oldest.append(i[0])
            elif k[1] == oldest[0]:
                oldest.append(k[1])
                oldest.append(k[0])
                oldest.append(i[0])

print('Самые старые: ', oldest)


