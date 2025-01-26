#a 
streng = input()
tall = float(input())
# IKKE endre koden over her
# Skriv koden din mellom her...
def alfa(streng,tall):
    if tall == 0:
        print(min(streng))
    elif tall>0:
        print(max(streng))
# ...og her
# IKKE endre koden under her
print(alfa(streng,tall))