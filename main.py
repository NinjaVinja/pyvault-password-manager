from tkinter import *
from tkinter import messagebox
import random
import json

# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v',
               'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R',
               'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    nr_letters = random.randint(8, 10)
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)

    password_letters = [random.choice(letters) for _ in range(nr_letters)]
    password_symbols = [random.choice(symbols) for _ in range(nr_symbols)]
    password_numbers = [random.choice(numbers) for _ in range(nr_numbers)]

    password_list = password_letters + password_symbols + password_numbers
    random.shuffle(password_list)

    password = "".join(password_list)
    password_entry.insert(0, password)
# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
    website = website_entry.get()
    email = email_entry.get()
    password = password_entry.get()
    new_data = {
        website: {
            "email": email,
            "password": password
        }
    }
    if len(email) == 0 or len(password) == 0 or len(website) == 0:
        messagebox.showinfo("Error", "Please enter all required information")
    else:
        try:
            with open("data.json", "r") as data_file:
                    # json.dump(new_data, file, indent=4)
                    data = json.load(data_file)
        except FileNotFoundError:
            with open("data.json", "w") as data_file:
                json.dump(new_data,data_file,indent=4)
        else:
            data.update(new_data)
            with open("data.json", "w") as data_file:
                json.dump(data,data_file,indent=4)
        finally:
                website_entry.delete(0,END)
                password_entry.delete(0,END)
                email_entry.delete(0,END)

# ---------------------------- SEARCH ------------------------------- #
def find_password():
    website = website_entry.get()
    try:
        with open("data.json", "r") as data_file:
            data = json.load(data_file)
    except FileNotFoundError:
        messagebox.showinfo("Error", "No data found")
    else:
        if website in data:
            email = data[website]["email"]
            password = data[website]["password"]
            messagebox.showinfo(website, f"Email: {email}\n Password: {password}")
        else:
            messagebox.showinfo("Error",  f"No details for {website} exits.")
# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)

canvas = Canvas(height=200, width=200)
logo = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo)
canvas.grid(row=0, column=1)

#Labels
website_label = Label(text="Website:")
website_label.grid(row=2, column=0, sticky="e", padx=(0, 10), pady=8)
email_label = Label(text="Email/Username:")
email_label.grid(row=3, column=0, sticky="e", padx=(0, 10), pady=8)
password_label = Label(text="Password:")
password_label.grid(row=4, column=0, sticky="e", padx=(0, 10), pady=8)

#Entries
website_entry = Entry(width=32)
website_entry.grid(row=2, column=1, pady=8, sticky="w")
website_entry.focus()
email_entry = Entry(width=32)
email_entry.grid(row=3, column=1, columnspan=2, pady=8, sticky="w")
email_entry.insert(0,"example@gmail.com")
password_entry = Entry(width=32)
password_entry.grid(row=4, column=1, pady=8, sticky="w")

# ---------------------------- BUTTONS ------------------------------- #
#Generate_password_button
generate_password_button = Button(text="Generate Password", width=14, command=generate_password)
generate_password_button.grid(row=4, column=2, padx=(10, 0), pady=8, sticky="w")
#add_button
add_button = Button(text="Add", width=36,command=save)
add_button.grid(row=5, column=0, columnspan=3, pady=(20, 0), sticky="ew")
#Search_button
search_button = Button(text="Search", command=find_password)
search_button.grid(row=2, column=2, padx=(10, 0), pady=8, sticky="w")



window.mainloop()
