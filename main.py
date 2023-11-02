
#библиотеки для telegram
import telebot
bot = telebot.TeleBot('5648163845:AAFGaNYtvzMXGhtENXngDb1GYEB4kutUm70')

nms = ['Гусман бей','Райнур абый','Аккмалутдинов','Бариев','Воробьев','Галаутдинов','Гашигулин','Димухаметов','Загидулин','Закиров','Замалеев','Ильин','Исмагилов',
         'Леухин','Лукьянов','Мифтахов','МустафинК','МустафинС','Мухаметгалиев','ПимурзинРусл',
         'ПимурзинРуст','Сахабутдинов','Фаизов','Фазлиев','Хамидулин','Шамсиев','Юсупов']
ind = [0,0,1303460009,1735288618,1153400878,1668851054,1203352160,1082861746,2049380647,1612294989,0,1196509690,
       0,1118648643,1463862718,1388947413,761831397,1958898376,1644355420,0,
       1433174395,1349375141,1332512027,1310469611,1298983887,1200998361,1351307952,0,0,0,0,0,0,0]#1202390893

#клавы
main = telebot.types.ReplyKeyboardMarkup()
main.add('Домашнее задание')
main.add('Новости')
main.add('Дежурство')
main.add('Расписание')

dz = telebot.types.ReplyKeyboardMarkup()
dz.add('Биология')
dz.add('Турецкий(рус)')
dz.add('Турецкий(тат)')
dz.add('География')
dz.add('ИЗО')
dz.add('Английский(сред)')
dz.add('Английский(сил)')
dz.add('История')
dz.add('Лит-ра')
dz.add('Алгебра')
dz.add('Геометрия')
dz.add('Музыка')
dz.add('Общество')
dz.add('Род.лит(рус)')
dz.add('Родной(рус)')
dz.add('Род.лит(тат)')
dz.add('Родной(тат)')
dz.add('Рус.яз')
dz.add('Технология')
dz.add('Физ-культура')
dz.add('Физика')
dz.add('Информатика')
dz.add('MENU')

week = telebot.types.ReplyKeyboardMarkup()
week.add('ПН','ВТ','СР')
week.add('ЧТ','ПТ','СБ')
week.add('MENU')

names = telebot.types.ReplyKeyboardMarkup()
names.add('Гусман бей')
names.add('Райнур абый')
names.add('Аккмалутдинов')
names.add('Бариев')
names.add('Воробьев')
names.add('Галаутдинов')
names.add('Гашигулин')
names.add('Димухаметов')
names.add('Загидулин')
names.add('Закиров')
names.add('Замалеев')
names.add('Ильин')
names.add('Исмагилов')
names.add('Леухин')
names.add('Лукьянов')
names.add('Мифтахов')
names.add('МустафинК')
names.add('МустафинС')
names.add('Мухаметгалиев')
names.add('ПимурзинРусл')
names.add('ПимурзинРуст')
names.add('Сахабутдинов')
names.add('Фаизов')
names.add('Фазлиев')
names.add('Хамидулин')
names.add('Шамсиев')
names.add('Юсупов')


#подключение firebase
import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore

cred = credentials.Certificate("./serviceAccountKey.json")
firebase_admin.initialize_app(cred)

db = firestore.client()


#обновление информации
def update():
    global timetable
    global news
    global hw
    global tgid
    global dez

    users_ref = db.collection('Evo1')
    docs = users_ref.stream()

    for doc in docs:
        if doc.id == "timetable":
            timetable = doc.to_dict()
        elif doc.id == "news":
            news = doc.to_dict()
        elif doc.id == "hw":
            hw = doc.to_dict()
        elif doc.id == "dez":
            dez = doc.to_dict()
        elif doc.id == "tgid":
            tgid = doc.to_dict()

    ind[0]=  tgid["n0"]
    ind[1] =  tgid["n1"]
    ind[2] =  tgid["n2"]
    ind[3] =  tgid["n3"]
    ind[4] =  tgid["n4"]
    ind[5] =  tgid["n5"]
    ind[6] =  tgid["n6"]
    ind[7] =  tgid["n7"]
    ind[8] =  tgid["n8"]
    ind[9] =  tgid["n9"]
    ind[10] =  tgid["n10"]
    ind[11] =  tgid["n11"]
    ind[12] =  tgid["n12"]
    ind[13] =  tgid["n13"]
    ind[14] =  tgid["n14"]
    ind[15] =  tgid["n15"]
    ind[16] =  tgid["n16"]
    ind[17] =  tgid["n17"]
    ind[18] =  tgid["n18"]
    ind[19] =  tgid["n19"]
    ind[20] =  tgid["n20"]
    ind[21] =  tgid["n21"]
    ind[22] =  tgid["n22"]
    ind[23] =  tgid["n23"]
    ind[24] =  tgid["n24"]
    ind[25] =  tgid["n25"]
    ind[26] =  tgid["n26"]
    ind[27] =  tgid["n27"]


