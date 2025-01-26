matvarer = [['laks',59, 'middag'],
['kjøttdeig',25,'middag'],
['ris',15,'middag'],
['ost',99,'frokost'],
['bønner',7,'middag'],
['soyasaus',33,'middag'],
['banan',4,'mellommåltid']]

vare = input("Skriv inn matvare:")

# IKKE endre koden over her
# Skriv koden din mellom her...
def finn_pris(matvarer,let_etter):
#iterere gjennom listene
#finne index 2
#iterere gjennom dictonary ("key, value ")
#printe heltallet fra matvarer
    for matvare in matvarer:
        if matvare[0] == let_etter:
            return matvare[1]
    return 0
# ...og her
# IKKE endre koden under her
print(finn_pris(matvarer,vare))