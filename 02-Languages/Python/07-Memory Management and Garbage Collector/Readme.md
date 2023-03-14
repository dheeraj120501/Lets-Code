Python treats everything as Object.
Python's memory management take care of life of the object.
Variables/Objects is declared in heap.
It is accessible through one-to-many references. Most of the objects are immutable, so when they are modified there's a new allocation to hold the updated value. Older object's reference is overwritten to refer to the new object. The old object's reference count reduces. When the reference count become 0, the the object is removed from the memory.
This is garbage collection.

NOTE:
    l1 = [1,2,3]
    l2 = [1,2,3]
    l1 and l2 will have different memory address of contigious block but the blocks will point to the same object address as l1's block
    So address of l1 and l2 are different but the address of their elements are same

    == operator check if the elements are equal
    is operator check if both identifiers points to the same address or NOT
    eg.
        l1 == l2    // true
        l1 is l2    // false