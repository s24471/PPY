import random
from getpass import getpass

opcje = ["Kamień", "Papier", "Nożyce"]
wyniki = []
ilosc = int(input("Podaj ilosc rund:\n"))
tryb = int(input("Podaj tryb gry: (1- gracz vs komputer, 2- gracz vs gracz)\n"))
imiona = []
w1 = 0
w2 = 0
for i in range(0, tryb):
    imiona.append(input("Podaj imie gracza " + str(i + 1) + ":\n"))
if (tryb == 1):
    imiona.append("Komputer")
for i in range(0, ilosc):
    picked = int(getpass(prompt=("Gracz " + imiona[0] + " wybiera: (1- kamień, 2- papier, 3- nożyce\n")))
    if (tryb == 2):
        picked2 = int(getpass(prompt=("Gracz " + imiona[1] + " wybiera: (1- kamień, 2- papier, 3- nożyce\n")))
    else:
        picked2 = random.randrange(1, 4)
        print("Komputer wybiera ") #+ opcje[(picked2-1)])
    if picked == picked2:
        tmp = "Remis!"
    else:
        if picked == 1:
            if picked2 == 3:
                tmp = ("Wygral " + imiona[0])
                w1 += 1
            else:
                tmp = ("Wygral " + imiona[1])
                w2 += 1
        else:
            if picked == 2:
                if picked2 == 1:
                    tmp = ("Wygral " + imiona[0])
                    w1 += 1
                else:
                    tmp = ("Wygral " + imiona[1])
                    w2 += 1
            else:
                if picked2 == 2:
                    tmp = ("Wygral " + imiona[0])
                    w1 += 1
                else:
                    tmp = ("Wygral " + imiona[1])
                    w2 += 1

    wyniki.append(opcje[picked-1] + " vs " + opcje[picked2-1]+" "+tmp)
    print(tmp)
    print(str(w1) + " vs " + str(w2))
print("====Historia====")
for s in wyniki:
    print(s)
print("=======Wyniki=======")


print(imiona[0] + ": " + str(w1))
print(imiona[1] + ": " + str(w2))
if(w1>w2):
    print("Wyrgał " + imiona[0])
else:
    if(w2>w1):
        print("Wygrał " + imiona[1])
    else:
        print("Remis!")
