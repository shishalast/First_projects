import random

number = random.randint(0, 100)  # Генерируем случайное число от 0 до 100
print("Добро пожаловать в числовую угадайку!")

print("Введите пожалуйста целое число")
number1 = int(input())  # Просим ввести число

cnt = 0  # вводим счётчик попыток


def is_valid(
    num,
):  # Функция проверяет является ли введённые данные числом из заданного промежутка
    if num >= 0 and num <= 100:
        return True
    else:
        return False


while is_valid(number1) == True:  # Проверяем угадали ли число
    if number1 == int(number):
        print(f"Поздравляю, вы угадали число, вам потребовалось {cnt} попыток!")
        break
    elif number > number1:
        cnt += 1
        print("Ваше число меньше загаданного, попробуйте ещё раз")
        number1 = int(input())
        continue
    else:
        cnt += 1
        print("Ваше число больше загаданного, попробуйте ещё раз")
        number1 = int(input())
        continue
else:
    print("А может всё таки введём целое число от 1 до 100?")
    number1 = int(input())

print("Спасибо, что играли в числовую угадайку, до скорых встреч)")
