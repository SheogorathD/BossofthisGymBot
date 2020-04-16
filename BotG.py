# Cya, Boss of this Gym

import telebot


bot = telebot.TeleBot('TOKEN')


keyboard1 = telebot.types.ReplyKeyboardMarkup(True)
keyboard1.row('/GachiPhrase', '/SayMyName')

keyboard2 = telebot.types.ReplyKeyboardMarkup(True)
keyboard2.row('/FuckYouLeatherMan', '/DeepDarkFantasies', '/FistingIs300Bucks', '/FuckYou')
keyboard2.row('/ItTunsMeOn', '/BondageGayWebSite', '/SoFkDeep', '/WhatAreYouDoing')  # If you'll use this method like
keyboard2.row('/ImSorry', '/SryForWhat', '/YesSir', '/WrongDoor')  # here, you'll be able to create some lines
keyboard2.row('/WhatAreYouDoing', '/ThatsAmazing', '/TakeItBoy', '/Swallow')  # It's better than one big line, trust me
keyboard2.row('/GetBackHere', '/OurDadToldUs', '/IAm', '/FkGoBack')


@bot.message_handler(commands=['start'])
def start_message(message):
    bot.send_message(message.chat.id, 'Fuck you', reply_markup=keyboard1)
    sti = open('pic\wan.webp', 'rb')  # path to picture, I won't write this comment anymore
    bot.send_sticker(message.chat.id, sti)


@bot.message_handler(commands=['GachiPhrase'])
def gachi_sound(message):
    bot.send_message(message.chat.id, 'Yes, Master', reply_markup=keyboard2)
    pic = open('pic\master.jpeg', 'rb')
    bot.send_sticker(message.chat.id, pic)


@bot.message_handler(commands=['FuckYouLeatherMan'])
def leather_man(message):
    bot.send_message(message.chat.id, 'Yes, my Master', reply_markup=keyboard2)
    audio = open('sound\leather.mp3', 'rb')
    bot.send_audio(message.chat.id, audio)


@bot.message_handler(commands=['DeepDarkFantasies'])
def ddf(message):
    bot.send_message(message.chat.id, 'Yes, my Master', reply_markup=keyboard2)
    audio = open('sound\DeepDarkFantasies.mp3', 'rb')
    bot.send_audio(message.chat.id, audio)


@bot.message_handler(commands=['FistingIs300Bucks'])
def fisting(message):
    bot.send_message(message.chat.id, 'Yes, my Master', reply_markup=keyboard2)
    audio = open('sound\FistingIs300Bucks.mp3', 'rb')
    bot.send_audio(message.chat.id, audio)


@bot.message_handler(commands=['FuckYou'])
def fyou(message):
    bot.send_message(message.chat.id, 'Yes, my Master', reply_markup=keyboard2)
    audio = open('sound\FuckYou.mp3', 'rb')
    bot.send_audio(message.chat.id, audio)


@bot.message_handler(commands=['ItTunsMeOn'])
def fyou(message):
    bot.send_message(message.chat.id, 'Yes, my Master', reply_markup=keyboard2)
    audio = open('sound\ItTunsMeOn.mp3', 'rb')
    bot.send_audio(message.chat.id, audio)


@bot.message_handler(commands=['BondageGayWebSite'])
def fyou(message):
    bot.send_message(message.chat.id, 'Yes, my Master', reply_markup=keyboard2)
    audio = open('sound\BondageGayWebSite.mp3', 'rb')
    bot.send_audio(message.chat.id, audio)


@bot.message_handler(commands=['SoFkDeep'])
def fyou(message):
    bot.send_message(message.chat.id, 'Yes, my Master', reply_markup=keyboard2)
    audio = open('sound\SoFkDeep.mp3', 'rb')
    bot.send_audio(message.chat.id, audio)


@bot.message_handler(commands=['ImSorry'])
def fyou(message):
    bot.send_message(message.chat.id, 'Yes, my Master', reply_markup=keyboard2)
    audio = open('sound\ImSorry.mp3', 'rb')
    bot.send_audio(message.chat.id, audio)


