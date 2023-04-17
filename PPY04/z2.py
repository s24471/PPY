# Zadanie 2. Napisz funkcję sprawdzającą czy podane liczby są
# liczbami pierwszymi w szybszy sposób niż w przykładzie. (jakim przykladzie?)
# Do funkcji można przekazać dowolną liczbę argumentów (liczby). Liczby 0 i 1 nie są liczbami pierwszymi. (10%)

liczby = input("Podaj liczby oddzielone pojedynczymi znakami spacji:\n")
liczby = liczby.split(" ")


def fun(l):
    a = []
    for i in l:
        a.append(int(i))
    pierwsze = []
    for i in range(max(a) + 1):
        pierwsze.append(True)
    pierwsze[0] = False
    pierwsze[1] = False
    for i in range(len(pierwsze)):
        if pierwsze[i]:
            kw = i * i
            while kw < len(pierwsze):
                pierwsze[kw] = False
                kw += i

    for i in a:
        print(str(i) + " -> " + str(pierwsze[i]))


fun(liczby)
