from colorama import init as init_col, Fore
import time
init_col(autoreset=True)

print(Fore.GREEN + "===========================================================")
print(Fore.GREEN + "                     PyDesCript v 0.1")
print(Fore.GREEN + "===========================================================")
print("Seleccione el archivo que desee desencriptar")

archive_directory = input("")
archive = open(archive_directory, "r")

try:
    archive_status = archive.readable
    if not archive_status:
        print("Ha ocurrido un error")
        time.sleep(1)
    else:
        print(Fore.YELLOW + f"Desencriptar '{archive_directory}'?")
except Exception as e:
    print(Fore.RED + Exception)

print("\nEscribe la contraseña")
password = input("")
password_p = []

letters = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q",
           "r", "s", "t", "u", "v", "w", "x", "y", "z",
           "1", "2", "3", "4", "5", "6", "7", "8", "9", "0", "+", "-", "*", "/", "<", ">",
            "!", "\"", "#", "$", "&", "(", ")", "=", "?", "¡", "'", "¿", "{", "}", "[", "]",
            ",", ";", ".", ":"]

for le in range(len(password)):
     p = letters.index(password[le])
     password_p.append(p)
print(password_p)


new_archive = open("Des_encripter.txt", "w")
new_archive.write("")

archive = open(archive_directory, "r")

password_counter = 0

for li in range(0, len(archive.readlines())):

    archive = open(archive_directory, "r")
    print(archive.readlines()[li])
    archive = open(archive_directory, "r")

    for le in range(0, len(archive.readlines()[li])):
        try:
            archive = open(archive_directory, "r")
            letter_ar = letters.index((archive.readlines()[li][le % len(letters)]).lower())
            pass_index = letter_ar - password_p[ password_counter % len(password_p) ]
            letter_pos = letters[pass_index % len(letters)]
        
        except Exception as e:
            print(f"{li}, {le}///  {e}")
            archive = open(archive_directory, "r")
            letter_ar = (archive.readlines()[li][le]).lower()
            letter_pos = letter_ar

        password_counter += 1
        new_archive = open("Des_encripter.txt", "a")
        new_archive.write(letter_pos)