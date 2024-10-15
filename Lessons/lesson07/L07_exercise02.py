# ÖVNING 2
#
# Vilka specifika exceptions behöver
# du fånga i nedanstående kod ()?
#
# NOTERA:
#   Koden kommer avslutas när 
#   det första felet inträffar.
#
#   Fixa (hantera) detta fel med hjälp
#   av try-except enligt TIPS 3 nedan
#   och kör sedan koden igen för att
#   generera nästa fel, och så vidare.
#
#   
# - - - - - - Här börjar koden - - - - - - - - - - - - -
#     
#     print(10 / 0)         # Första felet
#
#     print('10' / 0)       # Andra felet
#     
#     lista = []
#     print(lista[10])      # Tredje felet
#
#     import math
#     print(math.sqrt(-1))  # Fjärde felet
#
# - - - - - - Här slutar koden - - - - - - - - - - - - -
# 
# TIPS 1:
#   Läs mer om vilka exception-typer det finns på
#       https://docs.python.org/3/library/exceptions.html#concrete-exceptions
#
# TIPS 2: 
#   När du kör koden ovan kommer ett exception genereras
#   och skrivas ut på konsolen (tillsammans med en s.k.
#   traceback). Det är detta exception du behöver fånga.
#
#
# TIPS 3:
#   Använd gärna nedanstående kod
#   try:
#       print('10' / 0)
#   except <exception-typ> as e:
#       print("Fångade ett exception av typ: ", e.__class__.__name__)
# 
#
# LÖSNINGSFÖRSLAG
#
# print(10 / 0)
# print('10' / 0)
# lista = []
# print(lista[10])
# import math
# print(math.sqrt(-1))

try:
    print(10 / 0)
except ZeroDivisionError as e:
    print("Fångade ett exception av typ: ", e.__class__.__name__)

try:
    print('10' / 0)
except TypeError as e:
    print("Fångade ett exception av typ: ", e.__class__.__name__)

try:
    lista = []
    print(lista[10])
except IndexError as e:
    print("Fångade ett exception av typ: ", e.__class__.__name__)

try:
    import math
    print(math.sqrt(-1))
except ValueError as e:
    print("Fångade ett exception av typ: ", e.__class__.__name__)

