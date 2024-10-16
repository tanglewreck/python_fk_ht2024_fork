#
# ÖVNING 3
#
# Skriv om nedanstående kod så att den 
# inte kontrollerar i förväg om den 
# angivna filen existerar utan i stället
# fångar felet (exception) som uppstår om
# filen inte existerar. 
#
# TIPS:
#   Fånga felet (exception) med try-except.
#   Vilken typ av exception behöver du fånga?
#
#   (Ledtråd: print(e.__class__.__name___) skriver ut namnet
#   på det exception som variabeln 'e' innehåller)
#   
#
#  import os
#  
#  foo_file = "foofile.txt"
#  if os.path.isfile(foo_file):
#      print(f"Filen {foo_file} existerar och innehåller nedanstående text")
#      with open(foo_file, 'r') as f:
#          print("\t" + f.read())
#  else:
#      print(f"Skapar filen {foo_file}")
#      with open(foo_file, 'w') as f:
#          f.write("Det här är innehållet i filen foo_file.txt")
#
#
# input("Press enter")
#
# LÖSNINGSFÖRSLAG
#
foo_file = "foofile.txt"

try:
    with open(foo_file, 'r', encoding="utf-8") as f:
        print(f"Filen {foo_file} existerar och innehåller nedanstående text:")
        print("\t" + f.read())
except FileNotFoundError as e:
    print(f"Skapar filen {foo_file}")
    with open(foo_file, 'w') as f:
        # f.write("Filen foo_file.txt innehåller den här texten")
        # f.write("Det här är innehållet i filen foo_file.txt")
        print("Det här är innehållet i filen foo_file.txt", file=f)
