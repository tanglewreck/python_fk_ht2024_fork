# I den här övningen ska du skapa en fil som innehåller ett (påhittat, om man
# vill) namn och en poängsumma (påhittad).
#
# Skriv ett program som gör följande:
#
# 1. Be användaren skriva in ett (påhittat) namn i konsolfönstret;
#    spara namnet i variabeln 'name',
#    t.ex. name = input("Hur var namnet? ")
#
# 2. Be användaren skriva in en poängsumma i konsolfönstret;
#    spara namnet i variabeln points
#
#
# 3. Skapa text-variabeln data = f"name: {name}, points: {points}"
#
# 3. Öppna filen 'person_points.txt' för skrivning. Om filen redan
#    finns ska den ersättas (skrivas över) 
#    Tips 1: Använd open() med argumentet mode='w'
#    Tips 2: Öppna filen inom en with-'klausul'
#
# 4. Skriv in i filen (person_points.txt) namnet och poängen.
#    Tips 1: Spa
#    Tips: Använd write()
#
# 5. När datat skrivits till filen och filen är stängd,
#    öppna filen för läsning
#    Tips 1: Använd with och open()
#    Tips 2: Använd argumentet 'r' till open()
#
# 6. Läs in innehållet i filen till variabeln data_read
#
# 7. Skriv ut filinnehållet på skärmen (konsolen)
#
FILE_NAME = "person_points.txt"

# LÖSNINGSFÖRSLAG:
name = input("Hur var namnet? ")
points = input("Hur var poängen? ")

# Skapa variabeln data
data = f"name: {name}, points: {points}"

# try – except optional
try:
    # Öppna filen för skrivning.
    # Genom att använda 'with' behöver vi inte tänka 
    # på att stänga filen när vi är klara.
    with open("person_points.txt", "w") as f:
        # Skriv
        f.write(data + "\n")
except OSError as e:
    print(str(e))
    raise SystemExit(1)

try:


print("Great success")
