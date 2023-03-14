import random
import backend
from PIL import Image, ImageDraw, ImageFont
from datetime import datetime

def getDate():
    dt = datetime.now()
    return dt.strftime('%d %b %Y')

def generateCertificate(category, name, subject, target):
    #decide the image file by category
    if category == 'A':
        fname = 'D:/batches/Python1/examination_system/certificate_a.jpg'
        clr = (166, 130, 52)  # (r,g,b)
    elif category == 'B':
        fname = 'D:/batches/Python1/examination_system/certificate_b.jpg'
        clr = (141, 137, 73)  # (r,g,b)
    else:
        fname = 'D:/batches/Python1/examination_system/certificate_c.jpg'
        clr = (135, 125, 115)  # (r,g,b)

    #load the image in memory
    canvas = Image.open(fname)
    #know the size of the canvas
    w,h = canvas.size
    #access the canvas's writing pen
    pen = ImageDraw.Draw(canvas)
    #set the image font
    fnt = ImageFont.truetype('c:/windows/fonts/ITCKRIST.TTF', size=60)
    #date today
    dt = getDate()

    #know the required sizes
    reqd_size_name = pen.textsize(text=name, font=fnt)
    reqd_size_subject = pen.textsize(text=subject, font=fnt)
    reqd_size_date = pen.textsize(text=dt, font=fnt)

    #writing the name
    x = w//2- reqd_size_name[0]//2
    y = 800 # calculated manually as per the specific certificate template
    pen.text(xy=(x,y), text=name, font=fnt, fill=clr)

    # writing the subject
    x = w // 2 - reqd_size_subject[0] // 2
    y = 1150  # calculated manually as per the specific certificate template
    pen.text(xy=(x, y), text=subject, font=fnt, fill=clr)


    # writing the date
    x = 600 # calculated manually as per the specific certificate template
    y = 1490  # calculated manually as per the specific certificate template
    pen.text(xy=(x, y), text=dt, font=fnt, fill=clr)

    #done
    canvas.save(target)


def getQuestionTopicwise(all_topics_question_bank, tid, qty):
    questions = []
    for qid in all_topics_question_bank:
        if all_topics_question_bank[qid].endswith(str(tid)):
            questions.append(all_topics_question_bank[qid])

    q = len(questions)
    while q > qty:
        questions.pop(random.randint(0, q-1))
        q-=1
    return questions

def generateQuestionPaper(topics_store, questions_store):
    all_topics = backend.getTopicStore(topics_store)
    question_bank = backend.getQuestionStore(questions_store)

    q_paper = []
    qty = 3
    for x in all_topics:
        q_paper.extend(getQuestionTopicwise(question_bank, x, qty))

    return q_paper