import tkinter as tk
from PIL import ImageTk, Image

window = tk.Tk()


frame1 = tk.Label(text='Armature Defect Detector',master=window, height=5, bg="grey",font=('Helvatical bold',20))
frame1.pack(fill=tk.X)

label1 = tk.Label(window, text = "Red / Green", fg = 'black', bg = 'beige',font=('Helvatical bold',20)) 
label2 = tk.Label(window, text = "Type of defect", fg = 'black', bg = 'beige',font=('Helvatical bold',20)) 
label1.place(x = 1200,y = 450) 
label2.place(x = 1200 , y=750) 
text2_field = tk.Text(window, height = 5, width = 25, font = "lucida 13")
image = Image.open("API\input.jpg")
image=image.resize((600,600))
photo = ImageTk.PhotoImage(image)
img_label = tk.Label(image=photo)
img_label.image = photo
img_label.pack(side='left',padx=200,pady=100)
window.mainloop()   