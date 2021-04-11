from tkinter import *

root = Tk()
root.title("Tkinter Sub menus")
root.geometry("600x500")

menu = Menu(root)
root.config(menu=menu)


def save():
    print("I made it! "*8)


# First submenu
submenu = Menu(menu, tearoff=0)
menu.add_cascade(label="File", menu=submenu)
submenu.add_command(label="New")
submenu.add_separator()
submenu.add_command(label="Open")
submenu.add_command(label="Save", command=save)
submenu.add_command(label="Close", command=quit)

# Second submenu
submenu1 = Menu(menu, tearoff=0)
menu.add_cascade(label="Edit", menu=submenu1)
submenu1.add_command(label="Delete")
submenu1.add_separator()
submenu1.add_command(label="Copy")
submenu1.add_command(label="Cut")
submenu1.add_command(label="Paste", )
submenu1.add_command(label="Find")

# 3rd submenu
submenu2 = Menu(menu, tearoff=0)
menu.add_cascade(label="View", menu=submenu2)
submenu2.add_command(label="Delete")
submenu2.add_separator()
submenu2.add_command(label="Copy")
submenu2.add_command(label="Cut")
submenu2.add_command(label="Paste", )
submenu2.add_command(label="Find")
root.mainloop()
