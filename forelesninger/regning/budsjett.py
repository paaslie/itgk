budsjett = float(input("Hva er budsjettet ditt denne måneden?"))
differens = budsjett
belop = float(input("Oppgi beløp som er brukt (0 avslutter):"))

while belop != 0:
    differens -= belop
    belop = float(input("Oppgi beløp som er brukt (0 avslutter)"))

if differens == 0:
    print("Du har gått i balance.")
elif differens > 0:
    print(f"Du har et overskudd på {differens:.2f} kr.")
else:
    print(f"Du har et underskudd på {differens:.2f} kr.")
