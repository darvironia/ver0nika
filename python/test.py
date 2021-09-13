import pyowm

owm = pyowm.OWM(
  'fd688cedc9202c33d316dda05b28df8e'
)
mgr = owm.weather_manager()

place = input("В каком городе/стране?: ")

observation = mgr.weather_at_place(place)
w = observation.weather

temp = w.temperature('celsius')["temp"]

print("В городе " + place + " сейчас " + w.detailed_status)
print( "Температура в районе " + str(temp))

if temp < 10:
    print("Там дубак как на северном полюсе")

elif temp < 0:
   print("Хочешь отморозить уши? Окей, я тебя не держу")

elif temp < 20:
    print("Нормас, но возьми что-нибудь")

elif temp > 30:
    print("Ахтунг! Там грёбаная баня")

elif temp > 20:
    print("Зашибись, самое оно")