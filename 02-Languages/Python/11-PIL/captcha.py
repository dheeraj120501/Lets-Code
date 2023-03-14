import random
from PIL import Image, ImageFont, ImageDraw

def generateCaptcha(size):
    lowerCase = []
    for i in range(97,123): #ASCII a-z
        lowerCase.append(chr(i))

    upperCase = []
    for i in range(65,91): #ASCII A-Z
        upperCase.append(chr(i))

    digits = []
    for i in range(48,58): #ASCII 0-9
        digits.append(chr(i))

    all = []
    all.extend(lowerCase)
    all.extend(upperCase)
    all.extend(digits)

    random.shuffle(all)

    captcha = ''
    for i in range(size):
        captcha = captcha + random.choice(all)

    return captcha

def drawCaptcha(captcha):
    #load the image in memory
    canvas = Image.open('d:/images/captcha_background.jpg')

    #access canvas's writing pen
    pen = ImageDraw.Draw(canvas)

    #define the font
    fnt = ImageFont.truetype('c:/windows/fonts/segoepr.ttf', 30)

    #write
    x= 0
    y= 0
    min_y_offset = 10
    max_y_offset = 20
    min_x_offset = 20
    max_x_offset = 30
    flag = False


    for character in captcha:
        x = x + random.randint(min_x_offset, max_x_offset)
        if flag == False:
            y = y + random.randint(min_y_offset, max_y_offset)
        else:
            y = y - random.randint(min_y_offset, max_y_offset)

        flag = not flag

        pen.text(xy=(x,y), text= character, fill=(random.randint(0,180), random.randint(0,180), random.randint(0,180)), font=fnt)

    canvas.save('d:/captcha.jpg')

def main():
    captcha = generateCaptcha(5)
    print(captcha)
    drawCaptcha(captcha)

main()

