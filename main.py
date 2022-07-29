# Для работы данного кода нужны модули colorama, pyTelegramBotAPI
import telebot
from colorama import Back
import config as cfg
import init_gram as i
import time
bot = telebot.TeleBot(cfg.token, parse_mode=None)
hm = None
print(Back.GREEN)
print("Бот был запущен \n Чтобы открыть меню введите в консоль :menu \n :help - помощь по 0xgram \n Чтобв начать пользование введите start")
print(Back.RESET)
info = input("\n")

if info.lower() == ":help":
  print(Back.MAGENTA)
  print(f"Помощь по 0xgram: \n Чтобы войти в меню напишите :menu в консоле когда пользователи будут нажимать на кнопку \"Старт\" в боте и писать сообщение вам будет приходить информация о пользователи и сообщение и вы сможете на него ответить в будущем будут выходить обновления и добавлятся новые фишки Удачного вам пользования :3 \n Информация о 0xgram: \n Версия {i.version} \n Создатель кода: {i.owner}")
  print(Back.RESET)
  info = input("\n")
   
   
if info.lower() == ":menu":
  print(Back.YELLOW)
  print("Меню: \n 1 - Написать сообщение пользователю (обязательно этот пользователь должен нажать кнопку старт чтобы сообщение отправилось) \n 2 - Получить информацию о боте \n 3 - завершить код \n 4 - отчистить консоль")
  print(Back.RESET)
  hm = input("\n")
  
if info.lower() == "start":
    print("Успешно")

if hm == "1":
    try:
      print("0xgram >>> Введите chatif пользователя которому хотите отправить сообщение")
      chidstr = input("\n")
      chid = int(chidstr)
      print("0xgram >>> Введите текст сообщения")
      txtmsg = input("\n")
      bot.send_message(chid, txtmsg)
    except:
      print("Произошла ошибка")
  
  
if hm == "2":
  print(f"Токен: {cfg.token} \n Имя бота: {cfg.botname}")
  
if hm == "3":
  print("Код был завершен")
  exit(0)
  
if hm == "4":
  print("Отчистка консоли...")
  time.sleep(0.5)
  i.clear()
  info = ":menu"
  hm = None
  

@bot.message_handler()
def on_message(message):
  userid = message.chat.id
  first_name = message.from_user.first_name
  msgtxt = message.text
  print(Back.CYAN)
  print(f"0xgram >>> Пришло новое сообщение \n Chatid: {userid} \n first_name: {first_name}")
  print(Back.YELLOW)
  print(f"Текст сообщения: {msgtxt}")
  print(Back.CYAN)
  replyinfo = input("Вы хотите отправить сообщение с пересылкой его пользователю (ответить) или нет \n Если да - 1 Если нет - 2")
  print("Чтобы отправить сообщение пользователю введите текст сообщения \n")
  textmsg = input("\n")
  if textmsg == "kekskksjekefieir7473iKkKkrkdkdkkeoeidid":
      print("\n")
  else:
    if replyinfo == "1":
      bot.reply_to(message, textmsg)
      print("Отправленно успешно")
      print(Back.RESET)
    else:
      bot.send_message(message.chat.id, textmsg)
      print("Сообщение отправленно")
      print(Back.RESET)
      if cfg.clearmsg == True:
          print("Отчистка консоли...")
          time.sleep(1)
          i.clear()
     

bot.polling(none_stop=True, interval=0)