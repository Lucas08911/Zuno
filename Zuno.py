import os
import sys
import shutil
import time

# ANSI escape codes for colors
RED = "\033[91m"
GREEN = "\033[92m"
YELLOW = "\033[93m"
CYAN = "\033[96m"
RESET = "\033[0m"

VERSION = "Zuno OS 1.2"
AUTHOR = "Lucas (Discord: lucas0891111)"
current_dir = os.getcwd()

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def boot_screen():
    clear_screen()
    print(GREEN + "Booting Zuno OS..." + RESET)
    time.sleep(1)
    print(GREEN + f"{VERSION} by {AUTHOR}" + RESET)
    time.sleep(1)
    print(GREEN + "Loading shell..." + RESET)
    time.sleep(1)
    clear_screen()

def help_menu():
    print(YELLOW + "Available commands:")
    print("  ls / dir         - List directory contents")
    print("  cd [folder]      - Change directory")
    print("  pwd              - Show current directory")
    print("  mkdir / md       - Create a new directory")
    print("  rmdir            - Remove an empty directory")
    print("  rm / del [file]  - Delete a file")
    print("  touch [file]     - Create an empty file")
    print("  cat / type       - View file contents")
    print("  echo [text]      - Print text")
    print("  clear / cls      - Clear the screen")
    print("  exit             - Quit Zuno" + RESET)

def list_dir():
    for item in os.listdir():
        print(item)

def change_dir(path):
    global current_dir
    try:
        os.chdir(path)
        current_dir = os.getcwd()
    except FileNotFoundError:
        print(RED + f"No such directory: {path}" + RESET)
    except NotADirectoryError:
        print(RED + f"{path} is not a directory" + RESET)

def make_dir(path):
    try:
        os.mkdir(path)
    except FileExistsError:
        print(RED + "Directory already exists." + RESET)
    except Exception as e:
        print(RED + f"Error: {e}" + RESET)

def remove_dir(path):
    try:
        os.rmdir(path)
    except FileNotFoundError:
        print(RED + "Directory not found." + RESET)
    except OSError:
        print(RED + "Directory not empty or cannot be removed." + RESET)

def remove_file(path):
    try:
        os.remove(path)
    except FileNotFoundError:
        print(RED + "File not found." + RESET)
    except Exception as e:
        print(RED + f"Error: {e}" + RESET)

def create_file(filename):
    try:
        open(filename, 'a').close()
    except Exception as e:
        print(RED + f"Error: {e}" + RESET)

def view_file(filename):
    try:
        with open(filename, 'r') as f:
            print(f.read())
    except FileNotFoundError:
        print(RED + "File not found." + RESET)

def zuno_shell():
    boot_screen()
    print(GREEN + f"Welcome to {VERSION}!\nType 'help' for a list of commands." + RESET)
    while True:
        try:
            cmd = input(CYAN + f"zuno:{os.getcwd()}$ " + RESET).strip()
            if not cmd:
                continue

            parts = cmd.split()
            command = parts[0]
            args = parts[1:]

            if command == "exit":
                print(GREEN + "Shutting down Zuno..." + RESET)
                break
            elif command in ["help", "?"]:
                help_menu()
            elif command in ["ls", "dir"]:
                list_dir()
            elif command == "cd":
                if args:
                    change_dir(args[0])
                else:
                    print(RED + "Usage: cd [folder]" + RESET)
            elif command == "pwd":
                print(os.getcwd())
            elif command in ["mkdir", "md"]:
                if args:
                    make_dir(args[0])
                else:
                    print(RED + "Usage: mkdir [folder]" + RESET)
            elif command == "rmdir":
                if args:
                    remove_dir(args[0])
                else:
                    print(RED + "Usage: rmdir [folder]" + RESET)
            elif command in ["rm", "del"]:
                if args:
                    remove_file(args[0])
                else:
                    print(RED + "Usage: rm [file]" + RESET)
            elif command == "touch":
                if args:
                    create_file(args[0])
                else:
                    print(RED + "Usage: touch [file]" + RESET)
            elif command in ["cat", "type"]:
                if args:
                    view_file(args[0])
                else:
                    print(RED + "Usage: cat [file]" + RESET)
            elif command == "echo":
                print(" ".join(args))
            elif command in ["clear", "cls"]:
                clear_screen()
            else:
                print(RED + f"Unknown command: {command}" + RESET)
        except KeyboardInterrupt:
            print(YELLOW + "\nUse 'exit' to quit Zuno." + RESET)
        except Exception as e:
            print(RED + f"Error: {e}" + RESET)

if __name__ == "__main__":
    zuno_shell()

