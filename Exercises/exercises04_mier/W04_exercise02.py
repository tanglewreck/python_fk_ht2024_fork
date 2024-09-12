"""W04_exercise02 - join()"""
import subprocess

subprocess.call(["/usr/bin/clear"])
print("""
#
# ÖVNINGAR
#
# Nedanstående övning kräver import av listan ascii_lowercase från modulen string:
#
#   from string import ascii_lowercase
#
#
# Övning X. 
# Skriv ut listan ascii_lowercase (se ovan), en bokstav per rad.
# Använd join() på strängen "\n". 
#
# NOT: Om du jobbar i ett python-skal ("shell" eller "console") behöver du
# använda print() för att listan ska skrivas ut ett tecken per rad, annars
# kommer du få strängen 'a\\nb\\nc\\nd\\ne\\nf\\ng\\nh\\ni\\nj\\nk\\nl\\nm\\nn\\no\\np\\nq\\nr\\ns\\nt\\nu\\nv\\nw\\nx\\ny\\nz'
# utskriven: print() behövs för att radbrytningstecknet "\\n" ska tolkas som en radbrytning.
#
# LÖSNINGSFÖRSLAG:
from string import ascii_lowercase
print("\n".join(ascii_lowercase))""")

from string import ascii_lowercase
print("\n".join(ascii_lowercase))



print("-" * 80)  # foo
input("Press return for next")
subprocess.call(["/usr/bin/clear"])

print("""
# Övning X - extra
# Skriv ut listan ascii_lowercase i omvänd ordning, ett tecken per rad
#
# LÖSNINGSFÖRSLAG:
from string import ascii_lowercase
print("\n".join(sorted(ascii_lowercase, reverse=True)))
""")
from string import ascii_lowercase
print("\n".join(sorted(ascii_lowercase, reverse=True)))

print("-" * 80)  # foo
input("Press return for next")
subprocess.call(["/usr/bin/clear"])

print("""
# ÖVNING Y.
# 1. Skapa en lista bestående av strängarna '0', '1', ... , '9'.
#    Använd en list comprehension tillsammans med str()-funktionen.
#
# LÖSNINGSFÖRSLAG:
num_string = [str(k) for k in range(10)] 
print(num_string)  # --> ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9'] """)

num_string = [str(k) for k in range(10)] 
print(num_string)
