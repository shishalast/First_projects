print(
    "Здравствуйте, вы хотите провести шифрование или дешифрование? (1 или 2)"
)  # запрашвиаем данные у пользователя
answer1 = int(input())
while answer1 != 1 and answer1 != 2: #проверка на правильность введённых данных
    print('Пожалуйста, введите корректные данные 1 или 2')
    answer1 = int(input())
    
print("Какой язык вы хотите использовать русский или английский? (рус или анг)")
answer2 = input()
while answer2 != 'rus' and answer2 != 'eng' and answer2 != 'рус' and answer2 != 'анг': #проверка на правильность введённых данных
    print('Пожалуйста, введите корректные данные 1 или 2')
    answer2 = input()

print("Какой шаг свдига вправо вам нужен?")
answer3 = int(input())
while answer3 < 1 : #проверка на правильность введённых данных
    print('Пожалуйста, введите корректные данные 1 или 2')
    answer3 = int(input())

print("Введите ваш текст")
text = input()


def rus_text(text, answ1, answ3): #Функция по использованию шифра для русского алфавита
    alphabet = "абвгдеёжзийклмнопрстуфхцчшщъыьэюя"
    alphabet_upper = 'АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ'
    new_text = "" #создаём пустую строку для будущего результата
    for ch in text: #проверяем каждый символ в ввёденом тексте 
        if ch in alphabet: #если буквы строчные
            index = alphabet.index(ch)
            if answ1 == 1: #шифрование
                new_index = (index + answ3) % len(alphabet)
            else: #дешифрование
                new_index = (index - answ3) % len(alphabet)
            new_text += alphabet[new_index] #добавляем в нашу строку новый зашифрованный символ
        elif ch in alphabet_upper: #если буквы заглавные
            index = alphabet_upper.index(ch)
            if answ1 == 1:
                new_index = (index + answ3) % len(alphabet_upper)
            else:
                new_index = (index - answ3) % len(alphabet_upper) 
            new_text += alphabet_upper[new_index]
        else: # если символ не является буквенным, то мы его добавляем без изменений
            new_text += ch
    return (f'Ваш текст готов - «{new_text}»') #возвращаем новый текст

def eng_text(text, answ1, answ3):  #Функция по использованию шифра для английского алфавита
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    alphabet_upper = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    new_text = "" #создаём пустую строку для будущего результата
    for ch in text:
        if ch in alphabet: #если буквы строчные
            index = alphabet.index(ch)
            if answ1 == 1: #шифрование
                new_index = (index + answ3) % len(alphabet)
            else: #дешифрование
                new_index = (index - answ3) % len(alphabet)
            new_text += alphabet[new_index]
        elif ch in alphabet_upper: #если буквы заглавные
            index = alphabet_upper.index(ch)
            if answ1 == 1:
                new_index = (index + answ3) % len(alphabet_upper)
            else:
                new_index = (index - answ3) % len(alphabet_upper) 
            new_text += alphabet_upper[new_index]
        else:
            new_text += ch
    return (f'Ваш текст готов - «{new_text}»')


if answer2 == "рус" or answer2 == 'rus': #в зависимости от введённых данных мы выводим функцию или с русским, или с английским алфавитом
    print(rus_text(text, answer1, answer3))
else:
    print(eng_text(text, answer1, answer3))
