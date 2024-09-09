# = = = = = = = = = = = = = = = = = = = = = = = = = = = = 
# 1. Skriv en funktion som tar ett heltal som argument
#    och returnerar True om talet är udda.
# = = = = = = = = = = = = = = = = = = = = = = = = = = = = 
#
# TIPS:
#       1.  Funktionen kan, förslagsvis, heta 'is_odd()'.
#
#       2.  Restoperatorn % returnerar 0 (noll) om talet är jämnt.
#
#           I Python räknas 0 (noll) som "falsish" och alla andra
#           tal som "truish".
#
#           Detta innebär att uttrycket
#
#               n % 2 
#       
#           (som returnerar 1 om n är udda) kan användas
#           'som det står' i jämförelser.
#
#           Exempel:
#           Följande kod kommer att skriva ut texten "3 är udda":
#
#               n = 3
#               if n % 2:
#                   print(n, "är udda")   # Alternativt: print(f"{n} är udda")
#               else:
#                   print(n, "är jämnt")  # Alternativt: print(f"{n} är jämnt")
#       
# LÖSNINGSFÖRSLAG 1:
#
#       def is_odd(n):  # Returnerar en bool (True el. False)
#           if n % 2 == 1:
#               return True
#           else:
#               return False
#
# LÖSNINGSFÖRSLAG 2 (kortare, mer koncist; returnerar 0 eller 1): 
#
#       def is_odd(n):
#           return n % 2
#
# LÖSNINGSFÖRSLAG 3 (med s.k. type hints):
#
#       def is_odd(n: int) -> bool:
#           return n % 2
#
# = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = 
# 2. Använd funktionen från övning 1. i en list comprehension för
#    skapa en lista av alla udda tal mellan 0 och 100
# = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = 
#
# Använd en list comprehension för att skapa en lista av alla udda tal
# mellan 0 och 100. Skriv sedan ut listan.
#
#
# LÖSNINGSFÖRSLAG:
#
#       odd_numbers = [k for k in range(101) if is_odd(k)]
#       print(odd_numbers)



# = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = 
# 3. Använd en list comprehension för att skapa en list som består 
#    av ... <work in progress>
# = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = 
#
# LÖSNINGSFÖRSLAG:
#
