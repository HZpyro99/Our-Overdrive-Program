# import tkinter as tk
# from PIL import Image, ImageTk


# class Scenes:
#     def __init__(self,root):
#         self.root = root
#         self.root.geometry("1600x900")
#         self.root.title("Our Overdrive Program")
#         self.root.resizable(False,False)
#         self.root.attributes('-fullscreen',True)

#         self.canvas = tk.Canvas(self.window, width=1600, height=900)
#         self.canvas.pack()


#     def Scene1(self):
#         self.scene = ImageTk.PhotoImage(Image.open("5.png"))
#         self.canvas.create_image(0, 0, image=self.scene, anchor=tk.NW)

       


#     def Scene2(self):
#         self.scene = ImageTk.PhotoImage(Image.open("6.png"))
#         self.canvas.create_image(0, 0, image=self.scene, anchor=tk.NW)

#         Next = ImageTk.PhotoImage(Image.open("next.png"))
#         NextB = self.canvas.create_image(1450,800,image=Next)
#         self.canvas.tag_bind(NextB, '<Button-1>',self.Scene3)

#         Main = ImageTk.PhotoImage(Image.open("MM.png"))
#         MainB = self.canvas.create_image(100, 50, image=Main)

#         Save = ImageTk.PhotoImage(Image.open("save.png"))
#         savebtn = self.canvas.create_image(100,100,image=Save)

#         # self.canvas.itemconfigure(NextB,state="show")
#         # self.canvas.itemconfigure(MainB,state="show")
#         # self.canvas.itemconfigure(savebtn,state="show")


#     def Scene3(self):
#         self.scene = ImageTk.PhotoImage(Image.open("7.png"))
#         self.canvas.create_image(0, 0, image=self.scene, anchor=tk.NW)
#         self.canvas.itemconfigure(self.scene,state="show")


# root=tk.Tk()
# scene = Scenes(root)
# root.mainloop()
