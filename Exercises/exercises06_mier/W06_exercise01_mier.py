# Övning 1.
#   Skriv ett program som ber användaren skriva in text (valfri längd) och 
#   som sedan skriver den inmatade texten till en fil (t.ex. fil_1.txt).
#
#   Om ingen text matas in ska filen inte skapas.
#
#   TIPS 1: Kom ihåg att använda 'with open(...)' så att filen stängs automatiskt.
#   TIPS 2: För att kontrollera att text skrivits in, använd 'if <my_text>:' (där
#   <my_text> står för namnet på variabeln du använde i input()-satsens.
#
out_file = 'fil_1.txt'
out_text = input(f"Skriv in texten som ska sparas till filen {out_file}: ")
if out_text:
    with open(out_file, 'w') as f:
        f.write(out_text)
    print(f"Texten \"{out_text}\" skrevs till filen \"{out_file}\"")
else:
    print(f"Ingen text skrevs in. Filen {out_file} lämnades orörd")

input("Press return to continue ")

# 
#   EXTRA (frivilligt):
#
#   Lägg till en kontroll om filen redan finns och be i så fall användaren
#   bekräfta (genom att skriva in "ja") att filen får skrivas över (ersättas
#   med nytt innehåll). Om användaren svarar 'nej', avsluta programmet.
#
#   TIPS 1:
#       Använd funktionen os.path.exists() för att kontrollera om filen
#       existerar (import os).
#       
#   TIPS 2:
#       Ett alternativ till 'quit()' för att avsluta programmet är: 
#           raise SystemExit(1)
#
#       Då kommer programmet avslutas och returnera koden 1, vilket
#       indikerar att körningen avslutades p.g.a. att något 'fel' 
#       inträffade (när programmet körts utan att något fel uppstått 
#       returneras normalt sett koden 0: raise SystemExit(0)).
#
#   TIPS 3:
#       För att kontrollera att någon inmatning gjorts kan du använda följande
#       kod:
#
#           out_file = 'fil_1.txt'
#           # Kolla om filen redan finns och be användaren skriva in 
#           # "ja" eller "nej". Om användaren skriver in "nej" eller inte
#           # skriver in någon text alls avslutas programmet.
#           if os.path.exists(out_file):
#               confirm = input(f"Filen {out_file} finns redan. Vill du skriva över (ja/NEJ)? ")
#               if confirm.lower() == "nej" or confirm == "":
#                   raise SystemExit(1)  # Avsluta programmet
#           
#   LÖSNINGSFÖRSLAG:

import os

# Fil som ska skrivas
out_file = 'fil_1.txt'

# Kolla om filen redan finns och be användaren skriva in 
# "ja" eller "nej". Om användaren skriver in "nej" eller inte
# skriver in någon text alls avslutas programmet.
if os.path.exists(out_file):
    confirm = input(f"Filen {out_file} finns redan. "
                    "Bekräfta att filen skrivs över [ja/NEJ]: ")
    if confirm.lower().startswith("n") or confirm == "":
        print(f"Okej. Filen {out_file} lämnas orörd")
        raise SystemExit(10)
        # quit()

    out_text = input(f"Skriv in texten som ska sparas till filen {out_file}: ")
    if out_text:
        with open(out_file, 'w') as f:
            f.write(out_text)
        print(f"Texten \"{out_text}\" skrevs till filen \"{out_file}\"")
    else:
        print(f"Ingen text skrevs in. Filen {out_file} lämnades orörd")
        raise SystemExit(0)


input("Press return to continue ")

#
#
# Övning 2.
#   Skriv ett program som kopierar innehållet i filen i uppgiften ovan till en annan, ny, fil.
#
#   Om du vill kan du, på samma sätt som i uppgiften ovan, lägga till kontroller som för om
#   filerna existerar och om utdata-filen ska skrivas över (om den redan existerar).
#
#   TIPS 1: 
#   Läs in innehållet i filen med hjälp av read() och skriv 
#   sedan med hjälp av write(). Det behövs två open()-satser för detta.
#
# LÖSNINGSFÖRSLAG (bare-bones):
import os

in_file = "fil_1.txt"
out_file = "fil_2.txt"

if not os.path.exists(in_file):
    print(f"Indata-filen ({in_file}) saknas")
    raise SystemExit(1)

with open(in_file, 'r') as f:
    in_data = f.read()

if os.path.exists(out_file):
    confirm = input(f"Utdata-filen ({out_file}) finns redan. Vill du skriva över den (ja/NEJ)? ")
    if not confirm or confirm.lower().startswith("n"):
        print("Okej, utdata-filen kommer inte skrivas över. "
              "Programmet avslutas")
        raise SystemExit(0)
    else:
        print("Okej, utdata-filen skrivs över")

with open(out_file, 'w') as f:
    f.write(in_data)
