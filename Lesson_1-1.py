# Найдите сумму цифр трехзначного числа.
#*Пример:*
#123 -> 6 (1 + 2 + 3)
#100 -> 1 (1 + 0 + 0) |

num = input("Введите любое трехзначное число: ")
print(f"Вы ввели число {num}")
if len(num) != 3:
  print("Вы ввели не трехзначное число!")
else:
  print(f"{int(num[0])} + {int(num[1])} + {int(num[2])} = {int(num[0])+int(num[1])+int(num[2])}")