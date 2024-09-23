line = "this,is,a,line,with,lots,of,commas"

print("Using a list comprehension")
print([x.upper() for x in line.split(',')] + 'NOW,IN,UPPERCASE'.split(","))

print()
print("Using map")
print(list(map(str.upper, line.split(','))))

print()
print("Using a generator expression")
print(list(str.upper(x) for x in line.split(',')))


# Duplicate words
print()
print("Using map")
print(list(map(lambda x: x.title() * 2, line.split(','))))

print()
print("Using a generator expression")
print(list(x.title() * 2 for x in line.split(',')))

# Squares
print()
print("Using map")
print(list(map(lambda x: x**2, range(10))))  # Rather messy
print("Using a generator expression")
print(list(x ** 2 for x in range(10)))       # Prettier


# Nested expressions
print()
print("Nested expression")

nums = (-4, -3, -2, -1, 0, 1, 2 , 3, 4)
print(f"{nums = }")

print()
print("list(x ** 2 for x in (abs(x) for x in nums))")
print(list(x ** 2 for x in (abs(x) for x in nums)))
