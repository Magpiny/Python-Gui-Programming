from tkinter import *

app = Tk()


def close():
    app.destroy()
    # quit()


def show_value():
    print(radiobtn_value.get())


def delete_items():
    my_entry.delete(0, END)
    my_entry1.delete(0, END)
    print(my_entry1.grid_size())


app.geometry("400x350")
app.title("App1")
# my variables
radiobtn_value = IntVar()
# Button widget
quitButton = Button(app, text="CLOSE", fg="black", bg="yellow", command=close)

# Radio button : Only one is selected at a time
lbl_radio = Label(app, text="Select your favourite sport", bg="#fed")
radio1 = Radiobutton(app, text="Soccer", value=1, variable=radiobtn_value)
radio2 = Radiobutton(app, text="Basketball", value=2, variable=radiobtn_value)
radio3 = Radiobutton(app, text="Athletics", value=3, variable=radiobtn_value)
radio4 = Radiobutton(app, text="Boxing", value=4, variable=radiobtn_value)
btnValue = Button(app, text="Show btn Value", bg="green", command=show_value)

# Entry : Used to capture user data as in forms and are labeled using Label widgets
username = Label(app, text="Username", bg="#fe55ab")
my_entry = Entry(app, bg="#ffe")
password = Label(app, text="Password", bg="#fe55ab")
my_entry1 = Entry(app, bg="#fe9")
clear_entry = Button(app, text="CLEAR ENTRY", fg="red", command=delete_items)

# Pack all your widgets to the main application window
lbl_radio.pack(pady=15)
radio1.pack()
radio3.pack()
radio4.pack()
radio2.pack(pady=5)
btnValue.pack(pady=5)

username.place(x=50, y=184)
my_entry.place(x=120, y=184)
password.place(x=50, y=220)
my_entry1.place(x=120, y=220)
clear_entry.place(x=120, y=240)
quitButton.pack(fill="y", side="bottom", pady="10")
app.mainloop()
