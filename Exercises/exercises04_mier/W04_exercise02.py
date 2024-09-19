"""W04_exercise02 - join()"""
import subprocess

subprocess.call(["/usr/bin/clear"])  # Orkar inte ta reda på hur man skriver ut CTRL-L = clear screen: ) 
print("""
#
# ÖVNING X
#
# Denna övning kräver import av listan ascii_lowercase från modulen string:
#
#   from string import ascii_lowercase
#
# Utforska gärna denna modul, t.ex. genom att skriva  'dir(string)' i en
# pythonkonsol. Modulen innehåller flera använda strängvariabler. Pröva gärna
# att skriva ut några av dem, t.ex. genom att skriva 'print(string.digits)'
# i en konsol.
#
# Om man inte vill använda string-modulen kan man använda denna strängvariabel:
#
#   ascii_lowercase = 'abcdefghijklmnopqrstuvwxyz'
# 
#
# Övning X: 
# Skriv ut strängvariabeln ascii_lowercase (se ovan), en bokstav per rad.
# TIPS: Använd strängen "\n" (radbrytningstecken) och strängmetoden join().
#
# TIPS: Om du jobbar i ett python-skal (t.ex. i IDLE) behöver du använda funktionen
# print(), annars kommer strängen
#   'a\\nb\\nc\\nd\\ne\\nf\\ng\\nh\\ni\\nj\\nk\\nl\\nm\\nn\\no\\np\\nq\\nr\\ns\\nt\\nu\\nv\\nw\\nx\\ny\\nz'
# att skrivas ut: print()-satsen behövs för att radbrytningstecknet "\n" ska tolkas som en radbrytning.
#
# LÖSNINGSFÖRSLAG 1:

from string import ascii_lowercase
print("\\n".join(ascii_lowercase))

# LÖSNINGSFÖRSLAG 2:

ascii_lowercase = 'abcdefghijklmnopqrstuvwxyz'
print("\\n".join(ascii_lowercase))

# LÖSNINGSFÖRSLAG 3 (utan join()):
for _ in list(string.ascii_lowercase):
    print(_)

""")

from string import ascii_lowercase
print("\n".join(ascii_lowercase))



print("-" * 80)  # foo
input("Press return for next")
subprocess.call(["/usr/bin/clear"])

print("""
# Övning X - extra
# Skriv ut strängen ascii_lowercase i omvänd ordning, ett tecken per rad
#
# TIPS: Använd funktionen sorted() på strängvariabeln tillsammans med
# "\\n" och join(), som ovan.
#
# LÖSNINGSFÖRSLAG:
from string import ascii_lowercase
print("\\n".join(sorted(ascii_lowercase, reverse=True)))

""")
from string import ascii_lowercase
print("\n".join(sorted(ascii_lowercase, reverse=True)))



print("-" * 80)  # foo
input("Press return for next")
subprocess.call(["/usr/bin/clear"])



print("""
# ÖVNING Y.
# 1. Skapa en lista bestående av strängarna '0', '1', ... , '9'. 
#    Skriv sedan ut listan, en sträng per rad.
# 
# TIPS 1: Ett enkelt sätt att lösa uppgiften är att använda list()
#         på strängen '0123456789' för att skapa en lista och sedan
#         använda en for-loop för att skriva ut ett tecken per rad.
#
# TIPS 2: Ett lite mer avancerat (och roligare! :) sätt att göra samma
#         sak på är att använda en list comprehension tillsammans med
#         str()-funktionen för att skapa listan och sedan använda 
#         "\\n".join(), som ovan.
# 
# TIPS 3: Att importera strängen digits från string-modulen är kanske 
#         lite overkill, men samtidigt kanske också lite roligare/intressantare
#         eftersom man får öva sig på att importera objekt från moduler.
#         Det ska vara roligt att programmera!
#         😃

# LÖSNINGSFÖRSLAG 1:
num_string = [str(k) for k in range(10)] 
print("\\n".join(num_string))


# LÖSNINGSFÖRSLAG 2 (allt på en enda kodrad):
print("\\n".join([str(k) for k in range(10)]))


# LÖSNINGSFÖRSLAG 3 (utan comprehension):
import string
print("\\n".join(list(string.digits)))


# LÖSNINGSFÖRSLAG 4 (med en for-loop):
num_list = list('0123456789')
for _ in num_list:
    print(_)

""")

# 1
num_string = [str(k) for k in range(10)] 
print("\n".join(num_string))
print()

# 2
print("\n".join([str(k) for k in range(10)]))
print()

# 3
import string
print("\n".join(list(string.digits)))


