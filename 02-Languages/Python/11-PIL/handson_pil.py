#Python Image Library
from PIL import Image, ImageDraw, ImageFont

#lets decide about the primary canvas attributes
mode ="RGB" #Color space to be used
bg_color = (239,228,176) #LIGHT YELLOW COLOR
size = (400,300) #(width, height)

#lets create the canvas
canvas = Image.new(mode=mode, size = size, color=bg_color)

#Fetch the drawing pen
pen = ImageDraw.Draw(canvas)

#lets draw a rectangle
x1y1 = (50,50) #top left
x2y2 = (canvas.size[0]-50, canvas.size[1]-50) #bottom-right (w-50, h-50)
outline_color = (255,127,0) #orange
#pen.rectangle(xy=(x1y1,x2y2),outline= outline_color,width=5)
#pen.rectangle(xy=(x1y1,x2y2),outline= outline_color,width=20)
#pen.rectangle(xy=(x1y1,x2y2), outline=(0,0,0),width=5)
#pen.ellipse(xy=(x1y1,x2y2), outline=outline_color,width=5)
#pen.arc(xy=(x1y1,x2y2), start=0, end=270, fill=outline_color)
pen.chord(xy=(x1y1,x2y2), start=0, end=270, fill=(127,127,127), outline=outline_color, width=10)

#lets draw a polygon
#points = ((80,220), (195,45), (250,245), (85,85), (320,135))
#outline_color = (136,0,21) #dark red
#pen.polygon(xy = points, outline=outline_color)


#lets write on the canvas
fnt = ImageFont.truetype(font="c:/windows/fonts/Arial.ttf", size=40)
font_color= (0,0,0) #black
pen.text(xy = (100,100), text="Python", font=fnt, fill=font_color)

#save the canvas
canvas.save("d:/q.jpg")


