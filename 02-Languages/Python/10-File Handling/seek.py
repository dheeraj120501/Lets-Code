#File Seek
#Refer: Seek.png
def file_read_last_10_bytes(file):
    #open the file
    file_handle = open(file, 'rb') # rb: read in binary mode. It requires target file to exists, otherwise FileNotFoundError is raised.
    #position the file pointer @ offset -10 from EOF
    file_handle.seek(-10, 2)
    #read data
    buff = file_handle.read()
    #output on screen
    print(buff.decode())
    #close the file
    file_handle.close()

def get_file_size_in_bytes(file):
    file_handle = open(file, 'rb')
    #position the file pointer @ EOF
    file_handle.seek(0,2)
    #request fetch the current position (of file pointer)
    x = file_handle.tell()
    file_handle.close()
    return x

def read_reverse(file):
    file_handle = open(file, 'rb')
    # position the file pointer @ EOF
    file_handle.seek(0, 2)
    # request fetch the current position (of file pointer)
    x = file_handle.tell() #total len of file

    i = 1
    while i <= x:
        file_handle.seek(x-i,0)
        print(file_handle.read(1).decode(), end='')
        i+=1

    file_handle.close()



def main():
    file = 'd:/temp/a.txt' #absolute path
    #file_read_last_10_bytes(file)
    #l = get_file_size_in_bytes(file)
    #print('size of', file, ':',l, 'bytes')
    read_reverse(file)

main()