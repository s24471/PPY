# Lista1

'''
UWAGA! Nie należy zmieniać nazw funkcji, oraz wartości zmiennych podanych w pliku
poza wartościami ze stringiem "PODAJ WYNIK" - w tych zmiennych należy przechowywać wynik
dotyczący poszczególnych zadań w_1, w_2 ... w_6.

Ciało funkcji wpisujemy w kodzie zamiast "pass".

Wyniki z każdego zadania powinny wyświetlać się w jednej linijce.
Nie należy wyświetlań nic poza wynikiem działania kodu z poszczególnych zadań
w kolejności tak jak w pliku.
Plik należy zapisać w postaci: imie_nazwisko_lista1.py
'''
import random

# 1. Ile unikatowych elementów znajduje się w liście:
# 1 pkt
lista_1 = [0, 7, 8, 3, 3, 0, 7, 0, 3]
unique = []
for i in lista_1:
    if i not in unique:
        unique.append(i)
w_1 = str(len(unique))
print(w_1)

# 2. Napisz kod, który podmieni losowy znak ze stringa
s_2 = "ala ma kota"
# na '0':
# 2 pkt
tmp = s_2
tmp2 = random.randrange(len(s_2))
tmp = tmp[:tmp2] + '0' + tmp[tmp2 + 1:]

w_2 = tmp
print(w_2)

# 3. Napisz kod który podmieni z lista_3 język programowania R na JS, następnie wyświetl podmieniony JS.
# Przed JS nadal musi znajdować się python w strukturze takiego samego typu jak w przykladowej lista_3.
# 2pkt
lista_3 = [[{1: 'java', 0: ('python', 'R')}, 'c++'], ['word', 'excel']]
tmp = lista_3
tmp2 = list(lista_3[0][0][0])
tmp2[1] = 'JS'
tmp[0][0][0] = tuple(tmp2)
w_3 = tmp
print(w_3)

# 4. Jakiego typu dane z poniższych nie mogą być kluczami słownika?
# boolean,float,int,string,tuple,list,set. Odpowiedź umieśc w stringu w_4
# 1 pkt

w_4 = "list,set"
print(w_4)

# 5. Dla stringa wypisz
# ile razy pojawił się dany znak, w kolejności alfabetycznej.
# Użyj słownika - wynik również ma być słownikiem.
# Sprawdzamy tylko te znaki, które występują w podanym stringu.
# 2 pkt

s_5 = "ala ma kota imie ma macko"
tmp2 = ''.join(sorted(s_5))
tmp = {}
for i in tmp2:
    if i not in tmp:
        tmp[i] = 1
    else:
        tmp[i] += 1

w_5 = str(tmp)
print(w_5)

# 6. Napisz kod który sprawdzi, czy w poprzednim stringu s_5,
# jakikolwiek znak wystąpił dokładnie 3 razy. Wyświetl Tak jeżeli wystąpił,
# Nie jeżeli nie wystąpił.
# 1 pkt
tmp = "Tak" if 3 in tmp.values() else "Nie"
w_6 = tmp
print(w_6)


# 7. Napisz funkcję sprawdzającą czy podane słowa/zdania są palindromem
# i zwróci True lub False ( jest/ nie jest).
# Pomiń znaki nie będące literami, wielkość liter nie ma znaczenia
# 3pkt

def palindrom(s):
    s = ''.join(x for x in s if x.isalpha()).lower()
    return s == s[::-1]


s_7_1 = "Nowy Targ, góry, Zakopane – na pokazy róg, graty won"
print(palindrom(s_7_1))


# 8. Napisz funkcję, która zwróci
# wszystkie liczby od 1 do n w jednym stringu rozdzielone przecinkami,
# jednak jeżeli liczba jest podzielna przez:
# trzy – zamiast liczby mamy „Fizz”,
# pięć – zamiast liczby mamy „Buzz”,
# trzy i pięć zamiast liczby mamy „FizzBuzz”.
# wszystkie liczby/słowa mają zostać zwróćone w jednej linii, oraz być rozdzielone przecinkiem
# BEZ spacji
# 2 pkt

def fizzbuzz(n):
    s = ""
    for i in range(n):
        a = 0
        if (i + 1) % 3 == 0:
            s += "Fizz"
            a=1
        if (i + 1) % 5 == 0:
            s += "Byzz"
            a=1
        if a==0:
            s+=str(i+1)
        if i+1 != n:
            s += ","
    return s


n_8 = 16
print(fizzbuzz(n_8))

# 9. Napisz funkcję zwracającą n-ty element ciągu Fibonacciego
# przy F(0)= 0 i F(1) = 1.
# bez rekurencji:
# 3 pkt

n_9 = 6


def fibonacci(n):
    if n < 2:
        return n
    f=1
    ff = 0

    for i in range(n-1):
        tmp = f
        f= f+ff
        ff = tmp
    return f


print(fibonacci(n_9))


# 10. Napisz funkcję, która dla podanej posortowanej listy
# zwróci index wyszukiwanego elementu za pomocą wyszkukiwania binarnego,
# lub zwróci None gdy nie ma elementu w liscie:
# 3 pkt


def binary_search(lista, e):
    start = 0
    end = len(lista) - 1

    while start <= end:
        mid = (start + end) // 2
        if lista[mid] == e:
            return mid
        elif lista[mid] < e:
            start = mid + 1
        else:
            end = mid - 1
    return None


l_10 = [0, 2, 4, 8, 16, 32, 64, 128, 256, 512, 1024, 2048, 4096, 8192, 16384, 32768]
print(binary_search(l_10, 2))
