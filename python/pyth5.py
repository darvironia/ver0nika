def decorator ():
    def dec (func):
      def wrapper ():
          print ("Код до выполнения функции")
          func()
          print ("Код, который сработал после функции")
      return wrapper
    return dec  

def test (func):
    def wrapper ():
        print ("Код до выполнения функции 2")
        func ()
        print ("Код, который сработал после функции 2")
    return wrapper

@decorator()
@test
def show ():
    print("Я обычная функция")
   
# show = decorator (show)
show ()