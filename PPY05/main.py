# Zadanie:
# Napisz program który:
# 1. Wczyta z pliku dane dotyczące studentów – email, imię, nazwisko oraz liczbę uzyskanych punktów z przedmiotu Podstawy Programowania Python.
# Dodatkowo w pliku mogą znajdować się w tej samej linii dane dotyczące oceny końcowej oraz statusu (‘’, GRADED, MAILED). Zakładamy, że plik istnieje
# – może być pusty lub zawiera podstawowe informacje: email, imię, nazwisko, punkty. Do przechowywania danych w programie użyj słownika oraz zagnieżdżania (20%).
#
# 2. Umożliwi automatyczne wystawianie oceny wszystkim studentom, którzy jeszcze nie mają wystawionej oceny (status różny od GRADED oraz MAILED),
# zgodnie z punktacją zaproponowaną w regulaminie zaliczenia przedmiotu (20%).
# 3. Umożliwi usuwanie oraz dodawanie studentów ręcznie (sprawdzanie czy email jest już zajęty) (20%).
# 4. Umożliwi wysyłanie emaila z informacją o wystawionej ocenie wszystkim studentom ze statusem innym niż MAILED (20%).
# 5. Każda zmiana - dodawanie / usuwanie danych studenta, wysłanie maila, ocena – zapisze zmiany również w pliku (20%).
#
# ''' 50 i mniej - 2
#     51 -60 pkt - 3
#     61 – 70 pkt – 3.5
#     71 – 80 pkt - 4
#     81 - 90 pkt – 4.5
#     91 - 100 pkt - 5
# '''
import smtplib
from email.mime.text import MIMEText
from tkinter import *
from tkinter import messagebox

from tkscrolledframe import ScrolledFrame

students = {}
sf_inner = ""
sf = ""
with open('students.txt', 'r') as file:
    for line in file:
        data = line.strip().split(' ')
        email, first_name, last_name, points = data[:4]
        final_grade = data[4] if len(data) > 4 else ''
        status = \
            data[5] if len(data) > 5 else \
                'GRADED' if len(data) == 5 else ''
        # nie bylo sprecyzowane czy moze byc Final Grade bez Statusu

        student = {
            'email': email,
            'first_name': first_name,
            'last_name': last_name,
            'points': int(points),
            'final_grade': final_grade,
            'status': status
        }

        students[email] = student
print(students)


def zmiana():

    update_students_list()
    with open('students.txt', 'r') as file:
        lines = file.readlines()

    with open('students.txt', 'w') as file:
        for line in lines:
            parts = line.strip().split(' ')
            email = parts[0]
            if email in students:
                student = students[email]
                new_line = f"{student['email']} {student['first_name']} {student['last_name']} {student['points']}{(' ' + student['final_grade']) if student['final_grade'] != '' else ''}{(' ' + student['status']) if student['status'] != '' else ''}\n"
                file.write(new_line)

def add_student():
    add_window = Toplevel()
    add_window.title("Dodaj studenta")

    email_label = Label(add_window, text="E-mail:")
    email_label.grid(row=0, column=0)
    email_entry = Entry(add_window)
    email_entry.grid(row=0, column=1)

    first_name_label = Label(add_window, text="Imię:")
    first_name_label.grid(row=1, column=0)
    first_name_entry = Entry(add_window)
    first_name_entry.grid(row=1, column=1)

    last_name_label = Label(add_window, text="Nazwisko:")
    last_name_label.grid(row=2, column=0)
    last_name_entry = Entry(add_window)
    last_name_entry.grid(row=2, column=1)

    points_label = Label(add_window, text="Punkty:")
    points_label.grid(row=3, column=0)
    points_entry = Entry(add_window)
    points_entry.grid(row=3, column=1)
    ocena_label = Label(add_window, text="Ocena:")
    ocena_label.grid(row=4, column=0)
    ocena_entry = Entry(add_window)
    ocena_entry.grid(row=4, column=1)
    status_label = Label(add_window, text="Status:")
    status_label.grid(row=5, column=0)
    status_entry = Entry(add_window)
    status_entry.grid(row=5, column=1)

    add_button = Button(add_window, text="Dodaj", command=lambda: save_student(email_entry.get(), first_name_entry.get(), last_name_entry.get(), points_entry.get(), ocena_entry.get(), status_entry.get()))
    add_button.grid(row=6, column=0, columnspan=2)

    def save_student(email, first_name, last_name, points, ocena, status):
        if email in students:
            messagebox.showerror("Błąd", "E-mail jest już zajęty!")
            return

        student = {
            "email": email,
            "first_name": first_name,
            "last_name": last_name,
            "points": int(points),
            "final_grade": ocena,
            "status": status
        }

        students[email] = student
        with open("students.txt", 'a') as p:
            p.write(f"{student['email']} {student['first_name']} {student['last_name']} {student['points']}{(' ' + student['final_grade']) if student['final_grade'] != '' else ''}{(' ' + student['status']) if student['status'] != '' else ''}\n"
                )
        zmiana()
        update_students_list()
        add_window.destroy()


