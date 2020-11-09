from colorama import init as init_col, Fore, Style
import os
import time


letters =[" ",
        "a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q",
        "r", "s", "t", "u", "v", "w", "x", "y", "z",
        "1", "2", "3", "4", "5", "6", "7", "8", "9", "0", "+", "-", "*", "/", "<", ">",
        "!", "\"", "#", "$", "&", "(", ")", "=", "?", "¡", "'", "¿", "{", "}", "[", "]",
        ",", ";", ".", ":",
        "A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q",
        "R", "S", "T", "U", "V", "W", "X", "Y", "Z",
        "\n", "_"]


def delete_screen():
    os.system("cls")


def presentation(n: str):
    print(n)
    print(Fore.GREEN + "===============================================================")
    print(Fore.GREEN + Style.BRIGHT + "                 PyCript v 1")
    print(Fore.GREEN + "===============================================================")

init_col(autoreset=True)

notificacion = "\n"
archive_correct = True
while archive_correct:
    presentation(notificacion)

    print(Fore.YELLOW + "\n-- Seleccione el archivo que desee encriptar")
    archive_directory = input("-- ")
    archive = open(archive_directory, "r")

    try:

        archive_status = archive.readable
        if not archive_status:
            notificacion = Fore.RED + "-- El archivo no se puede leer"
            delete_screen()
        else:
            confirmation_ansewer = True
            while confirmation_ansewer: 

                print(Fore.YELLOW + f" -- Encriptar '{archive_directory}'? y/n")
                encryption_confirmation = input("-- ")

                if encryption_confirmation.lower() == "y":
                    archive_correct = False
                    confirmation_ansewer = False

                elif encryption_confirmation == "n":
                    confirmation_ansewer = False
                    delete_screen()
                    notificacion = Fore.BLUE + "-- Confirmacion cancelada"

                    


    except Exception as e:
        print(Fore.RED + Exception)

delete_screen()
presentation("\n")

print(Fore.YELLOW + "\n-- Establezca una contraseña")
password = input("")
password_p = []

for le in password:
     p = letters.index(le)
     password_p.append(p + 2)
print(password_p)
password_counter = 0


new_archive = open("encriptado.txt", "w")
new_archive.write("")
archive = open(archive_directory, "r")

secure_password = []
for num in range(0, len(password_p)):
    for gen in range(num, len(password_p)):
        secure_password.append(password_p[num] * password_p[gen])
        
print("-----------")
print(secure_password)

for li in range(0, len(archive.readlines())):

    archive = open(archive_directory, "r")
    print(archive.readlines()[li])
    archive = open(archive_directory, "r")

    for le in range(0, len(archive.readlines()[li])):
        try:
            archive = open(archive_directory, "r")
            line = archive.readlines()[li]

            letter_li = letters.index((line[le % len(letters)]))
            pass_index = letter_li + secure_password[password_counter % len(secure_password)]
            letter_pos = letters[pass_index % len(letters)]
        
        except Exception as e:
            print(f"{li}, {le}///  {e}")
            archive = open(archive_directory, "r")
            letter_ar = (archive.readlines()[li][le])
            letter_pos = letter_ar

        password_counter += 1
        new_archive = open("encriptado.txt", "a")
        new_archive.write(letter_pos)


print(Fore.BLUE + "\n Encriptado con exito")
w = input(Fore.BLUE + "===============================================")
