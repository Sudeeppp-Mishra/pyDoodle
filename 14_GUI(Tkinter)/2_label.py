# label = an area widget that holes text and/or image within a window

from tkinter import *

window = Tk()

window.geometry('320x320')

# label = Label(window, 
#               text="Hello World", 
#               font=('Times New Roman', 20, 'bold'), 
#               fg='black', 
#               bg='#00FF00',
#               relief=RAISED,
#               bd=10,
#               padx=20,
#               pady=20) # relief is for border and bd is border size another relief is SUNKEEN as well and many more, padding is space between text and the border
# label.pack() # adding to window

#OR

#label.place(x=0, y=0) # it is another way to place the label in window and we can even give co-ordinates for proper placement

# photo label -> for this we need to create Photo Image at first

photo = PhotoImage(file="/Users/sudeepdemishra/Documents/Random.py/14_GUI(Tkinter)/logo.png")

# label1 = Label(window,
#                image=photo,
#                bg='#00FF00')
# label1.pack()

# label with photo and text both
label2 = Label(window, 
              text="Hello World", 
              font=('Times New Roman', 20, 'bold'), 
              relief=RAISED,
              bg='white',
              bd=10,
              padx=20,
              pady=20,
              image=photo,
              compound='top')
label2.pack()

window.mainloop()