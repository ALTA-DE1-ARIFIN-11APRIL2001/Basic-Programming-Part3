bilangan = int(input("Masukkan bilangan: "))

print("Faktor dari", bilangan, "adalah:")
for i in range(1, bilangan + 1):
    if bilangan % i == 0:
        print(i)
