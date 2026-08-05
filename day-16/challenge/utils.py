import subprocess

def clear():
    subprocess.run(['cls'], shell=True)

def message(message="Please, enter a valid entry."):
    clear()
    print(message)

def customMessage(message):
    clear()
    print(message)

def wait():
    while input("Enter 0 to exit: ") != "0":
        pass
    clear()