update()

def updateind():
    doc_ref = db.collection('Evo1').document('tgid')

    i = 1
    for i in range(28):
        string = "n" + str(i)
        doc_ref.update({string: ind[i]})



@bot.message_handler(commands=['start'])
def start_message(message):
    bot.send_message(message.chat.id, 'Здравствуйте!👋', reply_markup=main)
    if message.chat.id not in  ind:
        bot.send_message(message.chat.id,"Хм, я вас не узнаю🙈, пожалуйста, выберите ваше имя/фамилию.",reply_markup=names)

@bot.message_handler(commands=['update'])
def start_message(message):
    bot.send_message(message.chat.id, 'Ожидайте')
    update()
    bot.send_message(message.chat.id, 'Выполенно')



@bot.message_handler(content_types=['text'])
def ans(message):
    global timetable
    global news
    global hw
    global dez

    if message.chat.id not in  ind:
        bot.send_message(message.chat.id,"Хм, я вас не узнаю🙈, пожалуйста, выберите ваше имя/фамилию.",reply_markup=names)

    if message.text == 'MENU':
        bot.send_message(message.chat.id, "Выполняю", reply_markup=main)


    if message.text == 'Домашнее задание':
        bot.send_message(message.chat.id, "Выберите урок:", reply_markup=dz)
    elif message.text == 'Новости':
        bot.send_message(message.chat.id, "Событие: " + news["event"])
        bot.send_message(message.chat.id, "Новости:")
        bot.send_message(message.chat.id, "1. " + news["new1"])
        bot.send_message(message.chat.id, "2. " + news["new2"])
        bot.send_message(message.chat.id, "3. " + news["new3"])
        bot.send_message(message.chat.id, "4. " + news["new4"])
        bot.send_message(message.chat.id, "5. " + news["new5"])
    elif message.text == 'Дежурство':
        bot.send_message(message.chat.id, "Дежурные на этой неделе:")
        bot.send_message(message.chat.id, "ПН." + dez["mon"])
        bot.send_message(message.chat.id, "ВТ." + dez["tue"])
        bot.send_message(message.chat.id, "СР." + dez["wed"])
        bot.send_message(message.chat.id, "ЧТ." + dez["thu"])
        bot.send_message(message.chat.id, "ПТ." + dez["fri"])
        bot.send_message(message.chat.id, "CБ." + dez["sat"])
    elif message.text == 'Расписание':
        bot.send_message(message.chat.id,"Выберите день",reply_markup=week)


    if message.text == 'ПН':
        bot.send_message(message.chat.id, "1. " + timetable["m1"])
        bot.send_message(message.chat.id, "2. " + timetable["m2"])
        bot.send_message(message.chat.id, "3. " + timetable["m3"])
        bot.send_message(message.chat.id, "4. " + timetable["m4"])
        bot.send_message(message.chat.id, "5. " + timetable["m5"])
        bot.send_message(message.chat.id, "6. " + timetable["m6"])
        bot.send_message(message.chat.id, "7. " + timetable["m7"])
        bot.send_message(message.chat.id, "8. " + timetable["m8"])
        bot.send_message(message.chat.id, "9. " + timetable["m9"])
    elif message.text == 'ВТ':
        bot.send_message(message.chat.id, "1. " + timetable["tu1"])
        bot.send_message(message.chat.id, "2. " + timetable["tu2"])
        bot.send_message(message.chat.id, "3. " + timetable["tu3"])
        bot.send_message(message.chat.id, "4. " + timetable["tu4"])
        bot.send_message(message.chat.id, "5. " + timetable["tu5"])
        bot.send_message(message.chat.id, "6. " + timetable["tu6"])
        bot.send_message(message.chat.id, "7. " + timetable["tu7"])
        bot.send_message(message.chat.id, "8. " + timetable["tu8"])
        bot.send_message(message.chat.id, "9. " + timetable["tu9"])
    elif message.text == 'СР':
        bot.send_message(message.chat.id, "1. " + timetable["w1"])
        bot.send_message(message.chat.id, "2. " + timetable["w2"])
        bot.send_message(message.chat.id, "3. " + timetable["w3"])
        bot.send_message(message.chat.id, "4. " + timetable["w4"])
        bot.send_message(message.chat.id, "5. " + timetable["w5"])
        bot.send_message(message.chat.id, "6. " + timetable["w6"])
        bot.send_message(message.chat.id, "7. " + timetable["w7"])
        bot.send_message(message.chat.id, "8. " + timetable["w8"])
        bot.send_message(message.chat.id, "9. " + timetable["w9"])
    elif message.text == 'ЧТ':
        bot.send_message(message.chat.id, "1. " + timetable["th1"])
        bot.send_message(message.chat.id, "2. " + timetable["th2"])
        bot.send_message(message.chat.id, "3. " + timetable["th3"])
        bot.send_message(message.chat.id, "4. " + timetable["th4"])
        bot.send_message(message.chat.id, "5. " + timetable["th5"])
        bot.send_message(message.chat.id, "6. " + timetable["th6"])
        bot.send_message(message.chat.id, "7. " + timetable["th7"])
        bot.send_message(message.chat.id, "8. " + timetable["th8"])
        bot.send_message(message.chat.id, "9. " + timetable["th9"])
    elif message.text == 'ПТ':
        bot.send_message(message.chat.id, "1. " + timetable["f1"])
        bot.send_message(message.chat.id, "2. " + timetable["f2"])
        bot.send_message(message.chat.id, "3. " + timetable["f3"])
        bot.send_message(message.chat.id, "4. " + timetable["f4"])
        bot.send_message(message.chat.id, "5. " + timetable["f5"])
        bot.send_message(message.chat.id, "6. " + timetable["f6"])
        bot.send_message(message.chat.id, "7. " + timetable["f7"])
        bot.send_message(message.chat.id, "8. " + timetable["f8"])
        bot.send_message(message.chat.id, "9. " + timetable["f9"])
    elif message.text == 'СБ':
        bot.send_message(message.chat.id, "1. " + timetable["s1"])
        bot.send_message(message.chat.id, "2. " + timetable["s2"])
        bot.send_message(message.chat.id, "3. " + timetable["s3"])
        bot.send_message(message.chat.id, "4. " + timetable["s4"])
        bot.send_message(message.chat.id, "5. " + timetable["s5"])
        bot.send_message(message.chat.id, "6. " + timetable["s6"])
        bot.send_message(message.chat.id, "7. " + timetable["s7"])
        bot.send_message(message.chat.id, "8. " + timetable["s8"])
        bot.send_message(message.chat.id, "9. " + timetable["s9"])





    if message.text == 'Биология':              bot.send_message(message.chat.id, 'По биологии задали: '                + hw["bio"])
    elif message.text == 'Турецкий(рус)':       bot.send_message(message.chat.id, 'По турецкому задали: '               + hw["tur1"])
    elif message.text == 'Турецкий(тат)':       bot.send_message(message.chat.id, 'По турецкому задали: '               + hw["tur2"])
    elif message.text == 'География':           bot.send_message(message.chat.id, 'По географии задали: '               + hw["geo"])
    elif message.text == 'ИЗО':                 bot.send_message(message.chat.id, 'По ИЗО задали: '                     + hw["art"])
    elif message.text == 'Английский(сред)':    bot.send_message(message.chat.id, 'По английскому(ср.группы) задали: '  + hw["eng1"])
    elif message.text == 'Английский(сил)':     bot.send_message(message.chat.id, 'По английскому(сил.группы) задали: ' + hw["eng2"])
    elif message.text == 'История':             bot.send_message(message.chat.id, 'По истории задали: '                 + hw["his"])
    elif message.text == 'Лит-ра':              bot.send_message(message.chat.id, 'По лит-ре задали: '                  + hw["lit"])
    elif message.text == 'Алгебра':             bot.send_message(message.chat.id, 'По алгебре задали: '                 + hw["geom"])
    elif message.text == 'Геометрия':           bot.send_message(message.chat.id, 'По геометрии задали: '               + hw["alge"])
    elif message.text == 'Музыка':              bot.send_message(message.chat.id, 'По музыке задали: '                  + hw["mus"])
    elif message.text == 'Общество':            bot.send_message(message.chat.id, 'По обществу задали: '                + hw["obs"])
    elif message.text == 'Род.лит(рус)':        bot.send_message(message.chat.id, 'По род.лит(рус) задали: '            + hw["rl1"])
    elif message.text == 'Родной(рус)':         bot.send_message(message.chat.id, 'По родной(рус) задали: '             + hw["rl2"])
    elif message.text == 'Род.лит(тат)':        bot.send_message(message.chat.id, 'По род.лит(тат) задали: '            + hw["r1"])
    elif message.text == 'Родной(тат)':         bot.send_message(message.chat.id, 'По родной(тат) задали: '             + hw["r2"])
    elif message.text == 'Рус.яз':              bot.send_message(message.chat.id, 'По рус.яз задали: '                  + hw["rus"])
    elif message.text == 'Технология':          bot.send_message(message.chat.id, 'По технологии задали: '              + hw["tec"])
    elif message.text == 'Физ-культура':        bot.send_message(message.chat.id, 'По физ-культуре задали: '            + hw["pe"])
    elif message.text == 'Физика':              bot.send_message(message.chat.id, 'По физике задали: '                  + hw["physic"])
    elif message.text == 'Информатика':         bot.send_message(message.chat.id, 'По информатике задали: '             + hw["info"])


    if message.text == 'Гусман бей':
        ind[nms.index("Гусман бей")] = message.chat.id
        bot.send_message(message.chat.id, "Рад познакомиться, надеюсь я буду вам полезен", reply_markup=main)
        updateind()

    elif message.text == 'Райнур абый':
        ind[nms.index("Райнур абый")] = message.chat.id
        bot.send_message(message.chat.id, "Рад познакомиться, надеюсь я буду вам полезен", reply_markup=main)
        updateind()

    elif message.text == 'Аккмалутдинов':
        ind[nms.index("Аккмалутдинов")] = message.chat.id
        bot.send_message(message.chat.id, "Рад познакомиться, надеюсь я буду вам полезен", reply_markup=main)
        updateind()

    elif message.text == 'Бариев':
        ind[nms.index("Бариев")] = message.chat.id
        bot.send_message(message.chat.id, "Рад познакомиться, надеюсь я буду вам полезен", reply_markup=main)
        updateind()

    elif message.text == 'Воробьев':
        ind[nms.index("Воробьев")] = message.chat.id
        bot.send_message(message.chat.id, "Рад познакомиться, надеюсь я буду вам полезен", reply_markup=main)
        updateind()

    elif message.text == 'Галаутдинов':
        ind[nms.index("Галаутдинов")] = message.chat.id
        bot.send_message(message.chat.id, "Рад познакомиться, надеюсь я буду вам полезен", reply_markup=main)
        updateind()

    elif message.text == 'Гашигулин':
        ind[nms.index("Гашигулин")] = message.chat.id
        bot.send_message(message.chat.id, "Рад познакомиться, надеюсь я буду вам полезен", reply_markup=main)
        updateind()

    elif message.text == 'Димухаметов':
        ind[nms.index("Димухаметов")] = message.chat.id
        bot.send_message(message.chat.id, "Рад познакомиться, надеюсь я буду вам полезен", reply_markup=main)
        updateind()

    elif message.text == 'Загидулин':
        ind[nms.index("Загидулин")] = message.chat.id
        bot.send_message(message.chat.id, "Рад познакомиться, надеюсь я буду вам полезен", reply_markup=main)
        updateind()

    elif message.text == 'Закиров':
        ind[nms.index("Закиров")] = message.chat.id
        bot.send_message(message.chat.id, "Рад познакомиться, надеюсь я буду вам полезен", reply_markup=main)
        updateind()

    elif message.text == 'Замалеев':
        ind[nms.index("Замалеев")] = message.chat.id
        bot.send_message(message.chat.id, "Рад познакомиться, надеюсь я буду вам полезен", reply_markup=main)
        updateind()

    elif message.text == 'Ильин':
        ind[nms.index("Ильин")] = message.chat.id
        bot.send_message(message.chat.id, "Рад познакомиться, надеюсь я буду вам полезен", reply_markup=main)
        updateind()

    elif message.text == 'Исмагилов':
        ind[nms.index("Исмагилов")] = message.chat.id
        bot.send_message(message.chat.id, "Рад познакомиться, надеюсь я буду вам полезен", reply_markup=main)
        updateind()

    elif message.text == 'Леухин':
        ind[nms.index("Леухин")] = message.chat.id
        bot.send_message(message.chat.id, "Рад познакомиться, надеюсь я буду вам полезен", reply_markup=main)
        updateind()

    elif message.text == 'Лукьянов':
        ind[nms.index("Лукьянов")] = message.chat.id
        bot.send_message(message.chat.id, "Рад познакомиться, надеюсь я буду вам полезен", reply_markup=main)
        updateind()

    elif message.text == 'Мифтахов':
        ind[nms.index("Мифтахов")] = message.chat.id
        bot.send_message(message.chat.id, "Рад познакомиться, надеюсь я буду вам полезен", reply_markup=main)
        updateind()

    elif message.text == 'МустафинК':
        ind[nms.index("МустафинК")] = message.chat.id
        bot.send_message(message.chat.id, "Рад познакомиться, надеюсь я буду вам полезен", reply_markup=main)
        updateind()

    elif message.text == 'МустафинС':
        ind[nms.index("МустафинС")] = message.chat.id
        bot.send_message(message.chat.id, "Рад познакомиться, надеюсь я буду вам полезен", reply_markup=main)
        updateind()

    elif message.text == 'Мухаметгалиев':
        ind[nms.index("Мухаметгалиев")] = message.chat.id
        bot.send_message(message.chat.id, "Рад познакомиться, надеюсь я буду вам полезен", reply_markup=main)
        updateind()

    elif message.text == 'ПимурзинРусл':
        ind[nms.index("ПимурзинРусл")] = message.chat.id
        bot.send_message(message.chat.id, "Рад познакомиться, надеюсь я буду вам полезен", reply_markup=main)
        updateind()

    elif message.text == 'ПимурзинРуст':
        ind[nms.index("ПимурзинРуст")] = message.chat.id
        bot.send_message(message.chat.id, "Рад познакомиться, надеюсь я буду вам полезен", reply_markup=main)
        updateind()

    elif message.text == 'Сахабутдинов':
        ind[nms.index("Сахабутдинов")] = message.chat.id
        bot.send_message(message.chat.id, "Рад познакомиться, надеюсь я буду вам полезен", reply_markup=main)
        updateind()

    elif message.text == 'Фаизов':
        ind[nms.index("Фаизов")] = message.chat.id
        bot.send_message(message.chat.id, "Рад познакомиться, надеюсь я буду вам полезен", reply_markup=main)
        updateind()

    elif message.text == 'Фазлиев':
        ind[nms.index("Фазлиев")] = message.chat.id
        bot.send_message(message.chat.id, "Рад познакомиться, надеюсь я буду вам полезен", reply_markup=main)
        updateind()

    elif message.text == 'Хамидулин':
        ind[nms.index("Хамидулин")] = message.chat.id
        bot.send_message(message.chat.id, "Рад познакомиться, надеюсь я буду вам полезен", reply_markup=main)
        updateind()

    elif message.text == 'Шамсиев':
        ind[nms.index("Шамсиев")] = message.chat.id
        bot.send_message(message.chat.id, "Рад познакомиться, надеюсь я буду вам полезен", reply_markup=main)
        updateind()

    elif message.text == 'Юсупов':
        ind[nms.index("Юсупов")] = message.chat.id
        bot.send_message(message.chat.id, "Рад познакомиться, надеюсь я буду вам полезен", reply_markup=main)
        updateind()


bot.polling()