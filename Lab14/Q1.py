book = {}
import pickle
import os.path
import sys
from tkinter.filedialog import askopenfilename
from tkinter.filedialog import asksaveasfilename
old_file = ""

def add_contact():
    new_contact = input("Enter a new contact: ")
    if new_contact == "contact":
        raise ValueError("Contact cannot contain the word \"contact\"")
    
    if new_contact in book:
        print("This contact is already in the book | to change number \"c\" | to detete \"d\"")
        cmd1 = input("Enter: ")
        if cmd1 == "d":
            del book[new_contact]
        elif cmd1 == "c":
            number = input("Enter new number: ")
            book[new_contact] = number
    else:
        number = input("Enter number: ")
        book[new_contact] = number
    
def delete_contact():
    contact = input("Enter the contact to delete: ")
    if contact in book:
        del book[contact]
    else:
        print(f"There is no contact {contact}")

def find_contact():
    contact = input("Enter the contact to find: ")
    if contact in book:
        print(f"Contact: {contact}, Number: {book[contact]}")
    else:
        print(f"There is no contact: {contact}")
        
def print_all():
    for contact in book:
        print(f"Contact: {contact}, Number: {book[contact]}")
    print("===================")

def exists(old_file):
    if os.path.isfile(old_file):
        raise RuntimeError("File already exists.")

def save_contacts():
    file = asksaveasfilename()
    global old_file
    old_file = file
    try:
        exists(old_file)
        if file:
            with open(file, "wb") as f:
                pickle.dump(book, f)
                f.close()
    
    except RuntimeError as e:
        print(e)
        return
        
def load_contacts():
    global old_file
    global book
    if os.path.isfile(old_file):
        print(f"{old_file} exists.")
        with open(old_file, "rb") as f:
            book = pickle.load(f)
            f.close()
    else:
        # file = input("Enter the file name: ")
        file_load = askopenfilename()
        try:
            with open(file_load, "rb") as f:
                book = pickle.load(f)
                f.close()
        except IOError:
            print("File does not exist.")
            return

while True:
    print("Phonebook Manager")
    print("Press \"+\" to add a new contact.")
    print("Press \"-\" to delete a new contact.")
    print("Press \"f\" to find a new contact.")
    print("Press \"s\" to save the contacts to a file.")
    print("Press \"l\" to load the contacts from a file.")
    print("Press \"p\" to fprint out all contacts in the phonebook.")
    print("Press \"q\" to quit the program.")
    
    print("===================")
    
    cmd = input("Enter a command: ")
    
    if cmd == "+":
        try:
            add_contact()
        except ValueError as e:
            print(e)
    elif cmd == "-":
        delete_contact()
    elif cmd == "f":
        find_contact()
    elif cmd == "p":
        print_all()
    elif cmd == "s":
        save_contacts()
    elif cmd == "l":
        load_contacts()
    elif cmd == "q":
        break