from tkinter import *
from tkinter import messagebox
import random
import pyperclip
import json

# JSON read : json.load()
# JSON Write : json.dump()
# JSON Update : json.update()

# ---------------------------- PASSWORD GENERATOR ------------------------------- #


def generate_password():
    password_input.delete(0, END)
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v',
               'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q',
               'R',
               'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    nr_letters = random.randint(8, 10)
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)

    password_letters = [random.choice(letters) for _ in range(nr_letters)]
    password_symbols = [random.choice(symbols) for _ in range(nr_symbols)]
    password_numbers = [random.choice(numbers) for _ in range(nr_numbers)]

    password_list = password_numbers + password_symbols + password_letters

    random.shuffle(password_list)

    password = "".join(password_list)
    password_input.insert(0, password)
    pyperclip.copy(password)

# ---------------------------- SAVE PASSWORD ------------------------------- #


def save():
    # Get the user input from the text box :
    website = website_input.get()
    email_username = email_username_input.get()
    user_password = password_input.get()

    new_data = {website: {
        "email": email_username,
        "password": user_password
    }}

    # Check if the user input anything!
    if len(user_password) == 0:
        messagebox.showinfo(title="Warning", message="Don't leave any of the fields empty!")
    else:
        # Open a JSON file and save the user input to said file.
        try:
            with open("data.json", "r") as file:
                # Reading old data
                data = json.load(file)
                # Updating old data with new data
                data.update(new_data)

        except (FileNotFoundError, json.decoder.JSONDecodeError):
            with open("data.json", "w") as file:
                json.dump(new_data, file, indent=4)

        else:
            # updating old data with new data
            data.update(new_data)

            with open("data.json", "w") as file:
                # Saving updated data
                json.dump(data, file, indent=4)

        # print(user_data)
        messagebox.showinfo(title="Info", message="Data saved successfully!")

        # Remove previously inputted text from the input box
        website_input.delete(0, END)
        email_username_input.delete(0, END)
        password_input.delete(0, END)

# ---------------------------- SEARCH FUNCTION ------------------------------- #


def search():
    user_search = website_input.get()
    with open("data.json", "r") as file:
        try:
            user_data = json.load(file)

        except (FileNotFoundError, json.decoder.JSONDecodeError):
            messagebox.showinfo(title="Info", message="0 user data entry found!, please add login data first.")

        else:
            # messagebox.showinfo(title="Info", message=user_data)
            if user_search in user_data:
                website = user_search
                email = user_data[user_search]["email"]
                password = user_data[user_search]["password"]
                messagebox.showinfo(title="Info",
                                    message=f"Website : {website}\nEmail : {email}\nPassword : {password}")

            else:
                messagebox.showinfo(title="Info", message=f"{user_search} login data not found, "
                                                          f"add {user_search} login data first!")

# ---------------------------- UI SETUP ------------------------------- #


# Create window
window = Tk()
window.title("MyPass Password Manager")
window.config(padx=50, pady=50)

# Create canvas
canvas = Canvas(width=200, height=200, highlightthickness=0)
# Create the image canvas
logo = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo)
# Put the canvas onto the window
canvas.grid(column=2, row=1)

# Website label and box entry
# Label
website_label = Label(text="Website:")
website_label.grid(column=1, row=2)
# Box Entry
website_input = Entry(width=35)
website_input.grid(column=2, row=2, columnspan=2, sticky="EW")
website_input.focus()

# Search Button
search_button = Button(text="Search", width=15, command=search)
search_button.grid(column=3, row=2, sticky="EW")

# Email/Username label and box entry
# Label
email_username_label = Label(text="Email/Username:")
email_username_label.grid(column=1, row=3)
# Box Entry
email_username_input = Entry(width=35)
email_username_input.grid(column=2, row=3, columnspan=2, sticky="EW")

# Change the value below to your most commonly used email for site registration, and de comment it for use
# email_username_input.insert(0, "default@defaultmail.com")

# Password label box , entry, and generate password button
# Label
password_label = Label(text="Password:")
password_label.grid(column=1, row=4)
# Box Entry
password_input = Entry(width=33)
password_input.grid(column=2, row=4)
# Generate random password button
generate_password_button = Button(text="Generate Password", command=generate_password)
generate_password_button.grid(column=3, row=4, sticky="EW")

# Add Button
add_button = Button(text="Add", width=36, command=save)
add_button.grid(column=2, columnspan=2, row=5, sticky="EW")

window.mainloop()