print("-" * 80)  # foo
input("Press return for next")
subprocess.call(["/usr/bin/clear"])


print("""
# ÖVNING W
# Skapa en sträng bestående av alla gemena (små) bokstäver med ett kommatecken
# infogat mellan varje par av bokstäver. Skriv sedan ut strängen.
# 
# TIPS 1: Om du vill slippa skriva in alla bokstäver kan du, som i övningen ovan, 
# importera variabeln ascii_lowercase från modulen string:
#   from string import ascii_lowercase
#
# LÖSNINGSFÖRSLAG:
from string import ascii_lowercase
comma_string = ", ".join(ascii_lowercase)
print(comma_string)

""")
from string import ascii_lowercase
comma_string = ", ".join(ascii_lowercase)
print(comma_string)


print("-" * 80)  # foo
input("Press return for next")
subprocess.call(["/usr/bin/clear"])

print("""
# ÖVNING Z
#
# Python tillåter inte att man ändrar direkt *i* en strängvariabel, så om
# man behöver uppdatera en textsträng måste man komma runt detta.
#
# Det finns flera sätt att göra detta på, varav det kanske enklase och 
# effektivaste sättet är att använda strängmetoden replace() för att skapa
# en *ny* sträng som man sedan tilldelar sin variabel:
#
#   string_with_no_underscores = string_with_underscores.replace("_", " ")
#
# Ett annat sätt, som vi för övningen skull ska använda här, är att konvertera
# strängen till en lista och sedan gå igenom listan element för element och
# ändra det som ska ändras på. När man är klar med ändringarna använder man
# join() för att konvertera tillbaka till en sträng.
#
#
# Använd den senare metoden för att byta ut alla "_"-tecken mot
# mellanslag (" ") i nedanstående sträng:
#
#       string_with_underscores = "Den_här_strängen_innehåller_underscores"
#
# 
# TIPS 1: Börja med att göra om strängen till en lista med hjälp av list().
#         Använd sedan en for-loop för att gå igenom listan och ändra där det behövs.
#         När for-loopen är klar, konvertera till en sträng med hjälp av join().
#
# TIPS 2: Du kommer att behöva en index-variabel för att hålla ordning på var
#         i listan du befinner dig. Ett sätt att gör det är att skapa en heltalsvariabel
#         utanför for-loopen och uppdatera denna medan loopen körs, t.ex:
#
#               k = 0
#               my_list = list("En_sträng_med_underscore")
#               for c in my_list:
#                   if c == "_":
#                       my_list[k] = " "
#                   k += 1
#
#         Ett annat sätt är att använda enumerate(), som för varje varv i
#         loopen returnerar en tupel bestående av ett heltalsindex (som
#         automatiskt räknas upp) och ett element i listan, t.ex.:
#
#           my_list = list("En_sträng_med_underscore")
#           for k, c in enumerate(num_list):
#               if c == "_":
#                   my_list[k] = " "
#
# TIPS 3: Ett sätt att slippa index-variablen är att använda en list-comprehension:
    [c if c != "_" else " " for c in list(string_with_underscores)]
  Lägg till join() till ovanstående så är du klar! : ) 

#
# LÖSNINGSFÖRSLAG 1:
#
string_with_underscores = "Det_här_är_en_sträng_med_en_massa_understreck_som_behöver_göras_om_till_mellanslag"
string_list = list(string_with_underscores)
for k, c in enumerate(string_list):
    if c == "_":
        string_list[k] = " "
string_with_underscores = "".join(string_list)
print(string_with_underscores)

# LÖSNINGSFÖRSLAG 2:
string_with_underscores = "Det_här_är_en_sträng_med_en_massa_understreck_som_behöver_göras_om_till_mellanslag"
string_list = list(string_with_underscores)

tmp_list = [c if c != "_" else " " for c in list(string_with_underscores)]
print("".join(tmp_list))

# Alternativt (men lite grötigare): 
print("".join([c if c != "_" else " " for c in list(string_with_underscores)]))

""")

# LÖSNINGSFÖRSLAG 1
string_with_underscores = "Det_här_är_en_sträng_med_en_massa_understreck_som_behöver_göras_om_till_mellanslag"
string_list = list(string_with_underscores)
for k, c in enumerate(string_list):
    if c == "_":
        string_list[k] = " "
string_with_underscores = "".join(string_list)
print(string_with_underscores)

# LÖSNINGSFÖRSLAG 2
tmp_list = [c if c != "_" else " " for c in list(string_with_underscores)]
print("".join(tmp_list))

# Alternativt (men lite grötigare): 
print("".join([c if c != "_" else " " for c in list(string_with_underscores)]))
