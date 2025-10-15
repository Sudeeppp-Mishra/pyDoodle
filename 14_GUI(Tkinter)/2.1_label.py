from tkinter import *
from PIL import Image, ImageTk

window = Tk()
window.geometry('320x320')

# Open and resize image
img = Image.open("/Users/sudeepdemishra/Documents/Random.py/14_GUI(Tkinter)/logo.png")
img = img.resize((100, 100))
photo = ImageTk.PhotoImage(img)

# Label with text and image
label2 = Label(window, 
               text="Hello World", 
               font=('Times New Roman', 20, 'bold'), 
               relief=RAISED,
               fg='red',
               bg='white',
               bd=10,
               padx=20,
               pady=20,
               image=photo,
               compound='bottom')

label2.image = photo  # keep reference
label2.pack()

window.mainloop()