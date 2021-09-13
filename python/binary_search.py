list = [100-i for i in range(0, 100)]

number = int (input ("Введите число: "))

# def includes (l, n):
#   left = 0
#   right = len(l)
#   step = 0
#   f = False
#   while True:
#     step += 1
#     i = (left + right) // 2
#     if left == right:
#       break
#     elif l[i] > n:
#       left = i + 1
#     elif l[i] < n:
#       right = i
#     else:
#       f = True
#       break

#   print (step)
#   return f

def includes (l, n):
  def find (left, right):
    i = (left + right) // 2
    if left == right:
      return False
    elif l[i] > n:
      return find(i + 1, right)
    elif l[i] < n:
      return find(left, i)
    else:
      return True

  return find(0, len(l))    


print (includes(list, number))
