# coding: utf-8
# 
#
#  ÖVNING XYZ
#
#  Skriv ett program som skriver ut nedanstående lista som
#  en snyggt formaterad tabell.
#
#    data = [
#        ["2024-09-16", 100, 42.99],
#        ["2024-09-15", 42, 49.99],
#        ["2024-09-14", 37, 51.99],
#        ["2024-09-13", 200, 24.42],
#        ["2024-09-12", 100, 42.99],
#        ["2024-09-11", 100, 42.99],
#        ["2024-09-10", 135, 41.41],
#        ["2024-09-09", 90, 44.44],
#        ["2024-09-08", 10, 54.99],
#    ]
#
# TIPS 1: Data-listan består av en lista av listor vilket gör det möjligt
#         att iterera över listan med hjälp av en for-loop:
#
#         for row in data:
#           print(row)
#               
#         Koden ovan skriver ut följande rader:
#
#         ['2024-09-16', 100, 42.99]
#         ['2024-09-15', 42, 49.99]
#         ['2024-09-14', 37, 51.99]
#         ['2024-09-13', 200, 24.42]
#         ['2024-09-12', 100, 42.99]
#         ['2024-09-11', 100, 42.99]
#         ['2024-09-10', 135, 41.41]
#         ['2024-09-09', 90, 44.44]
#         ['2024-09-08', 10, 54.99]
#
#         Varje rad består alltså av en lista med tre element.
#
#
# TIPS 2: En rad i tabellen kan formateras t.ex. så här:
#         
#           |2024-09-16     |    100.00|         42.99|
#
#         Första kolumnen är ett datum som vi skriver ut 
#         som en vänsterställd sträng. Formatkoden för en 
#         sträng är 's'. Om vi vill specificera att 
#         strängen ska skrivas ut med tio teckens bredd
#         blir formatkoden '10s'.
#l
#
#         Kolumn två och tre är tal som vi skriver ut 
#         högerställt med två decimaler på tio teckens bredd.
#         Formatkoden blir: '>10.2f'.
#
#
# TIPS 3: Om du vill kan du använda koden nedan:
#
#               for row in data:
#                   print(f"|{row[0]:10s}\t|{row[1]:>10.2f}|{row[2]:>10.2f})")
#
#
#
# LÖSNINGSFÖRSLAG 1
data = [
    ["2024-09-16", 100, 42.99],
    ["2024-09-15", 42, 49.99],
    ["2024-09-14", 37, 51.99],
    ["2024-09-13", 200, 24.42],
    ["2024-09-12", 100, 42.99],
    ["2024-09-11", 100, 42.99],
    ["2024-09-10", 135, 41.41],
    ["2024-09-09", 90, 44.44],
    ["2024-09-08", 10, 54.99],
]

for row in data:
    print(f"|{row[0]:10s}\t|{row[1]:>10.2f}|{row[2]:>10.2f}|")

print()
input("Tryck <enter> för lösningsförslag 2")
print()

# LÖSNINGSFÖRSLAG 2 (med tabellhuvud):
# 
print(" " + "-" * 38)
print(" Tabell 1: Försäljningssiffror")
print(" " + "-" * 38)
for row in data:
    print(f"|{row[0]:10s}\t|{row[1]:>10.2f}|{row[2]:>10.2f}|")
print(" " + "-" * 38)



print()
input("Tryck <enter> för lösningsförslag 3")
print()

### LÖSNINGSFÖRSLAG 3 (en smula överambitiöst kanske :) 

HEADER_FORMAT = ["<10s", ">10s", ">10s"]
ROW_FORMAT = ["<10s", ">10.2f"]

def table_line(line_char: str, n: int, newline: bool = True) -> str:
    """Return a table row break string"""
    line_str = " " + line_char * n
    if newline:
        line_str += "\n"
    return line_str


def table_header(*args, format=HEADER_FORMAT):
# def table_header(*args, format=["<10s", ">10s", ">10s"]):
    """ row(): Pretty print a table header."""
    table_width = len(args) * (10 + 1)

    header_top = table_line("-", table_width) 
    header_string = f" |{args[0]:{format[0]}}|{args[1]:{format[1]}}|{args[2]:{format[2]}}|\n"
    header_bottom = table_line("-", table_width, newline=False)

    return header_top + header_string + header_bottom


def table_row(*args, format=ROW_FORMAT):
# def table_row(*args, format=["<10s", ">10.2f"]):
    """ Pretty print a table row.
    The function returns a formatted row as a string.
    When printed, a row looks like this:
    |<date string>  | <number of items>| <price per item>|
    |2024-09-16     |    100.00|         42.99|

    """

    # First column (date) has a special format
    row_string = f" |{args[0]:{format[0]}}|"

    for arg in args[1:]:
        row_string += f"{arg:{format[1]}}|"

    return row_string



if __name__ == "__main__":

    data = [
        ["2024-09-16", 100, 42.99],
        ["2024-09-15", 42, 49.99],
        ["2024-09-14", 37, 51.99],
        ["2024-09-13", 200, 24.42],
        ["2024-09-12", 100, 42.99],
        ["2024-09-11", 100, 42.99],
        ["2024-09-10", 135, 41.41],
        ["2024-09-09", 90, 44.44],
        ["2024-09-08", 10, 54.99],
    ]

    table_head = ["Date", "No items", "Price"]
    print(table_header(*table_head))
    for d in data:
        print(table_row(*d))

    table_width = len(table_head) * (10 + 1)
    print(table_line("-", table_width))
