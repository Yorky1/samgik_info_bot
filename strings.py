"""
Bot data
trigger -> actions -> reply_message(?)/go to next state - state
"""

from telegram import ReplyKeyboardMarkup
FACULTIES=[
    "Музыкально-исполнительский факультет",
    "Факультет современного искусства и художественных коммуникаций",
    "Театральный факультет",
    "Факультет культурологии, социально-культурных и информационных технологий"
]

FACULTY_MESSAGES={
    FACULTIES[0]:"Тебе надо найти Мраморный зал. Да, в нем очень и очень много мрамора. "\
    "В холле слева ты увидишь парадную лестницу. Поднимайся по ней как важный до конца. "\
    "Устал, ну еще парочку этажей, давай. Студенты СГИКа должны быть в хорошей форме..",
    FACULTIES[1]:"Тебе повезло! Сейчас мы отправимся в одно из самых красивых мест нашего института – Актовый зал. "
    "Зал очень красивый, поверь, у тебя будет время оценить его за годы обучения!  Как придешь, познакомься с однокурсниками и с руководством факультета. "
    "Из холла иди в правую дверь, поднимайся на второй этаж. Нужная тебе дверь находится слева.",
    FACULTIES[2]:"Идем в Камерный зал  знакомиться с руководством факультета. Если ты в холле второго корпуса, иди прямо."
    "Перед тобой пано. Справа в стене ищи дверь. Тебе туда. В Камерном зале очень уютно.",
    FACULTIES[3]:"Идем в Малый зал  знакомиться с руководством факультета. Из холла иди в правую дверь, поднимайся на второй этаж. "\
    "Видишь кабинет ректора? Тебе пока не сюда. Сворачивай налево. Заходи в первый кабинет. Около него есть табличка «Малый зал»."
}

PROCESSION={
    FACULTIES[0]:"На улице не отставай от своего факультета. Маршрут твоего шествия такой: от первого корпуса иди в сторону филармонии. Не знаешь, где она – следи за помощниками режиссёра!"
    "Аккуратно переходи дорогу! А на улице Некрасовской поверни вниз! Так ты спустишься к ул. Куйбышева! Увидишь красивое большое здание – смело иди со своим факультетом к нему!",
    FACULTIES[1]:"На улице не отставай от своего факультета. Маршрут твоего шествия такой: от первого корпуса иди в сторону Струковского сада. Не знаешь, где он – следи за помощниками режиссёра!"
    "Аккуратно переходи дорогу! А на улице Куйбышева поверни налево! Иди, пока не увидишь красивое большое здание (знаем, на этой улице их много, но тебе помогут не ошибиться) – смело иди со своим факультетом к нему!",
    FACULTIES[2]:"На улице не отставай от своего факультета. Маршрут твоего шествия такой: от второго корпуса иди в сторону филармонии. Не знаешь, где она – следи за помощниками режиссёра!"
    "Аккуратно переходи дорогу! А на улице Некрасовской поверни вниз! Так ты спустишься к ул. Куйбышева! Увидишь красивое большое здание – смело иди со своим факультетом к нему!",
    FACULTIES[3]:"На улице не отставай от своего факультета. Маршрут твоего шествия такой: от первого корпуса иди в сторону Струковского сада. Не знаешь, где он – следи за помощниками режиссёра!"
    "Аккуратно переходи дорогу! А на улице Куйбышева поверни налево! Иди, пока не увидишь красивое большое здание (знаем, на этой улице их много, но тебе помогут не ошибиться) – смело иди со своим факультетом к нему!"
}

CHANTS={
    FACULTIES[0]:"Наш костёл и горд, и рад\nСГИКовский услышать лад!\n\nФилармония моя,\nСкоро здесь сыграю я!\n\n"
    "Училищу Шаталова от студентов\nНаши громкие аплодисменты!\n\nДирижабль – культ. объект\nМама, я теперь студент!",
    FACULTIES[1]:"По Куйбышева каждый год\nСГИК шествие свое ведет!\n\nПромышленности это дом\nСкоро нашим станет он!\n\n"
    "В департаменте культуры\nЕсть успех у абитуры!\n\nДирижабль – культ. объект\nМама, я теперь студент!",
    FACULTIES[2]:"По адресу Фрунзе сто тридцать восемь\nСкоро стартуем в театральную осень\n\nНа дворе тридцать шестой\nПишет про ключик Алексей Толстой!\n\n"
    "Театр Камерная сцена,\nВам идет на встречу смена!\n\nДирижабль – культ. объект\nМама, я теперь студент!",
    FACULTIES[3]:"Эй, музей! Давай скорей!\nВстречай новеньких друзей!\n\nВ Струковском саду опять\nБудет весь наш СГИК гулять!\n\n"
    "Всем СГИКом черпаем вдохновение\nВ детской картинной галерее!\n\nДирижабль – культ. объект\nМама, я теперь студент!"
}

