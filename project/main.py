#pip install pyTelegramBotApi

from telebot import types
import telebot
import time


bot = telebot.TeleBot('5358273204:AAGEdr1ChMcnkw1kVU22f-i23YxlLB0KsRw')


@bot.message_handler(commands=['start'])
def start(message):

    global timenow
    global a2

    timenow = int(''.join((' '.join(time.asctime().split()[3:-1])).split(':')[0]))
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = types.KeyboardButton("/help")
    btn2 = types.KeyboardButton("/eng")
    markup.add(btn1, btn2)

    a1 = ''
    a2 = ''

    if 23 < timenow < 24 or 0 <= timenow <= 6:
        a1 = 'Доброй ночи'
        a2 = 'Goodnight'
    elif 6 < timenow <= 12:
        a1 = 'Доброе утро'
        a2 = 'Good morning'
    elif 12 < timenow <= 18:
        a1 = 'Доброго дня'
        a2 = 'Good day'
    elif 18 < timenow <= 23:
        a1 = 'Доброго вечера'
        a2 = 'Good evening'

    bot.send_message(message.chat.id, f"{a1}, {message.from_user.first_name}! Я бот,"
                                      f" который создает напоминания для тебя!"
                                      f"\n"
                                      f"\n"
                                      f"Введите /help для того, чтобы увидеть возможности бота.\n"
                                      f"\n"
                                      f"Для того чтобы поменять язык на английский, введите /eng"
                                      f" - (change language to english)")


@bot.message_handler(commands=['help'])
def help(message):

    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = types.KeyboardButton("/donate")
    btn2 = types.KeyboardButton("/info")
    btn3 = types.KeyboardButton("/note")
    markup.add(btn1, btn2, btn3)

    bot.send_message(message.chat.id,
                     text="Функции бота: \n"
                          "/donate - пожертвованя разработчикам \n"
                          "/info - информация о боте, для чего он нужен \n"
                          "/note - создает напоминание".format(
                         message.from_user), reply_markup=markup)


@bot.message_handler(commands=['eng'])
def help_eng(message):

    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn4 = types.KeyboardButton("/donate_en")
    btn5 = types.KeyboardButton("/info_en")
    btn6 = types.KeyboardButton("/note_en")
    markup.add(btn4, btn5, btn6)

    bot.send_message(message.chat.id, f"{a2}, {message.from_user.first_name}! I'm a bot"
                                      f" which creates reminders for you!\n"
                                      f"\n"
                                      f"Bot features:\n"
                                      f"/donate_en - donation to developers\n"
                                      f"/info_en - information about the bot, what it is for\n"
                                      f"/note_en - creates a reminder")


@bot.message_handler(commands=['donate'])
def donate(message):
    markup = types.InlineKeyboardMarkup()
    button1 = types.InlineKeyboardButton("Донат", url='https://www.donationalerts.com/r/dailyday')
    markup.add(button1)
    bot.send_message(message.chat.id,
                     text="Ссылка на пожертвование: \n "
                          "https://www.donationalerts.com/r/dailyday".format(
                         message.from_user), reply_markup=markup)


@bot.message_handler(commands=['donate_en'])
def donate_en(message):
    markup = types.InlineKeyboardMarkup()
    button1 = types.InlineKeyboardButton("Donate", url='https://www.donationalerts.com/r/dailyday')
    markup.add(button1)
    bot.send_message(message.chat.id,
                     text="Donation Link: \n "
                          "https://www.donationalerts.com/r/dailyday".format(
                         message.from_user), reply_markup=markup)


@bot.message_handler(commands=['info'])
def info(message):
    bot.send_message(message.chat.id,
                     text="Что может делать этот бот? \n"
                          "- Вы можете узнать сколько времени! \n"
                          "- Вы можете создать заметку и через определенное время бот вам об этом напишет! \n"
                          "- Так же вы можете помочь нам в продвижении бота."
                          " А именно задонатить небольшую сумму денег!\n"
                          "\n"
                          "Кто работал над создание?\n"
                          "- Зданович Никита\n"
                          "- Вечаслав Егоров\n"
                          "\n"
                          "Контакты и поддержка - ОТСУТСТВУЕТ".format(
                         message.from_user))


@bot.message_handler(commands=['info_en'])
def info_en(message):
    bot.send_message(message.chat.id,
                     text="What can this bot do?? \n"
                          "- You can create a note and after a certain time the bot will write to you about it! \n"
                          "- You can also help us promote the bot."
                          " Namely, donate a sum of money!\n"
                          "\n"
                          "Who worked on the creation?\n"
                          "- Zdanovich Nikita\n"
                          "- Vechyaslav Egorov\n"
                          "\n"
                          "Contacts and support - NONE".format(
                         message.from_user))


@bot.message_handler(commands=['note'])
@bot.message_handler(content_types=["text"])
def reminder(message):
    if message.text == "/note":
        bot.send_message(message.chat.id,
                         text="Напишите, через сколько времени вы хотите сделать напоминание. \n"
                              "Например: чч:мм:сс\n"
                              "\n"
                              "Либо введите через какое количество секунд вы хотите получить сообщение".format(
                             message.from_user))
        bot.register_next_step_handler(message, clock)

    if message.text == "/note_en":
        bot.send_message(message.chat.id,
                         text="Enter how soon you want to be reminded. \n"
                              "For example: hours:minutes:seconds\n"
                              "\n"
                              "Or enter after what time you want to receive a message".format(
                             message.from_user))
        bot.register_next_step_handler(message, clock_en)


