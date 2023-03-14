import random
import backend
import logic

def admin_menu(t_store,q_store):
    while True:
        print('1 Topic Management')
        print('2 Question Management')
        print('3 Exit')

        ch = int(input('Make a choice '))
        if ch == 1:
            backend.manageTopicSet(t_store, q_store)
        elif ch == 2:
            backend.manageQuestionSet(t_store, q_store)
        elif ch == 3:
            break
        else:
            print('Wrong Choice')


def getOTP():
    otp = random.randint(10000, 99999)
    print(otp)
    return str(otp)


def student_menu(t_store, q_store):
    print('Enter Name ')
    name = input()
    subject = 'Python'
    target = 'd:/temp/'+ name+'.jpg'
    q_paper = logic.generateQuestionPaper(t_store, q_store)
    score = 0
    total = len(q_paper)*2
    for q in q_paper:
        qu = q.split(',')
        qu.pop(-1) #remove tid
        question = qu[0].strip("' ") #read question
        qu.pop(0) #remove the question
        ans = qu[-1].strip("' ") #read the ans
        qu.pop(-1) #remove the ans
        print(question)
        #remains : options only
        for x in qu:
            print(x.strip("' "))
        print('*) to pass')
        print('Reply ')
        user_ans = input()
        if user_ans == ans:
            score+=2
        elif user_ans != '*':
            score-=1

    print('Score: ', score ,'/', total)
    per = score*100/total
    if per >=0 and per < 40:
        logic.generateCertificate('C', name, subject, target)
        print('Please collect the certificate : ', target)
    elif per >=40 and per < 70:
        logic.generateCertificate('B', name, subject, target)
        print('Please collect the certificate : ', target)
    elif per >= 70 and per <= 100:
        logic.generateCertificate('A', name, subject, target)
        print('Please collect the certificate : ', target)
    else:
        print('Invalid Percentage ', per)
        print('Certificate not generated')


def main():
    t_store = 'd:/temp/alltopics'
    q_store = 'd:/temp/allquestions'

    while True:
        print('1. Admin ')
        print('2. Student ')
        print('3. Exit')
        print('Enter Choice')
        ch = int(input())

        if ch == 1:
            sys_otp = getOTP()
            print('Enter OTP')
            user_otp = input()
            if sys_otp != user_otp:
                print('Login Failed')
                continue
            admin_menu(t_store, q_store)

        elif ch == 2:
            sys_otp = getOTP()
            print('Enter OTP')
            user_otp = input()
            if sys_otp != user_otp:
                print('Login Failed')
                continue
            student_menu(t_store, q_store)
        elif ch == 3:
            break
        else:
            print('Wrong Choice')

main()


