import random

def guess_number():
    secret = random.randint(1, 100)
    attempts = 0

    print("Я загадал число от 1 до 100. Угадай!")
    while True:
        guess = int(input("Твой вариант: "))
        attempts += 1

        if guess < secret:
            print("Больше!")
        elif guess > secret:
            print("Меньше!")
        else:
            print(f"Правильно! Ты угадал за {attempts} попыток.")
            break

guess_number()
