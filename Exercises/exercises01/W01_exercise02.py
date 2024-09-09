# Skriv kod som beräknar summan av alla tal från 1 till och med 10.
# Summan ska därefter skrivas ut.
# Siffran som ska skrivas ut är alltså 55.

# Det finns flera möjliga sätt att lösa denna uppgift på, vilket sätt ni
# löser uppgiften på är valfritt.
# Att hårdkoda, d.v.s. att skriva print(55) är INTE rätt.

# Ett möjligt sätt att lösa denna uppgift är att använda sig av en while-loop.
N = 10

s = 0
for k in range(1, N + 1):
    s += k
print(f"sum(1) = {s}")


s = k = 0
while k <= N:
    s += k
    k += 1
print(f"sum(2) = {s}")


s = sum(list(range(1, 11)))
print(f"sum(3) = {s}")
