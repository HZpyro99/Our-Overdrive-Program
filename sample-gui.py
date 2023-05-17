import tkinter as tk
from PIL import Image, ImageTk

def quitGame(event):
    window.destroy()

def playgame(event):
    #creates the new background(subject to change duue to plot/lack of assets)
    bgclass = ImageTk.PhotoImage(Image.open("clas.png"))
    bgcl = canvas.create_image(0,0, image=bgclass, anchor=tk.NW)

    dxbox = ImageTk.PhotoImage(Image.open("Classro.png"))
    dxDiag = canvas.create_image(0,350, image=dxbox, anchor=tk.NW)

    canvas.itemconfigure(bg, state='hidden')
    canvas.itemconfigure(playButton, state='hidden')
    canvas.itemconfigure(AboutBtn, state='hidden')
    canvas.itemconfigure(quitButton, state='hidden')
    canvas.itemconfigure(bgcl, state="show")
    canvas.itemconfigure(dxDiag, state="show")

def aboutbutton(event):
    # Create a label with a transparent background
   
    canvas.create_text(650,300,text = "This is the about page",font=("Arial",31))
    canvas.create_text(650,350,text="Developers",font=("Arial",25))
    canvas.create_text(650,400,text="Ivan Klein Alegre & John Rafael Alipio",font=("Arial",20))
    canvas.create_text(650,450,text="Artists",font=("Arial",25))
    canvas.create_text(650,500,text="Shizukana,Knash,Diyan",font=("Arial",20))

    # Hide the buttons by setting their state to 'hidden'
    canvas.itemconfigure(playButton, state='hidden')
    canvas.itemconfigure(AboutBtn, state='hidden')
    canvas.itemconfigure(quitButton, state='hidden')

    NewquitImage = ImageTk.PhotoImage(Image.open("Exit.png"))
    NewquitButton = canvas.create_image(650, 600, image=NewquitImage)
    canvas.tag_bind(NewquitButton, "<Button-1>", quitGame)
    canvas.itemconfigure(NewquitButton,state='show')


window = tk.Tk()
window.geometry("1300x731")
window.title("Our Overdrive Program")
window.resizable(False,False)

canvas = tk.Canvas(window, width = 1300, height = 731)
canvas.pack()

# Creating background
bgImage = ImageTk.PhotoImage(Image.open("bg2.png")) 
bg = canvas.create_image(0, 0, image=bgImage, anchor=tk.NW)

# Creating button which supports png transparency
playGame = ImageTk.PhotoImage(Image.open("Play.png"))
playButton = canvas.create_image(650, 300, image=playGame)
canvas.tag_bind(playButton,"<Button-1>", playgame)

About = ImageTk.PhotoImage(Image.open("About.png"))
AboutBtn = canvas.create_image(650,400, image=About)
canvas.tag_bind(AboutBtn,"<Button-1>", aboutbutton)

quitImage = ImageTk.PhotoImage(Image.open("Exit.png"))
quitButton = canvas.create_image(650, 500, image=quitImage)
canvas.tag_bind(quitButton, "<Button-1>", quitGame)

window.mainloop()