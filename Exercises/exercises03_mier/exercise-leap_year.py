# = = = = = = = = = 
# ÖVNING: SKOTTÅR
# = = = = = = = = = 
#
# Skriv ett program som frågar efter ett årtal och som därefter
#    skriver ut huruvida årtalet räknas som ett skottår eller ej.
#
#   TIPS: 
#       1. Ett år är ett skottår om det är: 
#           i.  jämnt delbart med 4 OCH INTE jämnt delbart med 100, ELLER
#           ii. delbart med 400
#
#       2. Python-operatorn '%' kan användas för att avgöra om ett tal är jämnt
#          delbart med ett annat tal:
#               (2000 % 4 == 0)       -> True (2000 är jämnt delbart med 4)
#               (2000 % 400 == 0)     -> True (2000 är jämnt delbart med 400)
#               (2100 % 100 == 0)     -> True (2100 är jämnt delbart med 100)
#               (2001 % 4 == 0)       -> False (2001 är inte jämnt delbart med 4)
#
#       3. Använd lämpligt utplacerade parenteser runt jämförelsesatserna 
#
#   EXTRA:
#       Lägg kod som hanterar fallet att något annat än ett årtal (heltal) skrivs in,
#       t.ex. en while-loop med try-except:
#       
#       while True:
#           try:
#               year = int(input(...))
#               break
#           except ValueError:
#               print("Du har inte skrivit in ett årtal (ett heltal)")
#
#   = = = = = = = = = 
#   LÖSNINGSFÖRSLAG 1
#   = = = = = = = = = 
#   while True:
#       try:
#           year = int(input("Skriv in ett årtal "))
#           break
#       except ValueError:
#           print("Du har inte skrivit in ett årtal (ett heltal)")
#   if ((year % 4 == 0) and not (year % 100 == 0)) or (year % 400):
#       print(year, "är ett skottår")
#   else:
#       print(year, "är inte ett skottår")
#
#   = = = = = = = = = 
#   LÖSNINGSFÖRSLAG 2
#   = = = = = = = = = 
#   def leap_year(year: int) -> bool:
#       return ((year % 4 == 0) and not (year % 100 == 0)) or (year % 400)
#
#   while True:
#       try:
#           year = int(input("Skriv in ett årtal: ")
#           if leap_year(year):
#               print(year, "är ett skottår")
#           else:
#               print(year, "är inte ett skottår")
#           break
#       except ValueError:
#           print("Du har inte skrivit in ett årtal")
#
#   KOMMENTAR:
#       I stället för att göra alla jämförelser i en enda sats kan man göra
#       jämförelserna en i taget, t.ex.:
#           if (year % 4 == 0):
#               if (year % 100 == 0):
#                   if (year % 400 == 0):
#                       print(year, "är ett skottår")
#                   else
#                       print(year, "är inte ett skottår")
#               else:
#                   print(year, "är ett skottår")
#           else:
#               print(year, "är inte ett skottår")
#               
#                   
