# Zestaw 3. Napisz funkcję szyfrującą wiadomość szyfrem cezara. Dla ułatwienia należy przekształcić wiadomość tak aby zawierała tylko wielkie lub małe litery.
# Funkcja przyjmuje:
# wiadomość - tekst do zaszyfrowania
# klucz – liczbę o ile należy przesunąć litery w alfabecie
# zwraca zaszyfrowaną wiadomość w formie łańcucha znaków -string. (40%)
# Funkcja szyfruje tylko litery – inne znaki wstawia do końcowej zaszyfrowanej wiadomości bez zmian(10%)
# Funkcja rozwiązuje problem klucza przesuwającego litery poza zakres listy  z alfabetem oraz problem podania klucza o dowolnej wielkości(20%).
# Funkcja opcjonalnie przyjmuje dowolny alfabet. Domyślnie używa angielskiego(10%).
import getpass

napis = getpass.getpass("Podaj slowo do zaszyfrowania: ").upper()
print(napis)
szyfr = getpass.getpass("Podaj szyfr: ").upper()
print(szyfr)
opt = input("Czy chcesz podać własny alfabet? (0-nie 1-tak): ")
alphabet = []


def getA():
    a = input("Podaj alfabet (litery rozdzielone spacjami)\n").upper().split(" ")
    for i in szyfr:
        if a.count(i) == 0:
            print("Szyfr nie pasuje do podanego alfabetu!" + str(a))
            return getA()
    return a


if opt == "1":
    alphabet = getA()


def fun(n, a=None):
    if a is None:
        a = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T',
             'U',
             'V', 'W', 'X', 'Y', 'Z']
    index = 0
    ans = ""
    for i in n:
        if a.count(i) == 0:
            ans += i
        else:
            i = a.index(i) + (a.index(szyfr[index % len(szyfr)]))
            index += 1
            ans += a[i % len(a)]
    return ans


if opt == 1:
    print(fun(napis, alphabet))
else:
    print(fun(napis))
