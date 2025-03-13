import random

def random_word():
    words = ['голова', 'зубы', 'машина', 'учебник', 'шкаф', 'рыба']
    random_word = random.choice(words)  
    return (random_word)
  

def display_word (random_word, letters):
    return " ".join([letter if letter in letters  else "_" for letter in random_word])

def play():
    word = random_word()
    letters = set() # создаем 
    health_point = 6
    q = len(word)
    print(f'Привет! Твое слово из {q} букв')

    print(display_word(word, letters)) 

    while health_point > 0:
        user_input = input("Введите букву: ")
        if len(user_input) != 1 or not user_input.isalpha():
            print ('Ты дебил, напиши букву ')
            continue
        if user_input in letters:
            print ('вы уже вводили эту букву')
            continue
        letters.add(user_input)
        if user_input not in word:
            health_point -= 1
            print ('такой буквы нет')
            print (f'Осталось {health_point} жизней')
        map_display = display_word(word, letters) 
        print(map_display)
        if "_" not in map_display:
            print ('Поздравляем, вы прошли игру')
            break
    if health_point == 0:
        print ("Вы проиграли")

play ()