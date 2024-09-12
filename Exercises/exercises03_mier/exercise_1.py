# ÖVNINGAR – – utkast
#
# ------------------------------------------------------------------
# 1. Vad skrivs ut när följande kod körs?
#
#   x, y = 42, 0
#   z = x or y
#   w = x and y
#   print(z)
#   print(w)
#   
#   {Eller:
#       x, y = 42, 0
#       print(x or y)
#       print(x and y) }
#
# ------------------------------------------------------------------
#
# 2.1 Vad skrivs ut när följande kod körs?
#
#   x, y, z = 42, 21, 7
#   
#   if (x > y) and (y > z):
#       print(x, "är större än", y, "och", y, "är större än", z)
#   else:
#       print(x, "är inte större än", y, "eller", y, "är inte större än", z)
#
# 2.2 Blir det någon skillnad om parenteserna i if-satsen tas bort?
#
# ------------------------------------------------------------------
#
# 3 Vad skrivs ut när nedanstående kod körs?
#
#   a = 9
#   if a > 5 and a <= 10:
#       print("a är större än 5 och mindre än eller lika med 10")
#   else:
#       print("a är mindre än eller lika med 4 eller större än 10")
# 
# ------------------------------------------------------------------
#
# 4.1 Vad skrivs ut när nedanstående kod körs?
#   p = True
#   q = False
#   r = False
#   print( p or q and r )  #  Hint: Satsen är ekvivalent med: print(p or (q and r))
#
# 4.2 Vad skrivs ut när print-satsen ändras till:
#   print( (p or q) and r )
#
#
# I Python binder 'and' hårdare än 'or', vilket får konsekvenser i uttryck där
# båda operatorerna används.
#
# I den första print-satsen saknas parenteser, vilket betyder (eftersom 'and'
# binder hårdare än 'or') att den är ekvivalent med:
#   print( p or (q and r) )  --> True (eftersom p == True)
#
# I den andra print-satsen används parenteser:
#   print( (p or q) and r )  --> False (eftersom r == False)
#
# Med andra ord: parenteser ändrar prioriteringen av de logiska operatorerna.
#
#
# ------------------------------------------------------------------
#
# 5. Skriv ett program som ber användaren skriva in ett heltal och som därefter
#    skriver ut om talet är jämnt delbart med 2 eller med 3, eller med både 2
#    och 3.
#
#   LÖSNINGSFÖRSLAG (typ)
#
#    def div_by_2_or_3_or_both(n: int):
#        s = str(n) + " är varken delbart med 2 eller 3"
#        if n % 2 == 0:
#            s = str(n) + " är jämnt delbart med 2"
#        if n % 3 == 0:
#            s = str(n) + " är jämnt delbart med 3"
#        if (n % 2 == 0) and (n % 3 == 0):
#            s = str(n) + " är jämnt delbart med både 2 och 3"
#        print(s)
#        print()
#    
#    n = 999  # Just some random number 
#    while n != 0:
#        while True:
#            try:
#                n = int(input("Skriv in ett heltal (0 för att avsluta programmet): "))
#                div_by_2_or_3_or_both(n)
#                break
#            except ValueError:
#                print("Du har inte skrivit in ett heltal")
