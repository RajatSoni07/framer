import transform
import paste
import tkinter as tk
from tkinter import filedialog
import time


root = tk.Tk()
root.withdraw()

img_pth = filedialog.askopenfilename(filetypes=[("Image File", ".jpg .jpeg .png")])

with open('tmp\imagepath.tmp','w') as writer:
    writer.write(img_pth)

transform.resizeimg()

sv_pth = filedialog.asksaveasfile(mode='w', defaultextension=".jpg")
sv_strpth = str(sv_pth)[25:]
sv_strpth = sv_strpth[::-1]
sv_strpth = sv_strpth[29:]
sv_strpth = sv_strpth[::-1]

with open('tmp\savepth.tmp','w') as writer:
    writer.write(sv_strpth)

time.sleep(4)
paste.pasteimg()