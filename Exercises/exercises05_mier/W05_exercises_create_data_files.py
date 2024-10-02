numbers = [str(k) + "\n" for k in range(42)]
with open("data_1.txt", "w") as f:
    for k in numbers:
        f.write(k)


with open("data_2.txt", "w") as f:
    f.writelines(numbers)




print("Great success")
