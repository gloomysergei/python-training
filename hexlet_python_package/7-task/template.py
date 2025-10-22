# function = number * fact(number - 1)
def fact(number):
  if number == 1 or number == 0:
    return 1
  return number * fact(number - 1)
n = 4
i = 0
result = fact(n) // (fact(i) * fact(n - i))
print(result)
  