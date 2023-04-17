import random

a = input("Podaj liczby:\n")
a=a.split(",")
min = a[0]
max = a[0]
for i in a[1::]:
    if i < min:
        min = i
    if i > max:
        max = i
print("max: " + max)
print("min: " + min)

print("zadanie 2")

choice = input("Czy miał pan na myśli z listy 10ciu miast czy 10 nawiekszych z wiekszej lisy? 1-lista o wielkosci 10, 2-lista wieksza\n")
if choice == 1:
    miasta = ["Warsaw", "Kraków", "Łódź", "Wrocław", "Poznań", "Gdańsk", "Szczecin", "Bydgoszcz", "Lublin", "Białystok"]
    random.shuffle(miasta)
    print(miasta)
else:
    miasta = ["Warsaw", "Kraków", "Łódź", "Wrocław", "Poznań", "Gdańsk", "Szczecin", "Bydgoszcz", "Lublin", "Białystok", "Wołomin", "Radzymin"]
    wynik = []
    for i in range(10):
        losowa = random.randint(0, len(miasta))
        wynik.append(miasta[losowa])
        miasta.remove(miasta[losowa])
    print(wynik)