book = {}

def add_contact():
    new_contact = input("Enter a new contact: ")
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
        
while True:
    print("Phonebook Manager")
    print("Press \"+\" to add a new contact.")
    print("Press \"-\" to delete a new contact.")
    print("Press \"f\" to find a new contact.")
    print("Press \"p\" to fprint out all contacts in the phonebook.")
    print("Press \"q\" to quit the program.")
    print("===================")
    
    cmd = input("Enter a command: ")
    
    if cmd == "+":
        add_contact()
    elif cmd == "-":
        delete_contact()
    elif cmd == "f":
        find_contact()
    elif cmd == "p":
        print_all()
    elif cmd == "q":
        break