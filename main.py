from tkinter import *
from tkinter import messagebox
import random
import pyperclip
import json
#_____________________________ Search ____________________________________________#
def search():

    try:
        with open("My_data.json","r") as f:
            data = json.load(f)
            web = e1_website.get()

    except FileNotFoundError:
        messagebox.showinfo(title="ERROR",message="File not found")
    else:
        if web in data:
            email = data[web]["email"]
            passw = data[web]["password"]
            print(data[e1_website.get()])
            messagebox.showinfo(title=f"{e1_website.get()}",message=f"Email :{email}\nPassword :{passw}")
        else:
            messagebox.showinfo(title="Sorry",message=f"No info found related to {web}.\nPlease check for spelling and check for case sensitive ")

# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def password_generator():
    e3_password.delete(0,END)
    # Password Generator Project
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
               'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    nr_letters = random.randint(8, 10)
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)

    password_list = []

    for char in range(nr_letters):
        password_list.append(random.choice(letters))

    for char in range(nr_symbols):
        password_list += random.choice(symbols)

    for char in range(nr_numbers):
        password_list += random.choice(numbers)

    random.shuffle(password_list)

    password = ""
    for char in password_list:
        password += char

    e3_password.insert(END, password)
    pyperclip.copy(password)

# ---------------------------- SAVE PASSWORD ------------------------------- #



def addded():
    WEB = e1_website.get()
    EMAIL = e2_email.get()
    PASSWORD = e3_password.get()

    new_data = {
        WEB: {
            "email": EMAIL,
            "password":PASSWORD,
        }
    }

    if len(e1_website.get())== 0 or len(e3_password.get()) == 0 or len(e2_email.get()) == 0:
        messagebox.showinfo(title="Warning", message="One of the field is empty" )
    else:
        try:
            with open("My_data.json", "r") as f:

            #json.dump(new_data, f,indent=4)  #data should be openned as a {open("mydata.json","a")}
                data = json.load(f)  #reads the data   {open("mydata.json","r")}
                data.update(new_data)
            with open("My_data.json","w") as f:
                json.dump(data,f,indent=4)
        except FileNotFoundError:
            with open("My_data.json","w") as f:
                json.dump(new_data,f,indent=4)
        finally:
            e1_website.delete(0, END)
            e3_password.delete(0, END)
            e1_website.focus()
            messagebox.showinfo(title=f"{WEB}", message=f"The entry has been saved successful.\nEmail: {EMAIL} \nPasword: {PASSWORD}")




# ---------------------------- UI SETUP ------------------------------- #

win=Tk()
win.title("Password Manager")
# win.minsize(width=240,height=240)
win.config(pady=50,padx=50)


canva = Canvas(width=200, height=200)
logo_img = PhotoImage(file="logo.png")

canva.create_image(100,100,image=logo_img)
canva.grid(column=1,row=0)

#label
l1_website = Label(text="Website:")
l1_website.grid(column=0, row=1)
e1_website = Entry(width=35)
e1_website.grid(column=1,row=1,columnspan=1,sticky="EW")
e1_website.focus()

l2_email = Label(text="Email/Username: ")
l2_email.grid(column=0,row=2)
e2_email = Entry(width=35)
e2_email.insert(0, "abhilaksh2004sh@gmail.com")
e2_email.grid(column=1, row=2, columnspan=2,sticky="EW")

l3_password = Label(text="Password: ")
l3_password.grid(column=0,row=3)

e3_password = Entry()
e3_password.grid(column=1,row=3,sticky="EW")


b1 = Button(text="Generate Password", command=password_generator)
b1.grid(column=2,row=3)

b2 = Button(text="Add", width=36,command=addded)
b2.grid(column=1, row=4, columnspan=2,sticky="EW")

b3 = Button(text="Search",command=search)
b3.grid(column=2, row=1, sticky="EW")


win.mainloop()
