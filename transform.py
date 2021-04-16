from PIL import Image

def resizeimg():
    with open('tmp/imagepath.tmp','r') as reader:
        img_path = reader.read()

    img = Image.open(img_path)

    width, height = img.size

    if width<height:    
        newsize = (257,400)
    else:
        newsize = (400,257)

    img = img.resize(newsize)
    img.save('tmp/resized_img.jpg')
