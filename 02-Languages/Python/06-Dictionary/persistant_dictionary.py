import dbm
#dbm package allows storing/retrieving dictionaries to/from the disk.
#mode: 'r' (read only),'w' (read/write),'c' (create/read/write), 'n' (create/overwrite/read/write)
#create/open a dictionary with r/w support


def createNew(dname):
    passwrd = input('Enter password')
    if passwrd == 'imadmin':
        store = dbm.open('d:/p_dict.txt', 'n')
        store['breakfast'] = ''
        store['lunch'] = ''
        store['dinner'] = ''
        store.close()
        print('New Dictionary Created')
    else:
        print('Wrong Password')

def display(dname):
    store = dbm.open('d:/p_dict.txt', 'r')
    #traverse (read)
    for x in store:
        print(x.decode(), ':', store[x].decode() )
    store.close()

def manipulate(dname):
    store = dbm.open('d:/p_dict.txt', 'w')
    while True:
        print('1. Update the meals ')
        print('2. Ask when to eat what ')
        ch = int(input())
        if ch == 1:
            meal_item = input('Enter meal item ')
            m = input('Enter the meal which should include '+ meal_item +' ')
            if m in store:
                items = store[m].decode() #read existing value
                if len(items) >0:
                    items = items+ ', ' + meal_item
                else:
                    items = meal_item
                store[m] = items #update the items against the key
                print('Update Successful')
            else:
                print('Valid meals are ', store.keys())


        elif ch == 2:
            query = input('ask when to eat what ')
            flag = False
            ans = ''
            for x in store:
                # store[x]: value of the key x in binary object form
                # store[x].decode() : value of the key x in string object form
                # store[x].decode().split(',') : splits the string on commas and create a list
                meal = store[x].decode().split(',')
                if query in meal:
                    ans = ans + x.decode() + ' '
                    flag = True

            if flag == True:
                print('Have ', query, ' at ', ans)
            else:
                print('No data found')

        ch = input('Do you have more queries (y/n) ').lower()
        if ch != 'y':
            break

    store.close()


def main():
    dname = 'd:/p_dict.txt'
    while True:
        print('1 Create a new dictionary')
        print('2 Read the dictionary')
        print('3 Manipulate')
        print('4 Exit')
        ch = int(input())

        if ch == 1:
            createNew(dname)
        elif ch == 2:
            display(dname)
        elif ch == 3:
            manipulate(dname)
        elif ch == 4:
            break
        else:
            print('Wrong choice')

main()