CONTACTS={
    FACULTIES[2]:"\n".join([
        "*Декан* - Заварницына Наталья Михайловна",
        "\n\n*Контакты*:",
        "Специалист по учебно-методической работе - Абдулкина Анастасия Андреевна",
        "г. Самара, ул. Фрунзе, д. 138, \(учебный корпус №2\), а.33",
        "+7\(846\) 333-25-32 33",
        "tf@samgik.ru",
        "\n\n*Наставники*:",
        "АДТс-122 [Ярослав Лапшин](https://vk.com/riley.adam)",
        "РЛТ-122 [Лана Добрянина](https://vk.com/ladobro02)"
    ]),
    FACULTIES[0]:"\n".join([
        "*Декан* - Седова Наталья Викторовна",
        "\n\n*Контакты*:",
        "Доцент - Русанова Наталья Николаева",
        "г. Самара ул. Фрунзе, д. 167, \(учебный корпус №1\), ауд.405",
        "rusanovann@samgik.ru",
        "Специалист по учебно-методической работе - Крупская Татьяна Сергеевна",
        "г. Самара, ул. Фрунзе, д. 167, \(учебный корпус №1\), а.415",
        "+7\(846\) 333-24-79",
        "mif@samgik.ru",
        "\n\n*Наставники*:",
        "[Гузель Шаяхметова](https://vk.com/guzelshika)",
        "[Ксения Семёнова](https://vk.com/kseniya_semenova2001)"
    ]),
    FACULTIES[1]:"\n".join([
        "*Декан* - Плаксин Павел Алексеевич",
        "\n\n*Контакты*:",
        "Специалист по учебно-методической работе - Оганесова Анна Николаевна",
        "г. Самара, ул. Фрунзе 167, \(учебный корпус №1\), ауд. 312",
        "+7 \(846\) 333-35-47",
        "fsiihk@samgik.ru",
        "Специалист по учебно-методической работе - Шельдяшева Марина Владимировна",
        "г. Самара, ул. Фрунзе 167, \(учебный корпус №1\), ауд. 312",
        "+7 \(846\) 333-35-47",
        "fsiihk@smrgaki.ru",
        "\n\n*Наставники*:",
        "РТП-122",
        "[Арина Петрищева](https://vk.com/petrischevaa)",
        "[Наталья Ковылина](https://vk.com/natashafrom_russia)",
        "\nЗВС-122",
        "[Динар Хакимов](https://vk.com/smlag)",
        "\nРНХ-122",
        "[Мария Усачева](https://vk.com/id132915993)",
        "[Олег Калинин](https://vk.com/olegisfriends)",
        "[Соня Алыпова](https://vk.com/sonechkaa_al)",
        "[Виктория Николаенко](https://vk.com/victoriaaleksandrovna888)",
        "\nИЭО-122 МП-122",
        "[Николь Неласова](https://vk.com/n_nlsv)",
        "[Мария Автамонова](https://vk.com/m.avtamonova)"
    ]),
    FACULTIES[3]:"\n".join([
        "*Декан* - Галкина Екатерина Алексеевна",
        "\n\n*Контакты*:",
        "Доцент - Чиркова Наталья Владимировна",
        "г. Самара, ул. Фрунзе, д. 167, \(учебный корпус №1\), а.508",
        "+7\(846\) 333-22-25",
        "chirkovanv@samgik.ru",
        "Преподаватель - Шерстнев Александр Вячеславович",
        "г. Самара, ул. Фрунзе, д. 167, \(учебный корпус №1\), а.501",
        "+7\(846\) 333-26-21",
        "sherstnevav@samgik.ru",
        "\n\n*Наставники*:",
        "МИД-122 ДВ-122",
        "[Юлия Филатова](https://vk.com/youliee)",
        "\nБВ-122 КМ-122",
        "[Дмитрий Пичугин](https://vk.com/dmitrycherneckiy)",
        "\nСКД-122",
        "[Ольга Солодова](https://vk.com/olgadinosaur)",
        "\nЭтнодизайн",
        "[Анна Жиднаева](https://vk.com/id185920002)"
    ]),
}

for key, _ in CONTACTS.items():
    CONTACTS[key] = CONTACTS[key].replace("-", r"\-").replace(".", r"\.").replace("+", r"\+")

