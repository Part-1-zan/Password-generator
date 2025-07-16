import random

chisla = "+-/*!&$#?=@abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"
dlina = int(input('Введите требуюмую длину пароля:'))
password = ''
for i in range(dlina):
    f = random.choice(chisla)
    password+=f
print(' Твой пароль: ', password)