Dictionary is a linear data structure that stores data as key-value pairs.
It is created using {}.
key should always be unique and immutable.
pair can be anything.

Common Dictionary functions:
    -> states['Maharashtra'] = 'Mumbai'    // update the key's value or create a new one if not present.
    -> for i in d: // here i is key
    -> d.keys()    // give list of keys
    -> d.values()  // give list of values
    -> d.update(states)    // Merge states dict with d
    -> Printing values of dict:
        -> d['hello']  // Give value if key present othewise error
        -> d.get('hello')  // Give value if key present othewise return None
    -> Deleting a pair:
        -> del d['hello']  // deletes pair 'hello' or raises KeyError
        -> d.pop('hello', 'Alternate Value')  // deletes pair 'hello' and returns the value of the pair. If key is not found then returns 'Alternate Value' (second parameter). If the 'Alternate Value' (second parameter) and the key, both, are not available then KeyError is raised.
        -> d.popitem()    // deletes and returns the last pair of the dictionary. If dictionary is empty then it raises KeyError.


Persistant Dictionary
    -> dbm package allows storing/retrieving dictionaries to/from the disk.
    -> mode: 'r' (read only),'w' (read/write),'c' (create/read/write),'n' (create/overwrite/read/write)
    -> create/open a dictionary with r/w support

    This is similar to file handling
        -> Opening a store from dbm.open(filelocation, mode) // Store it in a variable, this will work as dict name.
        -> Closing the store from storeName.close()
        -> To print the value in readable format use .decode()
            eg. store[x].decode()   //  Give the value of x

        NOTE: 
            store[x]: value of the key x in binary object form
            store[x].decode() : value of the key x in string object form