# ÖVNING X_1
#
# Skriv ett program som skapar filen 
# 'data_1.txt' och skriver siffrorna
# 1 till 42, en siffra per rad.
#
# Kom ihåg att 'write()' och 'writelines()'
# enbart kan skriva strängar när en fil
# öppnats med flaggan 'w'.
#
# Om du vill kan du använda nedanstående
# kod för att skapa en list-variabel bestående
# av strängar:
#
#   numbers = [str(k) + "\n" for k in range(42)] 
# LÖSNINGSFÖRSLAG

numbers = [str(k) + "\n" for k in range(43)] 
with open("numbers_42.txt", 'w') as f:
    for k in numbers:
        f.write(k)


#
# ÖVNING X_2
#
# Skriv ett program som öppnar och skriver ut
# innehållet i filen du skapade i förra övningen.
#

# Lösningsförslag 1
print("Lösning 1")
file_name = "numbers_42.txt"
with open(file_name, 'r', encoding='utf-8') as f:
    contents = f.read()
    print(contents)
    # print(f.read())


input("Press enter for next ")
# 
# Lösningsförslag 2 (avancerat)
print("Lösning 2")
file_name = "numbers_42.txt"
with open(file_name) as f:
    for row in f:
        print(f.readline())


input("Press enter for next ")
print("Lösning 3")
# 
# Lösningsförslag 2 (avancerat)
import os
import sys
file_name = "numbers_42.txt"
if os.path.exists(file_name):
    with open(file_name) as f:
        # print(f.read())
        k = 0
        while row := f.readline():
            print(f"{k}: {row}")
            k += 1

        #for row in f:
        #    sys.stdout.write("Row: " + row)


