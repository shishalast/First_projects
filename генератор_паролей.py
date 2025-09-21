import random  # подключаем модуль рандом

digits = "0123456789"  # создаём строковые константы
lowwercase_letters = "abcdefghijklmnopqrstuvwxyz"
uppercase_letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
punctuation = "!#$%&*+-=?@^_"
bad_symbols = "il1Lo0O"
chars = ""  # создали переменную, в которой будут содержаться символы пароля
answ1, answ2, answ3, answ4 = 0, 0, 0, 0

print("Здравствуйте, скажите пожалуйста, сколько паролей вы хотите сгенерировать?")
n = int(input())  # кол-во паролей для генерации

print("Какой длины должен быть ваш пароль?")
length = int(input())  # длина пароля

print("Включать ли цифры 0123456789? (Да/Нет)")
if input().lower() == "да":
    answ1 += 1

print("Включать ли прописные буквы ABCDEFGHIJKLMNOPQRSTUVWXYZ? (Да/Нет)")
if input().lower() == "да":
    answ2 += 1

print("Включать ли строчные буквы abcdefghijklmnopqrstuvwxyz? (Да/Нет)")
if input().lower() == "да":
    answ3 += 1

print("Включать ли символы !#$%&*+-=?@^_? (Да/Нет)")
if input().lower() == "да":
    answ4 += 1

print("Исключать ли неоднозначные символы il1Lo0O? (Да/Нет)")
if input().lower() == "да":
    digits = "".join(ch for ch in digits if ch not in bad_symbols)
    uppercase_letters = "".join(ch for ch in uppercase_letters if ch not in bad_symbols)
    lowwercase_letters = "".join(
        ch for ch in lowwercase_letters if ch not in bad_symbols
    )
    punctuation = "".join(ch for ch in punctuation if ch not in bad_symbols)

while len(chars) < length:
    if answ1 == 1:
        chars += random.choice(digits)
    if answ2 == 1:
        chars += random.choice(uppercase_letters)
    if answ3 == 1:
        chars += random.choice(lowwercase_letters)
    if answ4 == 1:
        chars += random.choice(punctuation)


def generate_password(length, chars):
    passw = random.sample(chars, length)
    return passw


for i in range(n):
    print(f"Ваш пароль № {i+1}:", end=" ")
    print(*generate_password(length, chars), sep="")
