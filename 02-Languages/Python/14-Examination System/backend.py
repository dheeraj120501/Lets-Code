import dbm

def getNextId(store):
    i = 1
    while True:
        if str(i) in store:
            i+=1
        else:
            return str(i) #unqiue

def deleteQuestionsOfTopic(qStore, tid):
    ids = []
    for x in qStore:
        if qStore[x].decode().endswith(tid):
            ids.append(x)
    for i in ids:
        qStore.pop(i)


def manageTopicSet(tfname, qfname):
    tstore = dbm.open(tfname, 'c') #create,write and read (no overwrite)
    qstore = dbm.open(qfname, 'c')  # create,write and read (no overwrite)

    while True:
        print('1 Add Topic')
        print('2 View Topics')
        print('3 Delete Topic')
        print('4 Exit')
        ch = int(input())
        if ch == 1: #Add
            tstore[getNextId(tstore)] = input('Enter Topic Name ')

        elif ch == 2: #view
            print('All Topics')
            for x in tstore:
                print(x.decode(), ')', tstore[x].decode())

        elif ch == 3:
            print('All Topics')
            for x in tstore:
                print(x.decode(), ')', tstore[x].decode())
            print('Enter tid to delete ')
            id = input()
            if id in tstore:
                deleteQuestionsOfTopic(qstore, id)
                tstore.pop(id)
                print('Deleted the Topic and all questions under it!!!')
            else:
                print('Invalid id: ', id)

        elif ch == 4:
            break
        else:
            print('Wrong Choice')

    qstore.close()
    tstore.close()


def manageQuestionSet(tfname, qfname):
    qstore = dbm.open(qfname, 'c') #create,write and read (no overwrite)
    tstore = dbm.open(tfname, 'r')  #read only

    while True:
        for tids in tstore:
            print(tids.decode(), tstore[tids].decode())
        print('Q : Quit')
        print('Enter choice')
        ch_topic = input()
        if ch_topic in tstore:
            while True:
                print('1 Add Questions')
                print('2 View Questions')
                print('3 Delete Question')
                print('4 Exit')
                ch = int(input())
                if ch == 1: #Add
                    data = []
                    print('Enter question')
                    data.append(input())
                    print('Enter number of answer options (2-4)')
                    qty = int(input())
                    if qty <2 or qty >4:
                        print('Invalid number of options')
                        continue
                    for i in range(1, qty+1):
                        print('Enter option ',i)
                        data.append(str(i) + ') ' + input())

                    print('Enter correct answer (1-',qty, ')')
                    ans = int(input())
                    if ans < 1 or ans >qty:
                        print('Invalid Correct Answer')
                        continue
                    data.append(ans)

                    #record the topic
                    data.append(int(ch_topic))

                    #record
                    qstore[getNextId(qstore)] = str(data).strip('[]')

                elif ch == 2: #view
                    print('All Questions')
                    for x in qstore:
                        print(x.decode(), ')', qstore[x].decode())

                elif ch == 3:
                    print('All Questions')
                    for x in qstore:
                        print(x.decode(), ')', qstore[x].decode())
                    print('Enter qid to delete ')
                    id = input()
                    if id in qstore:
                        qstore.pop(id)
                        print('Question Deleted')
                    else:
                        print('Invalid id: ', id)
                    pass
                elif ch == 4:
                    break
                else:
                    print('Wrong Choice')
        elif ch_topic.lower() == 'q':
            break
        else:
            print('Invalid Selection')

    qstore.close()
    tstore.close()

def getTopicStore(store):
    t_store = dbm.open(store, 'r')
    topic_store = {}
    #topic_store.update(t_store)

    for x in t_store:
        topic_store[x.decode()] = t_store[x].decode()
    t_store.close()
    return topic_store


def getQuestionStore(store):
    q_store = dbm.open(store, 'r')
    question_store = {}
    #question_store.update(q_store)
    for x in q_store:
        question_store[x.decode()] = q_store[x].decode()
    q_store.close()
    return question_store