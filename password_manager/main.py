from tkinter import *
from tkinter import messagebox
import password_generator

# ---------------------------- PASSWORD GENERATOR ------------------------------- #

def get_password():
    password_entry.delete(0, END)
    password = password_generator.get_password()
    password_entry.insert(0, password)

# ---------------------------- SAVE PASSWORD ------------------------------- #

def save_password():

    if len(website_entry.get()) == 0 or len(password_entry.get()) == 0 or len(email_entry.get()) == 0:
        messagebox.showinfo("Derails Missing", "please enter all details")
        return
    confirmation = messagebox.askokcancel("Confirm saveing password", f"Your details are \n "
                                                       f"Website: {website_entry.get()}\n"
                                                       f"Email: {email_entry.get()}\n "
                                                        f"Password: {password_entry.get()}\n "
                                                       f"Press OK to confirm")
    if confirmation:
        with open("data.txt", "a") as file:
            file.write(f"{website_entry.get()} | {email_entry.get()} | {password_entry.get()}")
            file.write("\n")
        clear_feilds()

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
website_entry = Entry(width=35)
website_entry.focus()
website_entry.grid(row=1, column=1, columnspan=2)
email_entry = Entry(width=35)
email_entry.grid(row=2, column=1, columnspan=2)
password_entry = Entry(width=21)
password_entry.grid(row=3, column=1)

# Buttons
generate_password_button = Button(text="Generate Password", command = get_password)
generate_password_button.grid(row=3, column=2)
add_button = Button(text="Add", width=36, command=save_password)
add_button.grid(row=4, column=1, columnspan=2)

window.mainloop()