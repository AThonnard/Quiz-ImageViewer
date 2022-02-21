from tkinter import *
from PIL import Image, ImageTk
root = Tk()
root.title("Image viewer Group 1")
root.resizable(0, 0)
# create frame
frame=Frame(root, width=600, height=500, bg='white', relief=GROOVE, bd=2)
frame.pack(padx=10, pady=10)
# create thumbanials of all images
img1 = Image.open('Paris.jpg')
img1.thumbnail((550, 450))
img2 = Image.open('Mumbai.jpg')
img2.thumbnail((550, 450))
img3 = Image.open('Tokio.jpg')
img3.thumbnail((550, 450))
img4 = Image.open('NewYorkStreets.jpg')
img4.thumbnail((550, 450))

image1 = ImageTk.PhotoImage(img1)
image2 = ImageTk.PhotoImage(img2)
image3 = ImageTk.PhotoImage(img3)
image4 = ImageTk.PhotoImage(img4)

# create list of images
images = [image1, image2, image3, image4]
# configure the image to the Label in frame
i = 0
image_label = Label(frame, image=images[i])
image_label.pack()
# create functions to display
# previous an next images
def previous():
    global i
    i = i - 1
    try:
        image_label.config(image=images[i])
    except:
        i = 0
        previous()
def next():
    global i
    i = i + 1
    try:
        image_label.config(image=images[i])
    except:
        i = -1
        next()
# create buttons
btn1 = Button(root, text="<<", bg='lightblue', fg='black', font=('ariel 15 bold'), relief=GROOVE, command=previous)
btn1.pack(side=LEFT, padx=60, pady=5)
btn2 = Button(root, text="Exit", width=5, bg='lightblue', fg='black', font=('ariel 15 bold'), relief=GROOVE, command=root.destroy)
btn2.pack(side=LEFT, padx=60, pady=5)
btn3 = Button(root, text=">>", bg='lightblue', fg='black', font=('ariel 15 bold'), relief=GROOVE, command=next)
btn3.pack(side=LEFT, padx=60, pady=5)

root.mainloop()
