master_pwd = input("Enter your master password to access modes: ")

def add():
    website = input("URL/Website: ")
    name = input("Username: ")
    pwd = input("Password: ")

    with open("password.txt", 'a') as f:
        f.write(website + " | " + name + " | " + pwd + "\n")


def view():
    with open("password.txt",'r') as f:
        for line in f.readlines():
            print(line.rstrip())


while True:
    mode = input("Do you want to add a new password, view previous passwords or quit (add/view/quit): ").lower()
    if mode == "quit":
        continue

    if mode == "add":
        add()
    elif mode == "view":
        view()
    else:
        print("Invalid mode! Type add/view or quit")
        break