people_dict = {
    'студенты': {
        'Сергей': {
            'Возраст': 19,
            "Пол": "М",
            "Курс": 3
        },
        'Алексей': {
            'Возраст': 21,
            "Пол": "М",
            "Курс": 3
        },
        'Марина': {
            'Возраст': 18,
            "Пол": "Ж",
            "Курс": 2
        },
    },
    'работники': {
        'Илья': {
            'Возраст': 25,
            "Пол": "М",
            "Должность": "Инженер"
        },
        'Алексей': {
            'Возраст': 29,
            "Пол": "М",
            "Должность": "Инженер"
        },
        'Мария': {
            'Возраст': 24,
            "Пол": "Ж",
            "Должность": "Секретарь"
        },
    },
    'остальные': {
        "Александр": {
            'Возраст': 25,
            "Пол": "М",
            "Должность": "Инженер"
        },
        'Владимир': {
            'Возраст': 29,
            "Пол": "М",
            "Должность": "Инженер"
        },
        'Мария': {
            'Возраст': 24,
            "Пол": "Ж",
            "Должность": "Секретарь"
        },
    }
}

oldest = [0, 'Имя', 'Категория']

for category in people_dict.keys():
    for man in people_dict[category].keys():
        if people_dict[category][man]['Возраст'] > oldest[0]:
            oldest.clear()
            oldest.append(people_dict[category][man]['Возраст'])
            oldest.append(man)
            oldest.append(category)
        elif people_dict[category][man]['Возраст'] == oldest[0]:
            oldest.append(people_dict[category][man]['Возраст'])
            oldest.append(man)
            oldest.append(category)

print('Самые старые: ', oldest)