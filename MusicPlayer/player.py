from tkinter import *

app = Tk()
app.title("Magpiny Music Player")
app.geometry("700x580")


# close button func
def close():
    app.destroy()


quit = Button(app, text="CLOSE", bg="yellow", command=close)

# pack all your widgets here
quit.pack(side="bottom", ipadx=10)
app.mainloop()
