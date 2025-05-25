from tkinter import *
from tkinter import messagebox
from PIL import Image, ImageTk

# Setting up Main Window
root = Tk()
root.title('Denomination Counter')
root.configure(bg='light blue')
root.geometry('650x400')

# Adding Image and Labels in the Main Window
upload = Image.open("app_img.jpg")
# Resize the image using resize() method
upload = upload.resize((300, 300))
image = ImageTk.PhotoImage(upload)
label = Label(root, image=image, bg='light blue')
label.place(x=180, y=20)

label1 = Label(root,
               text="Hey User! Welcome to Denomination Counter Application.",
               bg='light blue',
               font=("Arial", 12, "bold"))
label1.place(relx=0.5, y=340, anchor=CENTER)

# Function to display a messagebox and proceed
def msg():
    messagebox.showinfo("Alert", "Do you want to calculate the denomination count?")
    topwin()

# Function for opening new/top window
def topwin():
    top = Toplevel()
    top.title("Denominations Calculator")
    top.configure(bg='light grey')
    top.geometry("600x350+50+50")

    # Labels and entry fields
    label = Label(top, text="Enter total amount (₹)", bg='light grey', font=("Arial", 12))
    label.place(x=200, y=30)
    entry = Entry(top, font=("Arial", 12))
    entry.place(x=200, y=60)

    lbl = Label(top, text="Here are number of notes for each denomination", bg='light grey', font=("Arial", 11, "italic"))
    lbl.place(x=130, y=120)

    l1 = Label(top, text="₹2000 :", bg='light grey', font=("Arial", 11))
    l2 = Label(top, text="₹500  :", bg='light grey', font=("Arial", 11))
    l3 = Label(top, text="₹100  :", bg='light grey', font=("Arial", 11))

    l1.place(x=170, y=160)
    l2.place(x=170, y=190)
    l3.place(x=170, y=220)

    t1 = Entry(top, font=("Arial", 11))
    t2 = Entry(top, font=("Arial", 11))
    t3 = Entry(top, font=("Arial", 11))

    t1.place(x=250, y=160)
    t2.place(x=250, y=190)
    t3.place(x=250, y=220)

    # Calculator Function
    def calculator():
        try:
            amount = int(entry.get())
            note2000 = amount // 2000
            amount %= 2000
            note500 = amount // 500
            amount %= 500
            note100 = amount // 100

            t1.delete(0, END)
            t2.delete(0, END)
            t3.delete(0, END)

            t1.insert(END, str(note2000))
            t2.insert(END, str(note500))
            t3.insert(END, str(note100))
        except ValueError:
            messagebox.showerror("Error", "Please enter a valid number.")

    btn = Button(top, text='Calculate', command=calculator, bg='brown', fg='white', font=("Arial", 11, "bold"))
    btn.place(x=240, y=270)

    top.mainloop()

# Main Window Button
button1 = Button(root,
                 text="Let's get started!",
                 command=msg,
                 bg='brown',
                 fg='white',
                 font=("Arial", 11, "bold"))
button1.place(x=260, y=360)

# Run Mainloop
root.mainloop()