"""W04_exercise03 - pack/unpack """
import subprocess

subprocess.call(["/usr/bin/clear"])  # Orkar inte ta reda på hur man skriver ut CTRL-L = clear screen: ) 
print("""
# Övning X-1
# Tilldela, på en enda kodrad, variablerna name, age, city värdena i listan data = ['Adnan', 27, # 'Stockholm'].
# Skriv sedan ut variablerna med hjälp av en f-sträng så att resultatet blir:
#   "Adnan är 27 år och bor i Stockholm"
# 
# #
# LÖSNINGSFÖRSLAG:
# data = ['Adnan', 27, 'Stockholm']
# name, age, city = data
""")
data = ['Adnan', 27, 'Stockholm']
name, age, city = data
print(f"{name} är {age} år och bor i {city}")


print("-" * 80)  # foo
input("Press return for next")
subprocess.call(["/usr/bin/clear"])

print("""
# Övning X-2
# Tilldela, på en enda kodrad, variablerna first och last det första respektive sista värdet i listan
#       some_numbers = [1, 2, 3, 4, 41]
# och skriv ut summan av dessa variabler. Resultatet ska bli 42.
# Skriv även ut de mittersta talen. Använd gärna en f-sträng!
#
# TIPS:
# 1. Du behöver använda *tre* variabler. Den tredje variabeln kan t.ex. heta 'middle'.
# 2. Den tredje variabeln behöver 'unpackas' m h a en asterisk ('*') framför variabelnamnet.
#
# LÖSNINGSFÖRSLAG:
# some_numbers = [1, 2, 3, 4, 41]
# first, *middle, last = some_numbers 
# print(first + last)
# print(f"De mittersta talen är: {middle}")
#
""")
some_numbers = [1, 2, 3, 4, 41]
first, *middle, last = some_numbers 
print(first + last)
print(f"De mittersta talen är: {middle}")


print("-" * 80)  # foo
input("Press return for next")
subprocess.call(["/usr/bin/clear"])
print("""
#
# *** KASTA ELLER SKRIV OM DENNA *** (NOTE to SELF!)
#
# ÖVNING Y.
# Anropa funktionen sum_numbers nedan med listan list_of_numbers som
# argument.
#
# TIPS:
# Listan behöver 'unpackas' för att kunna användas som argument till
# funktionen: sum_numbers(*list_of_numbers).
#
# def sum_first_three_numbers(numbers):
#   first, second, third, *the_rest = numbers
#   print(first + second + third)
#
# list_of_numbers = list(range(10))
#
# LÖSNINGSFÖRSLAG:
# def sum_numbers(*args):
#     sum = 0
#     for arg in args:
#         sum += arg
#     print(sum)
#
# list_of_numbers = list(range(10))
# sum_numbers(*list_of_numbers)
""")
def sum_numbers(*args):
    sum = 0
    for arg in args:
        sum += arg
    print(sum)

list_of_numbers = list(range(10))
sum_numbers(*list_of_numbers)

print("-" * 80)  # foo
input("Press return for next")
subprocess.call(["/usr/bin/clear"])


print("""
# ÖVNING Z
# Skriv en funktion som tar en lista av tal som argument och
# returnerar summan av alla tal i listan utom det första och sista. 
# 
# Funktionen kan, exempelvis, heta 'sum_all_but_first_and_last' (hitta på ett
# eget om du vill).
#
# Skriv sedan ut summan av de mittersta talen i listan 
# list_of_numbers = [9999, 1, 1, 1, 1, 9999].
#
# Resultaten ska bli 4.
#
# LÖSNINGSFÖRSLAG:
#
# def sum_all_but_first_and_last(numbers):
#   first, *middle, last = numbers
#   return sum(middle)
#
# list_of_numbers = [9999, 1, 1, 1, 1, 9999]
# print(sum_all_but_first_and_last(list_of_numbers))  # Skriver ut 
#
# 
""")
def sum_all_but_first_and_last(numbers):
    first, *middle, last = numbers
    return sum(middle)

list_of_numbers = [9999, 1, 1, 1, 1, 9999]
print(sum_all_but_first_and_last(list_of_numbers))  # Skriver ut talet 4. 

print("-" * 80)  # foo
input("Press return for next")
subprocess.call(["/usr/bin/clear"])

