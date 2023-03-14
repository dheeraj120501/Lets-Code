#Python Image Library (PIL)

#Installation:
#Open terminal
#pip install pillow

from PIL import Image

#Open an image
mem_img = Image.open('d:/images/kids.jpg')

#fetch its attributes
#print(mem_img.size) # size of the image as a (w,h) tuple
#print(mem_img.format) #format: JPEG, PNG, ...
#print(mem_img.mode) #Color model

#Create a thumbnail
#mem_img.thumbnail((128,128)) #thumbnail will be of size near to tuple(w,h) maintaining the aspect ratio.
#mem_img.save('d:/temp/kids_thumbnail.jpg')

#Crop a region
#box = (120,950,900,2400) #x1,y1,x2,y2
#region = mem_img.crop(box)
#region.save('d:/temp/vikas.jpg')

#Rolling
w,h = mem_img.size #size of the image (5000,3954)
roll_width = w//4 #25% roll
box_1 = (0,0,roll_width,h) #(0,0,1250,3954) (x1,y1, x2,y2)
box_2 = (roll_width,0,w,h) #(1250,3950,5000,3954) (x1,y1,x2,y2)

region_1 = mem_img.crop(box_1)
region_2 = mem_img.crop(box_2)

new_box1 = (0,0, region_2.size[0], region_2.size[1])
new_box2 = (region_2.size[0],0,  w,h)

mem_img.paste(region_2, new_box1)
mem_img.paste(region_1, new_box2)

mem_img.save('d:/temp/kids_rolling.jpg')