@bot.message_handler(commands=['SryForWhat'])
def fyou(message):
    bot.send_message(message.chat.id, 'Yes, my Master', reply_markup=keyboard2)
    audio = open('sound\SryForWhat.mp3', 'rb')
    bot.send_audio(message.chat.id, audio)


@bot.message_handler(commands=['YesSir'])
def fyou(message):
    bot.send_message(message.chat.id, 'Yes, my Master', reply_markup=keyboard2)
    audio = open('sound\YesSir.mp3', 'rb')
    bot.send_audio(message.chat.id, audio)


@bot.message_handler(commands=['WrongDoor'])
def fyou(message):
    bot.send_message(message.chat.id, 'Yes, my Master', reply_markup=keyboard2)
    audio = open('sound\WrongDoor.mp3', 'rb')
    bot.send_audio(message.chat.id, audio)


@bot.message_handler(commands=['WhatAreYouDoing'])
def fyou(message):
    bot.send_message(message.chat.id, 'Yes, my Master', reply_markup=keyboard2)
    audio = open('sound\WhatAreYouDoing.mp3', 'rb')
    bot.send_audio(message.chat.id, audio)


@bot.message_handler(commands=['ThatsAmazing'])
def fyou(message):
    bot.send_message(message.chat.id, 'Yes, my Master', reply_markup=keyboard2)
    audio = open('sound\ThatsAmazing.mp3', 'rb')
    bot.send_audio(message.chat.id, audio)


@bot.message_handler(commands=['TakeItBoy'])
def fyou(message):
    bot.send_message(message.chat.id, 'Yes, my Master', reply_markup=keyboard2)
    audio = open('sound\TakeItBoy.mp3', 'rb')
    bot.send_audio(message.chat.id, audio)


@bot.message_handler(commands=['Swallow'])
def fyou(message):
    bot.send_message(message.chat.id, 'Yes, my Master', reply_markup=keyboard2)
    audio = open('sound\Swallow.mp3', 'rb')
    bot.send_audio(message.chat.id, audio)


@bot.message_handler(commands=['GetBackHere'])
def fyou(message):
    bot.send_message(message.chat.id, 'Yes, my Master', reply_markup=keyboard2)
    audio = open('sound\GetBackHere.mp3', 'rb')
    bot.send_audio(message.chat.id, audio)


@bot.message_handler(commands=['OurDadToldUs'])
def fyou(message):
    bot.send_message(message.chat.id, 'Yes, my Master', reply_markup=keyboard2)
    audio = open('sound\OurDadToldUs.mp3', 'rb')
    bot.send_audio(message.chat.id, audio)


@bot.message_handler(commands=['IAm'])
def fyou(message):
    bot.send_message(message.chat.id, 'Yes, my Master', reply_markup=keyboard2)
    audio = open('sound\IAm.mp3', 'rb')
    bot.send_audio(message.chat.id, audio)


@bot.message_handler(commands=['WhatAreYouDoing'])
def fyou(message):
    bot.send_message(message.chat.id, 'Yes, my Master', reply_markup=keyboard2)
    audio = open('sound\WhatAreYouDoing.mp3', 'rb')
    bot.send_audio(message.chat.id, audio)



@bot.message_handler(commands=['FkGoBack'])
def back(message):
    bot.send_message(message.chat.id, 'Yes, Master', reply_markup=keyboard1)
    pic = open('pic\master.jpeg', 'rb')


@bot.message_handler(commands=['SayMyName'])
def gachi_name(message):
    bot.reply_to(message, 'You are my Dungeon Master')
    pic = open('pic\dmasta.jpg', 'rb')
    bot.send_sticker(message.chat.id, pic)


@bot.message_handler(content_types=['sticker'])
def sticker_id(message):
    print(message)


while True:     # This helps to keep bot alive
    try:
        bot.polling(none_stop=True)
    except Exception as e:
        print('Connection Error', e)
        time.sleep(15)
