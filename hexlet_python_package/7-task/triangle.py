def fact(number):
  if number == 1 or number == 0:
    return 1
  return number * fact(number - 1)

def triangle(n):
  lst = []
  for i in range(0, n + 1):
    result = fact(n) // (fact(i) * fact(n - i))
    lst.append(result)
  return lst

print(triangle(6))