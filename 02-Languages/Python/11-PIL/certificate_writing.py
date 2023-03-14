#Python Image Library

from PIL import Image, ImageDraw, ImageFont

#lets open the blank certificate
canvas = Image.open(fp="d:/blank.jpg")

#Fetch the drawing pen
pen = ImageDraw.Draw(canvas)


#lets write on the canvas
fnt = ImageFont.truetype(font="c:/windows/fonts/Arial.ttf", size=50)
font_color= (255,0,0) #red
pen.text(xy = (460,260), text="Python", font=fnt, fill=font_color)

#save the canvas
canvas.save("d:/myself.jpg")


