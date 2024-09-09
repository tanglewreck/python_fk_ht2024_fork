# Denna övning är lik den föregående men lägger till att funktioner ska användas.

# Skapa en funktion som tar emot tal som ett eller flera argument, ni väljer
# själva hur funktionen tar emot och behandlar talen, och sen adderar det som
# funktionen tagit emot samt skriver ut summan.

# Funktionen ska därefter anropas flera gånger, en gång för varje tal, med dessa tal:
# 1, 2, 8, 9
# 11, 42
# 9001, 4242
# Alla tal från 1 till och med 10

# Funktionen ska alltså anropas fyra gånger och de fyra resultaten som skrivs
# ut ska vara: 20, 53, 13243, 55
# Att hårdkoda är INTE korrekt.

L_1 = (1, 2, 8, 9)
L_2 = (11, 42)
L_3 = (9001, 4242)
L_4 = list(range(1, 11))

def my_sum(*args):
    try:
        s = sum(list(args))
        return s
    except TypeError as e:
        print(str(e))
        raise SystemExit(1)


if __name__ == "__main__":
    for k in range(1, 5):
        L = eval(f"L_{k}")
        print(f"sum of {L}: {my_sum(*L)}")
