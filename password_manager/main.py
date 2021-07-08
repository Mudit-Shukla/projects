from tkinter import *
from tkinter import messagebox
import password_generator
import json


#----------------------------- SEARCH DATA -------------------------------#

def search_password():
    website = website_entry.get()
    email = ""
    password = ""
    with open("data.json", 'r') as file:
        data = json.load(file)
        if website in data:
            messagebox.showinfo("Details", f"These are the requested details\n "
                                           f"website: {website}\n"
                                           f"email: {data[website]['email']}\n"
                                           f"password: {data[website]['password']}")
        else:
            messagebox.showinfo("Result","Requested details not available")

# ---------------------------- PASSWORD GENERATOR ------------------------------- #

def get_password():
    password_entry.delete(0, END)
    password = password_generator.get_password()
    password_entry.insert(0, password)

# ---------------------------- SAVE PASSWORD ------------------------------- #

def save_password():

    website = website_entry.get()
    password = password_entry.get()
    email = email_entry.get()

    new_data = {website : {"email" : email, "password" : password}}

    if len(website) == 0 or len(password) == 0 or len(email) == 0:
        messagebox.showinfo("Derails Missing", "please enter all details")
        return
    confirmation = messagebox.askokcancel("Confirm saveing password", f"Your details are \n "
                                                       f"Website: {website}\n"
                                                       f"Email: {email}\n "
                                                        f"Password: {password}\n "
                                                       f"Press OK to confirm")
    if confirmation:
        try:
            with open("data.json", "r") as data:
                old_data = json.load(data)
        except FileNotFoundError:
            with open("data.json", "w") as data:
                json.dump(new_data, data, indent = 4)
        else:
            old_data.update(new_data)
            with open ("data.json", "w") as data:
                json.dump(old_data, data, indent=4)
        finally:
            website_entry.delete(0, END)
            password_entry.delete(0, END)

def clear_feilds():
    website_entry.delete(0, END)
    email_entry.delete(0, END)
    password_entry.delete(0, END)
    website_entry.focus()

# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)

canvas = Canvas(height=200, width=200)
logo_img = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo_img)
canvas.grid(row=0, column=1)

#Labels
website_label = Label(text="Website:")
website_label.grid(row=1, column=0)
email_label = Label(text="Email/Username:")
email_label.grid(row=2, column=0)
password_label = Label(text="Password:")
password_label.grid(row=3, column=0)

#Entries
website_entry = Entry(width = 35)
website_entry.focus()
website_entry.grid(row=1, column=1, columnspan=2)
email_entry = Entry(width = 35)
email_entry.grid(row=2, column=1, columnspan=2)
password_entry = Entry()
password_entry.grid(row=3, column=1)

# Buttons
generate_password_button = Button(text="Generate Password", command = get_password)
generate_password_button.grid(row=3, column=2)
add_button = Button(text="Add", width=36, command=save_password)
add_button.grid(row=4, column=1, columnspan=2)
search_button = Button(text="Search", command = search_password)
search_button.grid(row=1, column=2)

window.mainloop()