import tkinter as Tk
from tkinter import *
from tkinter import filedialog
from PIL import Image, ImageTk
from colorthief import ColorThief
import os


root = Tk()
root.title("Color picker from image")
root.geometry("800x470+100+100")
root.configure(bg="#e4e8eb")
root.resizable(False,False)

def showimage():
    global filename
    filename = filedialog.askopenfilename(
        initialdir=os.getcwd(),
        title="Select Image File",
        filetypes=(("PNG file", "*.png"),  # Fixed syntax
                   ("JPG file", "*.jpg"),
                   ("All Files", "*.*"))  # Allow all file types
    )
    
    if filename:  # Check if a file was selected
        img = Image.open(filename)
        img = img.resize((310, 270))  # Resize to fit lbl dimensions
        img = ImageTk.PhotoImage(img)

        lbl.configure(image=img, width=310, height=270)
        lbl.image = img  # Keep a reference to prevent garbage collection


def Findcolor():
    ct = ColorThief(filename)
    palette = ct.get_palette(color_count=11)

    rgb1=palette[0]
    rgb2=palette[1]
    rgb3=palette[2]
    rgb4=palette[3]
    rgb5=palette[4]
    rgb6=palette[5]
    rgb7=palette[6]
    rgb8=palette[7]
    rgb9=palette[8]
    rgb10=palette[9]

    color1=f"#{rgb1[0]:02x}{rgb1[1]:02x}{rgb1[2]:02x}"
    color2=f"#{rgb2[0]:02x}{rgb2[1]:02x}{rgb2[2]:02x}"
    color3=f"#{rgb3[0]:02x}{rgb3[1]:02x}{rgb3[2]:02x}"
    color4=f"#{rgb4[0]:02x}{rgb4[1]:02x}{rgb4[2]:02x}"
    color5=f"#{rgb5[0]:02x}{rgb5[1]:02x}{rgb5[2]:02x}"
    color6=f"#{rgb6[0]:02x}{rgb6[1]:02x}{rgb6[2]:02x}"
    color7=f"#{rgb7[0]:02x}{rgb7[1]:02x}{rgb7[2]:02x}"
    color8=f"#{rgb8[0]:02x}{rgb8[1]:02x}{rgb8[2]:02x}"
    color9=f"#{rgb9[0]:02x}{rgb9[1]:02x}{rgb9[2]:02x}"
    color10=f"#{rgb10[0]:02x}{rgb10[1]:02x}{rgb10[2]:02x}"
    
    colors.itemconfig(id1, fill=color1)
    colors.itemconfig(id2, fill=color2)
    colors.itemconfig(id3, fill=color3)
    colors.itemconfig(id4, fill=color4)
    colors.itemconfig(id5, fill=color5)

    colors2.itemconfig(id6, fill=color6)
    colors2.itemconfig(id7, fill=color7)
    colors2.itemconfig(id8, fill=color8)
    colors2.itemconfig(id9, fill=color9)
    colors2.itemconfig(id10, fill=color10)
    
    hex1.config(text=color1)
    hex2.config(text=color2)
    hex3.config(text=color3)
    hex4.config(text=color4)
    hex5.config(text=color5)
    hex6.config(text=color6)
    hex7.config(text=color7)
    hex8.config(text=color8)
    hex9.config(text=color9)
    hex10.config(text=color10)
    



#icon
image_icon = PhotoImage(file ="D:\PythonProject\Color Detection Software\color detection\icon.png")
root.iconphoto(False,image_icon)


Label(root,width=120,height=10,bg="#4272f9").pack()

#frame
frame=Frame(root,width=700,height=370,bg="#fff")
frame.place(x=50,y=50)

logo=PhotoImage(file="D:\PythonProject\Color Detection Software\color detection\logo.png")
Label(frame,image=logo,bg="#fff").place(x=10,y=10)

Label(frame,text="Color Finder",font="arial 25 bold",bg="white").place(x=100,y=20)

#color1
colors=Canvas(frame,bg="#fff",width=150,height=265,bd=0)
colors.place(x=20,y=90)

id1 = colors.create_rectangle((10,10,50,50),fill="#b8255f")
id2 = colors.create_rectangle((10,50,50,100),fill="#db4035")
id3 = colors.create_rectangle((10,100,50,150),fill="#ff9933")
id4 = colors.create_rectangle((10,150,50,200),fill="#fad000")
id5 = colors.create_rectangle((10,200,50,250),fill="#afb83b")


hex1=Label(colors,text="#b8255f",fg="#000",font="arial 12 bold",bg="white")
hex1.place(x=60,y=15)

hex2=Label(colors,text="#db4035",fg="#000",font="arial 12 bold",bg="white")
hex2.place(x=60,y=65)

hex3=Label(colors,text="#ff9933",fg="#000",font="arial 12 bold",bg="white")
hex3.place(x=60,y=115)

hex4=Label(colors,text="#fad000",fg="#000",font="arial 12 bold",bg="white")
hex4.place(x=60,y=165)

hex5=Label(colors,text="#afb83b",fg="#000",font="arial 12 bold",bg="white")
hex5.place(x=60,y=215)



#color2
colors2=Canvas(frame,bg="#fff",width=150,height=265,bd=0)
colors2.place(x=180,y=90)

id6 = colors2.create_rectangle((10,10,50,50),fill="#7ecc49")
id7 = colors2.create_rectangle((10,50,50,100),fill="#299438")
id8 = colors2.create_rectangle((10,100,50,150),fill="#6accbc")
id9 = colors2.create_rectangle((10,150,50,200),fill="#158fad")
id10 = colors2.create_rectangle((10,200,50,250),fill="#14aaf5")


hex6=Label(colors2,text="#7ecc49",fg="#000",font="arial 12 bold",bg="white")
hex6.place(x=60,y=15)

hex7=Label(colors2,text="#299438",fg="#000",font="arial 12 bold",bg="white")
hex7.place(x=60,y=65)

hex8=Label(colors2,text="#6accbc",fg="#000",font="arial 12 bold",bg="white")
hex8.place(x=60,y=115)

hex9=Label(colors2,text="#158fad",fg="#000",font="arial 12 bold",bg="white")
hex9.place(x=60,y=165)

hex10=Label(colors2,text="#afb83b",fg="#000",font="arial 12 bold",bg="white")
hex10.place(x=60,y=215)


#select image
selectimage = Frame(frame,width=340,height=350,bg="#d6dee5")
selectimage.place(x=350,y=10)

f = Frame(selectimage,bd=3,bg="black",width=320,height=280,relief=GROOVE)
f.place(x=10,y=10)

lbl = Label(f,bg="black")
lbl.place(x=0,y=0)

Button(selectimage,text="Select Image",width=12,height=1,font="arial 14 bold",command=showimage).place(x=10,y=300)
Button(selectimage,text="Find Color",width=12,height=1,font="arial 14 bold",command=Findcolor).place(x=176,y=300)




root.mainloop()