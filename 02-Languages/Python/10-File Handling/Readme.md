File handling is for performing r/w operations with files stored on disk.
Steps to work with file:
    -> Open the file and store it in a variable. The stream is formed between the application and the file.
    -> Data transfer 
    -> Close the file, deaalcates the stream and ceases all i/o operations with the file.

    NOTE: A stream is a channel of data transfer.

Opening the file:
    Modes of opening the file is:
        r: read mode, file should be present
        w: write mode
        x: write mode, create or fails if file exists
        a: append mode, create if file don't exists, no overwriting, no failing
        rb: read binary file

        NOTE: use .decode() when wanna print binary content

    open(filePath, mode)    // Return file object if success else error
    file object is used to operate on file

Data transfer:
    Reading:
        -> read()   // reads entire file return the read content to be stored in variable
        -> read(n)  // reads entire file or n bytes whichever less return the read content to be stored in variable
        -> readlines()  //reads until the end the file ends and returns a list of lines of the entire file. It does not read more than one line.
        -> for x in file_object_name:   // x is one line of file data

    Writing:
        -> file_object_name.write(x) // write content of x in file
        -> file_object_name.writelines(list) // write list elements in file

Closing the file:
    file_object_name.close()

Working with pointers of file:
    file_object_name.seek() // use to position the file pointer at a point wrt BOF(0), CUR-POS(1), EOF(2)
    .seek(i,code)   // i is the position to move, code is the position from where to move BOF(0), CUR-POS(1), EOF(2)
    file_object_name.tell() // gives the location of the pointer


NOTE: If you are writing in append mode, start your text by putting a blank space or newline character (\n) else the compiler will start the line from the last word or full stop without any blank space because the curser in case of append mode is placed right after the last character.

Shortcut for opening and closing file:
    with open(filePath, mode) as file_object_name:
    The with block automatically close the file
    Multiple files can be opened.
        eg. with open(“file1txt”) as f, open(“file2.txt”) as g:
    The files that are opened together can have different modes
    Saves processing power by opening and closing file only when running code inside the block
    Creates a context manager, so lesser chances of an exception occurring