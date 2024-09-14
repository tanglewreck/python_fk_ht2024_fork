"""W04_exercise01 - f-strings"""
#
# ÖVNINGAR
#
# X. Använd en f-sträng för att skriva ut talet 1/3 med tre decimaler:
# LÖSNINGSFÖRSLAG
f = f"{1 / 3:.3f}" 

print("–" * len(f))
print(f"{1 / 3:.3f}") 
print("–" * len(f))
print()

# X. Använd en f-sträng för att skriva ut talet 1/3 tio tecken brett och med tre decimaler.
#    Skrivs talet ut vänsterställt eller högerställt?
#
# LÖSNINGSFÖRSLAG
print("–" * 10)
print(f"{1 / 3:10.3f}: en tredjedel med tre decimaler, högerställt, tio tecken") 
print(f"{1 / 3:>10.3f}: en tredjedel med tre decimaler, högerställt, tio tecken") 
print("–" * 10)

# X. Använd en f-sträng för att skriva ut 1/3 med tre decimaler, tio tecken brett, och högerställt:
# LÖSNINGSFÖRSLAG
print(f"{1 / 3:<10.3f}: en tredjedel med tre decimaler, vänsterställt, tio tecken") 
print("–" * 10)

# X. Använd en f-sträng för att skriva ut 1/3 med tre decimaler, tio tecken brett, och centrerat:
# LÖSNINGSFÖRSLAG
print(f"{1 / 3:^10.3f}: en tredjedel med tre decimaler, centrerat, tio tecken") 
print("–" * 10)
raise SystemExit(0)

# 1. Tilldela strängvariabeln 'name' något värde (t.ex. 'nisse hult') och använd sedan 
#    en f-sträng för att skriva ut variabeln med stora bokstäver
#
#    TIPS:
#    Sträng-metoden upper() omvandlar en sträng till versaler:
#       name = "freddie"
#       print(name.upper())
#
# >>>>> (Kodexemplet ovan kan kanske skrotas eftersom det ger hela svaret på övningen?)  <<<<<
#
#   LÖSNINGSFÖRSLAG:
namn = "nisse hult"
print(f"{namn.upper()}")
print()



# 2. Skriv ett program som först frågar efter ett namn, därefter frågar efter hur
# gammal personen är, och till sist skriver ut texten, t.ex. 'Nisse är 42 år gammal'.
# Använd en f-sträng i print-satsen!
# 
# I den andra frågan, den om ålder, kan man, om man vill, använda en f-sträng med
# namnet som skrivits in i den första frågan, så att frågan blir, t.ex.,
# "Hur gammal är Nisse?" (där "Nisse" är namnet som skrivits in i första frågan). 
#
#   LÖSNINGSFÖRSLAG: 
name = input("Skriv in ett namn på en person: ")
age = input(f"Skriv in hur gammal {name} är: ")
print(f"{name} är {age} år gammal")
print()

# 3. Lägg till kod till övning 2 som skriver ut om personen är ett barn, vuxen
#    eller pensionär.
#
#    Pensionärer är naturligtvis vuxna, men i den här övningen räknas 'vuxen' och
#    'pensionär' som två olika kategorier.
#
#    Barn är den som är högst 17 år gammal, pensionär den som är 67 år eller
#    äldre, vuxen är den som varken är barn eller pensionär. 
#
#    TIPS 1
#    Använd gärna f-strängar med namnet på personen så att utskriften blir,
#    t.ex., "Nisse, 68, är pensionär", "Lisa, 5, är ett barn", "Adnan, 37, är
#    vuxen".
#
#   TIPS 2:
#   Sträng-metoden capitalize() kan användas för att namnet ska skrivas 
#   ut versalgement (första bokstaven versalt, resten gement):  
#       name = 'adnan'
#       age = 33
#       print(name.capitalize())  --> "Adnan"
#       print(f"{name.capitalize()} är {age} år gammal")  --> "Adnan är 33 år gammal":
#
#   TIPS 3:
#   Strängmetoden title() omvandlar en sträng så att första bokstaven i
#   varje ord blir versal:
#       print("josefin maria svensson".title())  --> "Josefin Maria Svensson"

#   LÖSNINGSFÖRSLAG:
name = input("Skriv in ett namn på en person: ")
age = int(input(f"Skriv in hur gammal {name.title()} är: "))

print()
print(f"{name.capitalize()} är {age} år gammal")

if age <= 17:
    print(f"{name.capitalize()} är ett barn")
elif age > 17 and age < 67:
    print(f"{name.capitalize()} är vuxen")
else:
    print(f"{name.capitalize()} är pensionär")

