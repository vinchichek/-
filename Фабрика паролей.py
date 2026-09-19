import random, string

def generate_password(length=16, use_digits=True, use_symbols=True):
    chars = string.ascii_letters
    if use_digits:
        chars += string.digits
    if use_symbols:
        chars += "!@#$%^&*()-_=+"
    while True:
        password = "".join(random.choice(chars) for _ in range(length))
        if (any(c.isdigit() for c in password) and
                any(c.isalpha() for c in password) and
                any(c in "!@#$%^&*()-_=+" for c in password)):
            return password

def strength(password):
    score = len(password) * 4
    variety = len(set(password))
    return min(100, score + variety * 2)

if __name__ == "__main__":
    length = int(input("Длина пароля (Enter = 16): ") or 16)
    pwd = generate_password(length)
    print("Ваш пароль:", pwd)
    print("Надёжность:", strength(pwd), "% из 100")
    
# cmd
# python password_generator.py