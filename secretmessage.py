#project
from tkinter import messagebox, simpledialog, Tk
from random import choice
def is_even(number):
    return number % 2 == 0
def get_even_letters(message):
    even_letters = []
    for counter in range(0, len(message)):
        if is_even(counter):
            even_letters.append(message[counter])
    return even_letters
def get_odd_letters(message):
    odd_letters = []
    for counter in range(0, len(message)):
        if not is_even(counter):
            odd_letters.append(message[counter])
    return odd_letters
def get_task():
    task = simpledialog.askstring("Task", "Do you want to encrypt or decrypt?")
    return task
def get_message():
    message = simpledialog.askstring("Message", "Enter the secret message: ")
    return message
root = Tk()
def encrypt(message):
    encrypted_list = []
    fake_letters = ["a", "x", "p", "v", "y", "q", "k", "w", "r", "e", "s"]
    for counter in range(0, len(message)):
        encrypted_list.append(message[counter])
        encrypted_list.append(choice(fake_letters))
    new_message = " ".join(encrypted_list)
    return new_message
def decrypt(message):
    even_letters = get_even_letters(message)
    new_message = " ".join(even_letters)
    return new_message
while True:
    task = get_task()
    if task == "encrypt":
        message = get_message()
        encrypted = encrypt(message)
        messagebox.showinfo(" Encryption of secret message is: ", encrypted)
    elif task == "decrypt":
        message = get_message()
        decrypted = decrypt(message)
        messagebox.showinfo("Decryption of the secret message is: ", decrypted)
    else:
        break
root.mainloop()

    
