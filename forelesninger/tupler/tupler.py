liste = [1,3,5,7,9,]*5

n = len(liste)
for i in range(0,n,3):
    y = liste[i]**2
    print(y, end=", ")


def min_funksjon(liste):
    liste.append("Jeg lister med stilt på tå...")

min_liste = [1,2]
min_funksjon(min_liste)

print(min_liste)
