from cmath import pi
from multiprocessing.sharedctypes import Value
from tkinter import Y
import pwinput
import os
import time
from termcolor import cprint   

datauser = {
    "username" : ["alby", "arin", "novil"],
    "password" : ['123', '123', '123'],
    "id" : ['1', '2', '3']
}

angka = [53,20,19,78,43,10,27,3,14,98]


def cs():
    os.system('cls')
    time.sleep(1)


def check():
    print("\nData Angka:", angka)
    print("Panjang Data Angka Sekarang:", len(angka))
    time.sleep(1.5)
    return menu1()

#function untuk menambahkan data
def add():
    angka.append(int(input("Masukkan Angka yang ingin ditambahkan: ")))
    cs()
    print("Data Angka berhasil ditambahkan.")
    time.sleep(2)
    cs()
    check()
    time.sleep(1.5)
    return menu1()

#function untuk menghapus data
def delete():
    angka.pop(int(input("\nMasukkan index Angka ke berapa yang ingin dihapus: ")))
    cs()
    print("Data Angka berhasil dihapus.")
    time.sleep(1)
    cs()
    check()
    time.sleep(1.5)
    return menu1()

def searching():
    datasort = merge_sort(angka)
    y = len(angka)
    x = int(input("\nMasukkan Angka yang ingin dicari: "))
    index = search(datasort, x, y)
    if index >= 0:
        time.sleep(1)
        print("Number", x, "Has Been Found Out!")
        time.sleep(2)
        print("\nData Number:", datasort)
        print("Data Number Length Now :", len(datasort))
        print("Angka", x, "berada di index ke:", index)
        time.sleep(1)
        return menu1()
        
    else:
        cs()
        print("Sorry, Number", x, "Not Found!")
        time.sleep(2)
        cs()
        menu1()

def search(angka, x, y):
    offset = -1

    fib2 = 0
    fib1 = 1
    fib = fib2 + fib1

    while (fib < y):
        fib2 = fib1
        fib1 = fib
        fib = fib2 + fib1

    while (fib > 1):
        i = min(offset + fib2, y-1)
        if (angka[i] > x):
            fib = fib1
            fib1 = fib2
            fib2 = fib - fib1
            offset = i

        elif (angka[i] < x):
            fib = fib2
            fib1 = fib1 - fib2
            fib2 = fib - fib1

        else:
            return i

    if (fib1 and angka[y-1] == x):
        return y-1
    return -1


def merge_sort(angka):
    if len(angka) <= 1:
        return angka
    mid = len(angka) // 2
    left = merge_sort(angka[:mid])
    right = merge_sort(angka[mid:])
    return merge(left, right)

#function untuk menggabungkan 2 array sebelumnya
def merge(left, right):
    result = []
    i, j = 0, 0

    while i < len(left) and j < len(right):
        if left[i] > right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    result += left[i:]
    result += right[j:]
    return result



def menu1():
    print("""
=========================== Menu ===========================
|                        1. Check Data                     |
|                        2. Add Data                       |
|                        3. Search Data                    |
|                        4. Delete Data                    |
|                        5. Descending Data                |
|                        6. Exit                           |
============================================================
        """)
    choice = input("Silahkan Masukkan Pilihan Anda: ")
    try:
        if choice == "1":
            check()
        elif choice == "2":
            add()
        elif choice == "3":
            searching()
        elif choice == "4":
            delete()
        elif choice == "5":
            print(f"""{" Descending Data "}""".center(50,"="))
            print("\nData Normal: ", angka)
            print("Descending Data :  ", merge_sort(angka))
            menu1()
        elif choice == "6":
            exit()
        else: 
            cprint("Sorry, Your Input is Wrong. Please Try Again!", "red")
            menu1()
    except ValueError:
        cprint("Sorry, Your Input is Wrong. Please Try Again!", "red")
        cs()
        return menu1()
    
def menu():
    print("""
======================== Menu Login ========================
|                        1. Login                          |
|                        2. Register                       |
|                        3. Exit                           |
============================================================
        """)
    choice = input("Masukkan Pilihan Anda : ")
    try:
        if choice == "1":
            print("Silahkan masukkan Username dan Password Anda!!")
            login()
        elif choice == "2":
            register()
        elif choice == "3":
            exit()
    except ValueError:
        cprint("Sorry, Your Input is Wrong. Please Try Again!", "red")
        return menu()
        

def register():
    while True:
        add_username = input("Enter Your Username: ")
        if add_username in datauser.get("username"):
            cs()
            time.sleep
            cprint("Maaf Username Anda telah tersedia!!\nSilahkan Masukkan Ulang", 'red')
            register()
        else: 
            add_password = input("Enter Your Password: ")
            datauser.get("username").append(add_username)
            datauser.get("password").append(add_password)
            id = len(datauser.get('id'))
            datauser.get('id').append(id+1)
            time.sleep(1)
            cprint("Register Sucessful!!", "green")
            return menu()

def login():
    while True:
            try:
                username = input("Please Enter Your Username  : ")
                password = pwinput.pwinput("Please Enter Your Password : ")
                index = datauser.get("username").index(username)
                if username == datauser.get("username")[index] and password == datauser.get("password")[index]:
                    cprint("Login Sucess!", "green")
                    time.sleep(1.5)
                    cs()
                    print("Welcome to Our APP", datauser['username'][index])
                    menu1()
                    
                else : 
                    cprint("Login Failed!", "red")
                    cprint("Your Account or Password is incorrect. Please Try it Again!", "red")
                    # cs()
                    login()
            except ValueError:
                cprint("Sorry, your input is wrong. Please Try it Again!!", "yellow")
                # cs()
                login()


menu()