def remove_student(email):
    students.pop(email)
    zmiana()


def grade(student):
    points = student['points']
    if points <= 50:
        student['final_grade'] = '2'
    elif points <= 60:
        student['final_grade'] = '3'
    elif points <= 70:
        student['final_grade'] = '3.5'
    elif points <= 80:
        student['final_grade'] = '4'
    elif points <= 90:
        student['final_grade'] = '4.5'
    else:
        student['final_grade'] = '5'
    student['status'] = 'GRADED'
    zmiana()

def mail(student):
    if(student['status']!='GRADED'):
        grade(student)
    subject = "PPY końcowa ocena"
    body = "Twoja końcowa ocena z przedmiotu 'Podstawy Programowania Python' wynosi: " + student["final_grade"]
    sender = ""  #należy podać maila @TODO
    password = ""  # należy podać hasło do aplikacji @TODO
    recipient = student["email"]
    msg=MIMEText(body)
    msg['Subject'] = subject
    msg['From'] = sender
    msg['To'] = recipient
    smtp_server = smtplib.SMTP_SSL('smtp.gmail.com',465)
    smtp_server.login(sender,password)
    smtp_server.sendmail(sender,recipient,msg.as_string())
    smtp_server.quit()
    student['status'] = 'MAILED'
    zmiana()

def mail_all():
    for email, student in students.items():
        mail(student)
def grade_all():
    for email, student in students.items():
        if student['status']!= "GRADED" and student['status']!= "MAILED":
            grade(student)


def update_students_list():
    global sf_inner
    sf_inner.destroy()

    sf_inner = sf.display_widget(Frame)
    sf_inner.pack()
    email_label = Label(sf_inner, text='E-mail')
    email_label.grid(row=0, column=0)

    name_label = Label(sf_inner, text='Imię i nazwisko')
    name_label.grid(row=0, column=1)

    points_label = Label(sf_inner, text='Punkty')
    points_label.grid(row=0, column=2)

    points_label = Label(sf_inner, text='Ocena')
    points_label.grid(row=0, column=3)

    points_label = Label(sf_inner, text='Status')
    points_label.grid(row=0, column=4)
    row = 1
    for email, student in students.items():
        c = 0
        email_label = Label(sf_inner, text=student['email'])
        email_label.grid(row=row, column=c)
        c += 1

        name_label = Label(sf_inner, text=f"{student['first_name']} {student['last_name']}")
        name_label.grid(row=row, column=c)
        c += 1

        points_label = Label(sf_inner, text=student['points'])
        points_label.grid(row=row, column=c)
        c += 1

        grade_label = Label(sf_inner, text=student['final_grade'])
        grade_label.grid(row=row, column=c)
        c += 1

        status_label = Label(sf_inner, text=student['status'])
        status_label.grid(row=row, column=c)
        c += 1

        if student['status'] != 'MAILED' and student['status'] != 'GRADED':
            grade_button = Button(sf_inner, text='Wystaw ocenę', command=lambda student=student: grade(student))
            grade_button.grid(row=row, column=c)
            c += 1

        if student['status'] == 'GRADED':
            mail_button = Button(sf_inner, text='Wyślij mail', command=lambda student=student: mail(student))
            mail_button.grid(row=row, column=c)
            c += 1

        remove_button = Button(sf_inner, text='Usuń', command=lambda email=email: remove_student(email))
        remove_button.grid(row=row, column=c)
        c += 1

        row += 1


def init_window():
    global sf_inner

    root = Tk()
    root.title("Lista studentów")
    global sf

    sf = ScrolledFrame(root, width=640, height=480)
    sf.pack(side="top", expand=1, fill="both")
    sf_inner = sf.display_widget(Frame)
    sf_inner.pack(expand=True, fill='both')

    email_label = Label(sf_inner, text='E-mail')
    email_label.grid(row=0, column=0)

    name_label = Label(sf_inner, text='Imię i nazwisko')
    name_label.grid(row=0, column=1)

    points_label = Label(sf_inner, text='Punkty')
    points_label.grid(row=0, column=2)

    add_button = Button(root, text='Dodaj studenta', command=add_student)
    add_button.pack(side="left", padx=10, pady=10)
    add_button = Button(root, text='Wyslij maile', command=mail_all)
    add_button.pack(side="left", padx=10, pady=10)
    add_button = Button(root, text='Wystaw oceny', command=grade_all)
    add_button.pack(side="left", padx=10, pady=10)

    update_students_list()

    root.mainloop()


init_window()
