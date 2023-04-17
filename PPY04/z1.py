# Zadanie 1. Napisz funkcję obliczającą i zwracającą ilość potrzebnych opakowań paneli
# w danym pomieszczeniu, zakładając prostokątną podłogę i prostokątne panele.
# Dane wejściowe to długość i szerokość podłogi,
# (do powierzchni pomieszczenia należy dodać 10%)
# długość i szerokość panela oraz ilość paneli w opakowaniu. (10%)
import math

dlugosc_podlogi = int(input("Podaj długość podłogi: "))
szerokosc_podlogi = int(input("Podaj szerokość podłogi: "))
dlugosc_panela = int(input("Podaj długość panela: "))
szerokosc_panela = int(input("Podaj szerokość panela: "))
ilosc_paneli_w_opakowaniu = int(input("Podaj ilosc panieli w paczce: "))


def fun(dl_podlogi, sz_podlogi, dl_panela, sz_panela, ilosc):
    po_pomieszczenia = dl_podlogi * sz_podlogi * 1.1
    p_jednego_panela = dl_panela * sz_panela
    ilosc_paneli = po_pomieszczenia / p_jednego_panela
    ilosc_opakowan = math.ceil(ilosc_paneli / ilosc)
    return ilosc_opakowan


print(fun(dlugosc_podlogi, szerokosc_podlogi, dlugosc_panela, szerokosc_panela, ilosc_paneli_w_opakowaniu))
