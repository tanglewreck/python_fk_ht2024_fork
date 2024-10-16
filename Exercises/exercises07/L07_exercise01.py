#
# ÖVNING 1
#
#
# Komplettera koden nedan så att när användaren
# trycker CTRL-C (genererar ett KeyboardInterrupt-exception)
# så fångas detta och kör kod som ber användaren
# bekräfta att den vill avsluta programmet.
#
# Om användarens svar börjar på "j" (eller "y" om man
# föredrar engelska) ska programmet avslutas. 
#
#
# TIPS 1:
#   Du behöver lägga till en separat except-sats som
#   fångar KeyboardInterrupt:
#
#       try:
#           ...
#
#       except KeyboardInterrupt:
#           ...
#
#       except:
#           print("Fångade ett fel! Hurra!")
#
#
# TIPS 2:
#   input() går att använda direkt i en if-sats:
#
#       if input("Avsluta (j/N)? ") == "j":
#           ...
#
#   Alternativt, för att fånga input som börjar
#   på "j" eller "J":
#
#       if input("Avsluta (j/N)? ").lower().startswith("j"):
#           ...
#   
#
# TIPS 3: 
#   För att avsluta programmet kan quit(), raise SystemExit() 
#   eller sys.exit() användas.
#
#   NOT: sys.exit() kräver import av sys-modulen
#
#
# 
# Kod från exempel 3:
# while True:
#     try:
#         x = input("Skriv in ett värde som ska skrivas ut: ")
#         print(x)
#     except:
#         print("Fångade ett fel! Hurra!")

# Lösningsförslag:

while True:
    try:
        x = input("Skriv in ett värde som ska skrivas ut: ")
        print(x)
    except KeyboardInterrupt:
        print()
        print("Fångade ett KeyboardInterrupt-exception")
        if input("Avsluta (j/N)? ").lower().startswith("j"):
            print("Bye-bye")
            quit(0)
    except Exception:
        print("Fångade ett fel! Hurra!")



