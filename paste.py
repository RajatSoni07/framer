from PIL import Image, ImageDraw, ImageFilter
import os

def pasteimg(): 
    img2 = Image.open('tmp/resized_img.jpg')

    with open('tmp\savepth.tmp','r') as reader:
        savepth = reader.read()
    
    width, height = img2.size

    if width<height:
        imgor = 'p'
    else:
        imgor = 'l'
    
    if imgor == 'p':
        img1 = Image.open('frms\portrait.jpg')
        backim = img1.copy()
        backim.paste(img2,(153,105))
        backim.save(savepth)
        os.startfile(savepth)
    else:
        img1 = Image.open('frms\landscape.jpg')
        backim = img1.copy()
        backim.paste(img2,(90,140))
        backim.save(savepth)
        os.startfile(savepth)
