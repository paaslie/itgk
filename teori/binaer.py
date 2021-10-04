spørsmål = print(input("Skriv inn spørsmål"))
svar = input(print("Skriv inn svar"))
poeng = 0

while spørsmål != "Ingen flere spørsmål":
    svar = input()
    riktig_svar = input()
    
    if svar == riktig_svar:
        print("Riktig svar! Du har", poeng, "poeng")
        poeng += 7
    
    if not poeng % 10:
        print("🥳")
        
    elif poeng // 10 == 2:
        print("Tjuetalls poeng? Bra jobbet!")
    poeng += 1
    
    spørsmål = input()
print(poeng)