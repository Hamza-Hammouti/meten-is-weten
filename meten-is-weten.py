print("-------------------------------")
a = int(input("Welke waarde heeft A?: "))
b = int(input("Welke waarde heeft B?: "))
print("-------------------------------")
max = 0
min = 0

if a > b:
    max = a
    print(f"A is het grootste getal. Waarde: {max}")
elif a < b:
    max = b
    print(f"B is het grootste getal. Waarde: {max}")