import random

print("Давай пограємо у гру)")
name = input("Enter your name: ")
print(" ")
print('Гра загадала число від 1 до 50. Тобі треба його відгадати. Гра дає підказки: '
      'якщо введене користувачем число менше загаданого на 10 (в будь-який бік) - "Холодно", '
      'якщо на 5-9 - "Тепло", '
      'якщо менше 5 - "Гаряче".')

target_number = random.randint(0, 60)

while True:
    print(" ")
    user_input = int(input("Введіть позитивне число: "))
    result = user_input - target_number
    if user_input == target_number:
        print("Ви вгадали!")
        break
    if abs(result) >= 10:
        print("Холодно")
    if 5 <= abs(result) <= 9:
        print("Тепло")
    if abs(result) <= 5:
        print("Гаряче")