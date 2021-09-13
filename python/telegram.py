import pyowm
import telebot

owm = pyowm.OWM('fd688cedc9202c33d316dda05b28df8e')
mgr = owm.weather_manager()
bot = telebot.TeleBot("1993633105:AAG2kMF6zE9XK7uWvwD4x-N7wCMhBrJyz2M")

@bot.message_handler(content_types=['text'])
def send_echo(message):
  try:
    observation = mgr.weather_at_place( message.text)
    w = observation.weather
    
    temp = w.temperature('celsius')["temp"]

    answer = "В городе " + message.text + " сейчас " + w.detailed_status + "\n"
    answer += "Температура в районе " + str(temp) + "\n\n"
    
    if temp < 0:
      answer += "Хочешь отморозить уши? Окей, я тебя не держу"
    elif temp < 10:
      answer += "Там дубак как на северном полюсе"
    elif temp < 20:
      answer += "Нормас, но возьми что-нибудь"
    elif temp > 25:
      answer += "Ахтунг! Там грёбаная баня"
    elif temp > 20:
      answer += "Зашибись, самое оно"
  except:
    answer = "Хде?"

  bot.send_message(message.chat.id, answer)

bot.polling( none_stop= True )