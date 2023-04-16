
s1 = s2 = s3 = "Python 2023"

def a():
    print(s1 == s2 == s3)
def b():
    print(type(s1), hex(id(s1)))
    print(type(s2), hex(id(s2)))
    print(type(s3), hex(id(s3)))
a()
b()
s3="Java 11"
a()
b()
def z2():
    a = input("Podaj liczbe no. 1: ")
    b = input("Podaj liczbe no. b: ")
    x = input("Podaj znak: ")
    print(eval(a+x+b))

z2()



def submit():
    for i in range(len(pytania)):
        print("pytanie: " + str(pytania_txt[i]))
        print("odpowiedź: " + str(pytania[i].get()))
import tkinter as tk
from tkinter import ttk
app = tk.Tk()
app.title("Ankieta czytelnicza")

intro = tk.Label(app, text="Ankieta czytelnicza:", font=("Arial", 12, "bold"))
intro.pack(pady=10)

pytania = []

pytania_txt = [
    "1. Najczęstszym sposobem spędzania wolnego czasu jest dla Ciebie: ",
    "2. W jakich okolicznościach czytasz książki najczęściej?",
    "3. Jeżeli spędzasz czas wolny czytając książki, jaki jest główny powód takiego wyboru?",
    "4. Po książki w jakiej formie sięgasz najczęściej?",
    "5. Jakie masz imie i nazwisko?"
]

for txt in pytania_txt:
    frame = ttk.Frame(app)
    frame.pack(pady=5)
    label = ttk.Label(frame, text=txt, font=("Arial", 10))
    label.pack(side=tk.LEFT, padx=15)
    q = tk.StringVar()
    entry = ttk.Entry(frame, textvariable=q, width=40)
    entry.pack(side=tk.LEFT)
    pytania.append(q)

submit = ttk.Button(app, text="Wyślij", command=submit)
submit.pack(pady=10)

app.mainloop()