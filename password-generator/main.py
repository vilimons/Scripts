from tkinter import messagebox
from tkinter import *
from random import choice, randint, shuffle
import pyperclip
import json
# ---------------------------- PASSWORD GENERATOR ------------------------------- #


def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']


    password_letters = [choice(letters) for _ in range(randint(8, 10))]
    password_symbols = [choice(symbols) for _ in range(randint(2, 4))]
    password_numbers = [choice(numbers) for _ in range(randint(2, 4))]

    password_list = password_letters + password_symbols + password_numbers
    shuffle(password_list)

    password = "".join(password_list)
    password_entry.insert(0, password)
    pyperclip.copy(password)
    

# ---------------------------- SAVE PASSWORD ------------------------------- #

def save():

    website = website_entry.get()
    email = user_entry.get()
    password = password_entry.get()
    new_data = {
        website: {
            "email": email,
            "password": password,
        }
    }

    if len(website) == 00 or len(password) == 0 or len(email) == 0:
        messagebox.showinfo(title="Oops", message="Please make sure you haven't left any fields empty.")
    else:
        try:
            with open("GUI/password-generator/data.json", "r") as data_file:
                # Reading old data
                data = json.load(data_file)
        except FileNotFoundError:
            with open("GUI/password-generator/data.json", "w") as data_file:
                json.dump(new_data, data_file, indent=4)
        else:
            # Updating old data
            data.update(new_data)

            with open("GUI/password-generator/data.json", "w") as data_file:
                # Saving updated data
                json.dump(data, data_file, indent=4)
        finally:
            website_entry.delete(0, END)
            password_entry.delete(0, END)
            user_entry.delete(0, END)


# ----------------------- Password Finder ------------------------------ #

def find_password():
    website = website_entry.get()
    try:
        with open("GUI/password-generator/data.json") as data_file:
            data = json.load(data_file)
    except FileNotFoundError:
        messagebox.showinfo(title="Error", message="No Data File Found.")
    else:
        if website in data:
            email = data[website]["email"]
            password = data[website]["password"]
            messagebox.showinfo(title=website, message=f"Email: {email}\nPassword: {password}")
        else:
            messagebox.showinfo(text="Error", message=f"No details for {website} exists.")


    
# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager")
window.config(padx=40, pady=40)

canvas = Canvas(width=300, height=300)
img = PhotoImage(file="GUI/password-generator/logo.png")
canvas.create_image(150, 150, image=img)
canvas.grid(column=1, row=0)

# labels

website_label = Label(text="Website:",  font=("Arial", 10))
website_label.grid(column=0, row=1)

user_label = Label(text="Email:", font=("Arial", 10))
user_label.grid(column=0, row=2)

password_label = Label(text="Password:", font=("Arial", 10))
password_label.grid(column=0, row=3)

# Entries

website_entry = Entry(width=40)
website_entry.focus()
website_entry.grid(column=1, row=1)

user_entry = Entry(width=40)
user_entry.grid(column=1, row=2)

password_entry = Entry(width=40)
password_entry.grid(column=1, row=3)

# Buttons

search_button = Button(text="Search", width=10, font=("Arial", 10), command=find_password)
search_button.grid(column=2, row=1)

password_generator = Button(text="Generate Password", width=15, command=generate_password)
password_generator.grid(column=2, row=3)

add_button = Button(text="Add", width=45, font=("Arial", 10), command=save)
add_button.grid(column=1, row=4, columnspan=2)















window.mainloop()