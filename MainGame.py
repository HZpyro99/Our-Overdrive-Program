import tkinter as tk
from PIL import Image, ImageTk
import pygame
import sqlite3
import json

class SaveLoad:
    #initializes the database
    def __init__(self):
        self.db = sqlite3.connect('data.db')
        self.cursor = self.db.cursor()
        self.cursor.execute('CREATE TABLE IF NOT EXISTS screen_position (x INT, y INT)')
        self.db.commit()
    #Saves the screen position into a database and a json file
    def save_screen_position(self, x, y):
        self.cursor.execute('INSERT INTO screen_position VALUES (?, ?)', (x, y))
        self.db.commit()
        with open('data.json', 'w') as f:
            json.dump({'x': x, 'y': y}, f)

    #Loads the save file
    def load_screen_position(self):
        self.cursor.execute('SELECT * FROM screen_position')
        result = self.cursor.fetchone()
        if result:
            x, y = result
        else:
            x, y = 0, 0
        try:
            with open('data.json', 'r') as f:
                data = json.load(f)
            x, y = data['x'], data['y']
        except FileNotFoundError:
            pass
        return x, y

    #Closes  the database
    def __del__(self):
        self.db.close()


class OverdriveProgram(SaveLoad):
    def __init__(self, window):
        self.window = window
        self.window.geometry("1600x900")
        self.window.title("Our Overdrive Program")
        self.window.resizable(False,False)
        window.attributes('-fullscreen',True)

        self.save_load = SaveLoad()
          # Get the current screen position
        self.x, self.y = self.save_load.load_screen_position()

        # Set the window position to the saved position
        self.window.geometry(f'+{self.x}+{self.y}')
        
        #sets the counter for the intro scenes
        self.counter=0
        
        #plays the music in a loop
        pygame.mixer.init()
        pygame.mixer.music.load("The Monuments and Tunnels in Goa and Hampi - Bail Bonds.mp3")
        pygame.mixer.music.play(-1)

        #initializes the canvas
        self.canvas = tk.Canvas(self.window, width=1600, height=900)
        self.canvas.pack()

        #sets the main menu background
        self.bgImage = ImageTk.PhotoImage(Image.open("Main_Page.png"))
        self.bg = self.canvas.create_image(0, 0, image=self.bgImage, anchor=tk.NW)

        self.SceneCollection()  # call this function to set self.Collection

        #Creates the Play button
        self.playGame = ImageTk.PhotoImage(Image.open("Play.png"))
        self.playButton = self.canvas.create_image(800, 300, image=self.playGame)
        self.canvas.tag_bind(self.playButton, "<Button-1>", self.play_game)

        #Creates the load button
        self.loadg = ImageTk.PhotoImage(Image.open("load.png"))
        self.loadButton = self.canvas.create_image(800, 400, image=self.loadg)
        self.canvas.tag_bind(self.loadButton, "<Button-1>", self.load_position)

        #Creates the about button
        self.Aboutimg = ImageTk.PhotoImage(Image.open("About.png"))
        self.Aboutbtn = self.canvas.create_image(800, 500, image=self.Aboutimg)
        self.canvas.tag_bind(self.Aboutbtn, "<Button-1>", self.about_button)

        #Creates the quit button
        self.quitImage = ImageTk.PhotoImage(Image.open("Exit.png"))
        self.quitButton = self.canvas.create_image(800, 600, image=self.quitImage)
        self.canvas.tag_bind(self.quitButton, "<Button-1>", self.quit_game)

    def save_position(self):
        # Get the current screen position
        x, y = self.master.winfo_x(), self.master.winfo_y()

        # Save the screen position
        self.save_load.save_screen_position(x, y)

    def load_position(self):
        # Load the saved screen position
        x, y = self.save_load.load_screen_position()

        # Set the window position to the saved position
        self.master.geometry(f'+{x}+{y}')

    #Main menu(Main Menu button found throuughout the game is linked here)
    def Main_M(self, event):
        self.bgImage = ImageTk.PhotoImage(Image.open("Main_Page.png"))
        self.bg = self.canvas.create_image(0, 0, image=self.bgImage, anchor=tk.NW)

        self.playGame = ImageTk.PhotoImage(Image.open("Play.png"))
        self.playButton = self.canvas.create_image(800, 300, image=self.playGame)
        self.canvas.tag_bind(self.playButton, "<Button-1>", self.play_game)

        self.loadg = ImageTk.PhotoImage(Image.open("load.png"))
        self.loadButton = self.canvas.create_image(800, 400, image=self.loadg)
        self.canvas.tag_bind(self.loadButton, "<Button-1>", self.load_position)

        self.Aboutimg = ImageTk.PhotoImage(Image.open("About.png"))
        self.Aboutbtn = self.canvas.create_image(800, 500, image=self.Aboutimg)
        self.canvas.tag_bind(self.Aboutbtn, "<Button-1>", self.about_button)
    
        self.quitImage = ImageTk.PhotoImage(Image.open("Exit.png"))
        self.quitButton = self.canvas.create_image(800, 600, image=self.quitImage)
        self.canvas.tag_bind(self.quitButton, "<Button-1>", self.quit_game)

    #Closes the game
    def quit_game(self,event):
        pygame.mixer.music.stop()
        self.window.destroy()

    #About Window
    def about_button(self, event):
        About_pg = ImageTk.PhotoImage(Image.open("About_Page.png"))
        self.canvas.create_image(0,0,image = About_pg, anchor=tk.NW)

        self.canvas.itemconfigure(self.playButton, state='hidden')
        self.canvas.itemconfigure(self.Aboutbtn, state='hidden')
        self.canvas.itemconfigure(self.quitButton, state='hidden')

        Main = ImageTk.PhotoImage(Image.open("MM.png"))
        MainB = self.canvas.create_image(800, 750, image=Main)
        self.canvas.tag_bind(MainB, "<Button-1>", self.Main_M)
        self.canvas.itemconfigure(MainB, state='show')

    #Method where all the intro scenes are stored in a list
    def SceneCollection(self):
        self.i1 = ImageTk.PhotoImage(Image.open("5.png"))
        self.i2 = ImageTk.PhotoImage(Image.open("6.png"))
        self.i3 = ImageTk.PhotoImage(Image.open("7.png"))
        self.i4 = ImageTk.PhotoImage(Image.open("8.png"))
        self.i5 = ImageTk.PhotoImage(Image.open("9.png"))
        self.i6 = ImageTk.PhotoImage(Image.open("10.png"))
        self.i7 = ImageTk.PhotoImage(Image.open("11.png"))
        self.i8 = ImageTk.PhotoImage(Image.open("12.png"))
        self.i9 = ImageTk.PhotoImage(Image.open("13.png"))
        self.i10 = ImageTk.PhotoImage(Image.open("14.png"))
        self.i11 = ImageTk.PhotoImage(Image.open("15.png"))
        self.i12 = ImageTk.PhotoImage(Image.open("16.png"))
        self.i13 = ImageTk.PhotoImage(Image.open("17.png"))
        self.i14 = ImageTk.PhotoImage(Image.open("18.png"))
        self.i15 = ImageTk.PhotoImage(Image.open("19.png"))
        self.i16 = ImageTk.PhotoImage(Image.open("20.png"))
        self.i17 = ImageTk.PhotoImage(Image.open("21.png"))

        self.Collection=[self.i1,self.i2,self.i3,self.i4,self.i4,self.i5,self.i6,self.i7,self.i8
                         ,self.i9,self.i10,self.i11,self.i12,self.i13,self.i14,self.i15,self.i16,
                         self.i17]

    #Creates the first playable sequence, the Intro scenes
    def play_game(self,event):
        self.canvas.create_image(0,0,image=self.Collection[self.counter],anchor=tk.NW)

        Main = ImageTk.PhotoImage(Image.open("MM.png"))
        MainB = self.canvas.create_image(100, 50, image=Main)
        self.canvas.tag_bind(MainB, "<Button-1>", self.Main_M)

        Save = ImageTk.PhotoImage(Image.open("save.png"))
        savebtn = self.canvas.create_image(100,100,image=Save)
        self.canvas.tag_bind(savebtn,'<Button-1>',self.save_position)

        Next = ImageTk.PhotoImage(Image.open("Next.png"))
        NextB = self.canvas.create_image(1450, 800, image=Next)
        self.canvas.tag_bind(NextB, "<Button-1>", self.next_scene)

        self.canvas.itemconfigure(MainB, state="show")
        self.canvas.itemconfigure(savebtn, state="show")
        self.canvas.itemconfigure(NextB, state="show")

    #Linked to the next button. It increments a counter such that the next scene will be played
    def next_scene(self, event):
        self.counter += 1
        if self.counter >= len(self.Collection):
            self.decide()
        self.canvas.create_image(0,0,image=self.Collection[self.counter],anchor=tk.NW)
        
        #Main menu Button
        Main = ImageTk.PhotoImage(Image.open("MM.png"))
        MainB = self.canvas.create_image(100, 50, image=Main)
        self.canvas.tag_bind(MainB, "<Button-1>", self.Main_M)

        #Saves the current screen position when clicked
        Save = ImageTk.PhotoImage(Image.open("save.png"))
        savebtn = self.canvas.create_image(100,100,image=Save)
        self.canvas.tag_bind(savebtn,'<Button-1>',self.save_position)

        #Next Button
        Next = ImageTk.PhotoImage(Image.open("Next.png"))
        NextB = self.canvas.create_image(1450, 800, image=Next)
        self.canvas.tag_bind(NextB, "<Button-1>", self.next_scene)

        self.canvas.itemconfigure(MainB, state="show")
        self.canvas.itemconfigure(savebtn, state="show")
        self.canvas.itemconfigure(NextB, state="show")

    #Part where the user will decide wether Python or C++ is their language to practice
    def decide(self):
        self.deImg = ImageTk.PhotoImage(Image.open("22.png"))
        self.canvas.create_image(0,0,image=self.deImg,anchor=tk.NW)

        Main = ImageTk.PhotoImage(Image.open("MM.png"))
        MainB = self.canvas.create_image(100, 50, image=Main)
        self.canvas.tag_bind(MainB, "<Button-1>", self.Main_M)

        Save = ImageTk.PhotoImage(Image.open("save.png"))
        savebtn = self.canvas.create_image(100,100,image=Save)
        self.canvas.tag_bind(savebtn,'<Button-1>',self.save_position)

        pyimg = ImageTk.PhotoImage(Image.open("py.png"))
        pybtn = self.canvas.create_image(600, 400, image=pyimg)
        self.canvas.tag_bind(pybtn, '<Button-1>', self.py_button)

        cpImg = ImageTk.PhotoImage(Image.open("cp.png"))
        cpbtn = self.canvas.create_image(700, 400, image=cpImg)
        self.canvas.tag_bind(cpbtn, '<Button-1>', self.cp_button)

        self.canvas.itemconfigure(MainB, state="show")
        self.canvas.itemconfigure(savebtn, state="show")
        self.canvas.itemconfigure(pybtn,state="show")
        self.canvas.itemconfigure(cpbtn,state="show")

    def py_button(self, event):
        pass

    def cp_button(self, event):
        pass

if __name__ == "__main__":
    window = tk.Tk()
    overdrive_program = OverdriveProgram(window)
    window.mainloop()