def clock(message):

    global hour
    global minutes
    global sec

    hour = 0
    minutes = 0
    sec = 0
    alert = message.text.split(':')
    if len(alert) == 3:
        if alert[0].isdigit() == True and alert[1].isdigit() == True and alert[2].isdigit() == True:
            if 1 <= len(alert[0]) <= 2 and 1 <= len(alert[1]) <= 2 and 1 <= len(alert[2]) <= 2:
                if 0 <= int(alert[0]) <= 99 and 0 <= int(alert[1]) <= 59 and 0 <= int(alert[2]) <= 59:
                    hour += int(alert[0])
                    minutes += int(alert[1])
                    sec += int(alert[2])
                    bot.send_message(message.chat.id, f'Введите свою заметку.')
                    bot.register_next_step_handler(message, msg)
                else:
                    bot.send_message(message.chat.id, f'Ошибка в вводе чисел!!! \n'
                                                      f'Заметьте, количество часов НЕ может привышать 99,'
                                                      f'количество минут и секунд НЕ может привышать 59. \n'
                                                      f'\n'
                                                      f'Введите время занова')
                    bot.register_next_step_handler(message, clock)
            else:
                bot.send_message(message.chat.id, f'Ошибка в вводе чисел!!! \n'
                                                  f'Заметьте, числа можно записать только ОДНОЙ цифрой'
                                                  f'или ДВУМЯ!!! \n'
                                                  f'\n'
                                                  f'Введите время занова')
                bot.register_next_step_handler(message, clock)

        else:
            bot.send_message(message.chat.id, f'Ошибка в вводе!!! \n'
                                              f'Время НЕЛЬЗЯ записать буквами!!!\n'
                                              f'\n'
                                              f'Введите время занова')
            bot.register_next_step_handler(message, clock)

    elif len(alert) == 1:
        if alert[0].isdigit() == True:
            sec += int(alert[0])
            bot.send_message(message.chat.id, f'Введите свою заметку.')
            bot.register_next_step_handler(message, msg)

        else:
            bot.send_message(message.chat.id, f'Ошибка в вводе!!! \n'
                                              f'Время НЕЛЬЗЯ записать буквами!!!\n'
                                              f'\n'
                                              f'Введите время занова')
            bot.register_next_step_handler(message, clock)


def clock_en(message):

    global hour1
    global minutes1
    global sec1

    hour1 = 0
    minutes1 = 0
    sec1 = 0
    alert = message.text.split(':')
    if len(alert) == 3:
        if alert[0].isdigit() == True and alert[1].isdigit() == True and alert[2].isdigit() == True:
            if 1 <= len(alert[0]) <= 2 and 1 <= len(alert[1]) <= 2 and 1 <= len(alert[2]) <= 2:
                if 0 <= int(alert[0]) <= 99 and 0 <= int(alert[1]) <= 59 and 0 <= int(alert[2]) <= 59:
                    hour1 += int(alert[0])
                    minutes1 += int(alert[1])
                    sec1 += int(alert[2])
                    bot.send_message(message.chat.id, f'Enter your note.')
                    bot.register_next_step_handler(message, msg_en)
                else:
                    bot.send_message(message.chat.id, f'Error in entering numbers!!! \n'
                                                      f'Note that the number of hours can NOT exceed 99,'
                                                      f'the number of minutes and seconds cannot exceed 59. \n'
                                                      f'\n'
                                                      f'Enter the time again')
                    bot.register_next_step_handler(message, clock_en)
            else:
                bot.send_message(message.chat.id, f'Error in entering numbers!!! \n'
                                                  f'Note that numbers can only be written with ONE digit'
                                                  f'or TWO!!! \n'
                                                  f'\n'
                                                  f'Enter the time again')
                bot.register_next_step_handler(message, clock_en)

        else:
            bot.send_message(message.chat.id, f'Error in entering!!! \n'
                                              f'Time CANNOT be spelled out!!!\n'
                                              f'\n'
                                              f'Enter the time again')
            bot.register_next_step_handler(message, clock_en)

    elif len(alert) == 1:
        if alert[0].isdigit() == True:
            sec1 += int(alert[0])
            bot.send_message(message.chat.id, f'Enter your note.')
            bot.register_next_step_handler(message, msg_en)

        else:
            bot.send_message(message.chat.id, f'Input error!!! \n'
                                              f'Time CANNOT be spelled out!!!\n'
                                              f'\n'
                                              f'Enter the time again')
            bot.register_next_step_handler(message, clock_en)


def msg(message):
    note = message.text
    bot.send_message(message.chat.id, f'Спасибо! Мы получили вашу заметку! \n'
                                      f'Напоминание будет через {hour}ч {minutes}мин {sec}сек')

    hour_new = hour * 60 * 60
    minutes_new = minutes * 60
    sec_new = sec
    total_time = hour_new + minutes_new + sec_new
    time.sleep(total_time)
    bot.send_message(message.from_user.id, f'Здравствуйте, {message.from_user.first_name}! Напоминание для вас: \n'
                                           f'\n'
                                           f'{note}')


def msg_en(message):
    note = message.text
    bot.send_message(message.chat.id, f'Thank you! We have received your note! \n'
                                      f'Reminder will be in {hour1}h {minutes1}m {sec1}s')

    hour_new = hour1 * 60 * 60
    minutes_new = minutes1 * 60
    sec_new = sec1
    total_time = hour_new + minutes_new + sec_new
    time.sleep(total_time)
    bot.send_message(message.from_user.id, f'Hello, {message.from_user.first_name}! Reminder for you: \n'
                                           f'\n'
                                           f'{note}')


bot.polling(none_stop=True)