"""W04_exercise01 - f-strings"""

def underline(text: str, underline_char="-")  -> None:
    """Underline strings"""
    print(f"{underline_char * len(text)}")


def print_f_string_example(example_n: int, f_string: str) -> None:
    """
    Print and run (evaluate) an example f-string
    Arguments: 
        example_n:  Example number 
        f_string:   The f-string to print and evaluate
    """

    # Pretty-print the f-string
    print()
    underline("f-string = " + f_string, underline_char="=")
    print(f"EXEMPEL {example_n}")
    print(f"f-string = {f_string}:")
    underline("f-string = " + f_string, underline_char="=")

    # Run (evaluate) the f-string
    print(f"{eval(f_string)}")  #  f"{[k for k in range(1, 11)]}")


#
# FÖRKLARINGSTEXT f-STRÄNGAR: 
# Inom måsvingeparenterserna ({ }) kan godtycklig kod användas, så 
# länge som # returnerar värden placeras. 
#
# Exempel 1
f_string = "f\"{10 + 10}\""
print_f_string_example(example_n=1, f_string=f_string)

# Exempel 2
f_string = "f\"{[k for k in range(1,11)]}\""
print_f_string_example(example_n=2, f_string=f_string)

# Exempel 3
a_dict = {"namn": "Josefin", "age": 27}
f_string = "f\"{a_dict['namn']}, {a_dict['age']} år\""
print_f_string_example(example_n=3, f_string=f_string)

# Exempel 4
f_string = "f\"{dict(name='Josefin', age=27)['name']} är {dict(name='Josefin', age=27)['age']} år gammal\""
print_f_string_example(example_n=4, f_string=f_string)

#
# ÖVNINGAR
#
# X. Använd en f-sträng för att skriva ut texten "
# 1. Tilldela strängvariabeln 'name' något värde (t.ex. 'nisse hult') och använd sedan 
#    en f-sträng för att skriva ut variabeln med stora bokstäver
#
#    TIPS: Sträng-metoden upper() omvandlar en sträng till versaler.
#          Kodexemplet nedan skriver ut texten "FREDDIE":
#               name = "freddie"
#               print(name.upper())
# >>>>> (Kodexemplet ovan kan kanske skrotas eftersom det ger hela svaret på övningen)  <<<<<
#
#   LÖSNINGSFÖRSLAG:
namn = "nisse hult"
print(f"{namn.upper()}")



# 2. Skriv ett program som först frågar efter ett namn, därefter frågar efter hur
# gammal personen är, och till sist skriver ut texten, t.ex. 'Nisse är 42 år gammal'.
# Använd en f-sträng i print-satsen!
# 
# I den andra frågan, den om ålder, kan man, om man vill, använda en f-sträng med namnet som skrivits in i den första frågan, 
# t.ex. "Hur gammal är Nisse?" (där "Nisse" är namnet som skrivits in i fråga
# ett).
#
#   LÖSNING (förslag):
#   name = input("Skriv in ett namn på en person: ")
#   age = input(f"Skriv in hur gammal {name} är: ")
#   print(f"{name} är {age} år gammal")
#
#
# 3. Lägg till kod till övning 2 som skriver ut om personen är ett barn, vuxen
#    eller pensionär (pensionärer är naturligtvis vuxna, men i den här övningen är 
#    'vuxen' och 'pensionär' två olika kategorier). Barn är den som är högst 17
#    år gammal, pensionär den som är 67 år eller äldre, vuxen är den som varken
#    är barn eller pensionär. 
#
#    Använd gärna f-strängar med namnet på personen så att utskriften blir,
#    t.ex., "Nisse, 68, är pensionär", "Lisa, 5, är ett barn", "Adnan, 37, är
#    vuxen".
#
#   TIPS: sträng-metoden capitalize() kan användas för att första bokstaven i
#   strängen skrivs ut versalt och övriga bokstäver gement. Exemplet nedan
#   kommer resultera i att "Adnan är 33 år gammal" skrivs ut: 
name = 'adNAN'
age = 33
print(f"{name.capitalize()} är {age} år gammal") 
#
#   LÖSNINGSFÖRSLAG:
name = input("Skriv in ett namn på en person: ")
age = int(input(f"Skriv in hur gammal {name.capitalize()} är: "))

print()
print(f"{name.capitalize()} är {age} år gammal")

if age <= 17:
    print(f"{name.capitalize()} är ett barn")
elif age > 17 and age < 67:
    print(f"{name.capitalize()} är vuxen")
else:
    print(f"{name.capitalize()} är pensionär")

