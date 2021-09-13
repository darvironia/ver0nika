a = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

# def sort (l):
#   r = l
#   n = len(r)
#   step = 0
#   for i in range (1, n):
#     for j in range (0, i):
#       if r[j] < r[i]:
#         tmp = r[j]
#         r[j] = r[i]
#         r[i] = tmp
#       step += 1
#   print (step)
#   return r

def sort (l):
  r = l
  n = len(r)
  steps = 0
  swaps = 0
  while True:
    swapped = False
    for i in range (1, n):
      if r[i] < r[i-1]:
        tmp = r[i-1]
        r[i-1] = r[i]
        r[i] = tmp
        swapped = True
        swaps += 1
      steps += 1

    if not swapped:
      break
    n -= 1
  
  
  print (steps)
  print (swaps)
  return r

print (a)
print (sort(a))

