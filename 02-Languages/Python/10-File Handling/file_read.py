#File Reading

def file_read_1(file):
    #open the file
    file_handle = open(file, 'r') # r: read in text mode. It requires target file to exists, otherwise FileNotFoundError is raised.
    #read data
    buff = file_handle.readlines()
    #output on screen
    print(buff)
    #close the file
    file_handle.close()

def file_read_2(file):
    #open the file
    file_handle = open(file, 'r') # r: read in text mode. It requires target file to exists, otherwise FileNotFoundError is raised.
    #chunking: read data n characters at a time
    n = 2048 #chunk size
    while True:
        buff = file_handle.read(n) #fetch n or less number of bytes.
        if buff: #test the buff for successful fetch
            #output on screen
            print(buff, end='')
        else:
            break #stop the loop
    #close the file
    file_handle.close()

def file_read_3(file):
    #open the file
    file_handle = open(file, 'r') # r: read in text mode. It requires target file to exists, otherwise FileNotFoundError is raised.
    #iterate over the file line by line
    for l in file_handle:
        print(l, end='')
    #close the file
    file_handle.close()

def main():
    file = 'a.txt' #absolute path
    file_read_1(file)
    #file_read_2(file)
    # file_read_3(file)
main()
