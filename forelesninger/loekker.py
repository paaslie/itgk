import random
tall = random.randint(1, 100)
gjett = int(input('Gjett et tall mellom 1 og 100 :'))

while gjett != tall:
    gjett = int(input('Gjett et tall mellom 1 og 100 :'))
    if gjett == tall:
        print('Riktig!')
    elif gjett > tall:
        print('Det er feil.')
print()

