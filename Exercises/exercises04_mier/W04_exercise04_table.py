# coding: utf-8

def table_line(line_char: str, n: int) -> str:
    """Return a table row break string"""
    return " " + line_char * n + "\n"


def table_header(*args, format=["<10s", ">10s", ">10s"], print_header=False):
    """
    row(): Pretty print a table header
    """
    table_width = len(args) * (10 + 4)

    header_top = table_line("–", table_width)
    header_string = f"|{args[0]:{format[0]}}\t|{args[1]:{format[1]}}|\t{args[2]:{format[2]}}|\n"
    header_bottom = table_line("–", table_width)

    return header_top + header_string + header_bottom


def table_row(*args, format=["<10s", ">10.2f"], print_row=False):
    """
    row(): Pretty print a table row

    The functions returns a formatted table row as a string.

    When printed, a table row looks like this:

    | <date string> | <number of items> | <price per item> |

    """

    # First column (date) has a special format
    row_string = f"|{args[0]:{format[0]}}\t|"

    for arg in args[1:]:
        row_string += f"{arg:{format[1]}}|\t"
    # row_string += "|"

    if print_row:
        print(row_string)

    return row_string



if __name__ == "__main__":
    table_head = ["Date", "No items", "Price"]

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

    print(table_header(*table_head))
    for d in data:
        print(table_row(*d))

    table_width = len(table_head) * (10 + 4)
    print(table_line("–", table_width))
