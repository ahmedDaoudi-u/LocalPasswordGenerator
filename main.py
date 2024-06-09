from tkinter import *
from tkinter import messagebox

file_name = "data.txt"

window = Tk()
window.title("Password Generator")
window.config(padx=50,pady=50)


canvas = Canvas(height=200,width=200)
logo_img = PhotoImage(file="password-28 (1).png")
canvas.create_image(100,100,image=logo_img)
canvas.grid(row=0,column=1)


Website_label = Label(text="Website:")
Website_label.grid(row=1,column=0)

email_label = Label(text="Email/Username:")
email_label.grid(row=2,column=0)

password = Label(text="Password:")
password.grid(row=3,column=0)


website_input = Entry(width=54)
website_input.grid(row=1,column=1,columnspan=2)
website_input.focus()

email_input = Entry(width=54)
email_input.grid(row=2,column=1,columnspan=2)
email_input.insert(0,"moliti129@gmail.com")

password_input = Entry(width=35)
password_input.grid(row=3,column=1)

generate_password  = Button(text="Generate Password")
generate_password.grid(row=3,column=2)


def save_data():
    website = website_input.get()
    email = email_input.get()
    password = password_input.get()


    with open(file_name,"a") as file:
        file.write(f"{website} | {email} | {password}\n")

        website_input.delete(0,END)
        password_input.delete(0,END)

    messagebox.showinfo("Success", f"Data saved to {file_name} successfully ")


add_pass = Button(text="Add",width=52,command=save_data)
add_pass.grid(row=4,column=1,columnspan=2)




window.mainloop()