STATE_MESSAGES={
    1:"Доброе утро, первокурсник! Как настроение?",
    2:"Теперь ты — студент самого творческого вуза региона и часть команды Самарского института культуры."\
    "Пусть этот День знаний станет для тебя самым крутым. Тебя ждет квест, концерт и много всего прикольного."\
    "Рассказывай, куда поступил?",
    3:FACULTY_MESSAGES,
    4:"Пусть этот День знаний станет частью истории. Делай селфи на фоне СГИКа, выкладывай на своей странице в Вк с тегом "
      "#первокурсниксгик. Соберем все фото в альбом, чтобы через четыре года вы вспомнили какими были молодыми и смешными.",
    5:"Здесь ты можешь выбрать, что еще хочешь узнать",
    6:"Давай познакомимся. Из какого ты города?",
    13:["С тобой будут учиться ребята из разных городов. Познакомь их с Самарой.", "Самара тебе понравится. Где будешь жить?"],
    14:"Круто! Как добрался до института?",
    15:"Окей, спасибо, что поделился со мной!", # (?) results of forms from other participants
    7:["Кстати, про расписание. Сегодня у тебя особенный день! Расписание будет тоже особенное, праздничное. "
    "За праздники в нашем институте отвечают студенты кафедры режиссуры театрализованных представлений и праздников.",
    "Сегодня весь день с нами журналисты СГИК-медиа. Снимаем видос о Дне знаний в самом творческом вузе. "
    "Не бойся попадать в объектив и ищи видео со своим участием в наших социальных сетях."],
    8:CHANTS,
    9:["Мы пройдем от главного корпуса СГИКа по центральным улицам до Молодежного концертно-театрального комплекса «Дирижабль». "
    "Там проходят (логично) концерты и самые крупные мероприятия института. "
    "А в этом году в корпусе будут еще и учиться студенты кафедры эстрадно-джазового искусства.", PROCESSION],
    10:"TL;DR",
    11:CONTACTS,
    12:"Теперь наш черед рассказать про институт. В этом году Самарскому институту культуры исполнился…",
    16:[["Да, так и есть!", "Нет, в этом году СГИКу исполнился 51 год."],
    "Самарский институт культуры - единственный творческий вуз региона. Здесь 5 факультетов, 20 кафедр и больше 10 творческих коллективов, "
    "которые выступают по всей России. Учиться у нас сложно, но интересно. Готовься приходить сюда рано утром и уезжать домой на закате. "
    "Однокурсники станут твоей семьей, а преподаватели будут оберегать и заботиться ближайшие несколько лет.",
    "Будь в курсе, что происходит в институте. Рассказываем о наших талантливых студентах в группе в Vk и в Тг-канале. "
    "Если ты пишешь треки, придумываешь проекты, сам ставишь спектакли — становись героем историй. \n"
    "https://vk.com/sgik_culture\n"
    "https://t.me/sgik_culture",
    "Не только учеба. Каждую неделю ждем тебя на спектаклях в учебном театре СГИКа и на концертах МФЦ «Консерватория». Для студентов вход бесплатный.\n"
    "https://vk.com/u4teatr\n"
    "https://vk.com/samaraconcerts",
    "Будь спортивным. Держи себя в форме и в перерыве между репетициями и семинарами приходи на секции. "
    "Студенты СГИКа занимаются в бассейне и ходят на секцию по волейболу. Все расскажут ребята из студсовета.\n"
    "https://t.me/sgikstudsovet"
    ],
    17:"Выбери факультет"
}

STATE_REPLIES={
    1:[["Доброе утро!"]],
    2:[[x] for x in FACULTIES],
    3:[["Я на месте!"]],
    5:[["Анкета", "День знаний", "Кричалки"], ["Шествие", "Праздничный концерт", "Контакты"], ["Про СГИК"]],
    13:[[["Хорошо!"]], [["Общежитие"], ["Снимаю квартиру"]]],
    14:[["Пешком", "На городском транспорте"], ["На самокате", "На крыльях любви"]],
    12:[["69 лет", "51 год", "118 лет"]],
    17:[[x] for x in FACULTIES]
}

MENU_STATES=[]
for v in STATE_REPLIES[5]:
    for s in v:
        MENU_STATES.append(s)

NEXT_STATE={
    1:2,
    2:3,
    3:4,
    4:5,
    5:[6, 7, 8, 9, 10, 11, 12],
    6:13,
    13:14,
    14:15,
    12:16,
    16:5,
    17:17
}

REPLY_MARKUPS={}
for key, val in STATE_REPLIES.items():
    if isinstance(val[0][0], list):
        REPLY_MARKUPS[key] = [0] * len(val)
        for i, value in enumerate(val):
            REPLY_MARKUPS[key][i] = ReplyKeyboardMarkup(value, one_time_keyboard=True)
    else:
        REPLY_MARKUPS[key] = ReplyKeyboardMarkup(val, one_time_keyboard=True)

STRING_STATES={}
for key, val in STATE_REPLIES.items():
    for v in val:
        for s in v:
            if isinstance(s, list):
                for ss in s:
                    STRING_STATES[ss] = key
            else:
                STRING_STATES[s] = key


ERROR_MESSAGE="Ой, что-то пошло не так. Нажми /start, чтобы меня перезапустить."

SAMARA="самара"
MENU_STATE=5
START_FORM_STATE=6
CITY_STATE=13
GET_INSTITUTE_STATE=14
STATE="state"
FACULTY="faculty"
CITY="city"
QUIZ_STATE=12
RIGHT_ANSWER="51 год"
SET_FACULTY_STATE=17
PREV_STATE="prev_state"


FREE_ANSWER={CITY_STATE}
