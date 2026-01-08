import random
import string

def generate_password(length):

    if length < 4:

        return "Length must be at least four characters"

    password = [
        random.choice(string.ascii_lowercase),
        random.choice(string.ascii_uppercase),
        random.choice(string.digits),
        random.choice(string.punctuation)
    ]

    all_chars = (
        string.ascii_lowercase +
        string.ascii_uppercase +
        string.digits +
        string.punctuation
    )

    for _ in range(length - 4):

        password.append(random.choice(all_chars))

    random.shuffle(password)

    return "".join(password)

while True:

    print("\nGenerate Password Enter 1")
    print("Exit Enter 2\n")

    choice = input("Enter your choice : ")

    if choice == "1":

        print(" --- Password Generator --- ")

        length = int(input("Enter password length : "))

        print("Generated Password :", generate_password(length))

    elif choice == "2":

        print("Exiting...")

        break

    else:
        
        print("Choose correct choice")
