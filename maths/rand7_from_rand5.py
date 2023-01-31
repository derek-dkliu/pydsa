import random

def rand5():
    return random.randint(0, 4)

def rand25():
    return rand5() * 5 + rand5()

def rand7():
    num = rand25()
    while num > 20:
        num = rand25()
    return num // 3

for _ in range(7):
    print(rand7())
    
    