number = 2
sg = 'abcdef'
result = sg[0:number]
print(result)
result = sg[number:number + number]
print(result)
result = sg[number + number:number + number + number]
print(result)
number += number
print(number)