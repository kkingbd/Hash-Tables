

# '''
# Basic hash table key/value pair
# '''
class Pair:
    def __init__(self, key, value):
        self.key = key
        self.value = value


# '''
# Basic hash table
# Fill this in.  All storage values should be initialized to None
# '''
class BasicHashTable:
    def __init__(self, capacity):
        self.capacity = capacity
        self.storage = [None] * capacity


# '''
# Fill this in.
# Research and implement the djb2 hash function
# '''
def hash(string, max):
    hash_value = 5381
    for char in string:
        hash_value = ((hash_value << 5) + hash_value) + ord(char)


# '''
# Fill this in.

# If you are overwriting a value with a different key, print a warning.
# '''
def hash_table_insert(hash_table, key, value):
    storage = hash_table.storage
    avl_index = None
    exists  = False
    for i in range(len(storage)):
        if storage[i] == None:
            avl_index = i
            exists = True
    if exists:
        storage[i][1] = value
        print(f'This key: {key}, is overwritten ')
    elif avl_index == None:
        storage[len(storage)] = (key, value)
        print('Out of bound error')
    else:
        storage[avl_index]  = (key, value)


# '''
# Fill this in.

# If you try to remove a value that isn't there, print a warning.
# '''
def hash_table_remove(hash_table, key):
    storage = hash_table.storage
    target_index = None
    for i in range(len(storage)):
        if storage[i] is not None:
            if storage[i][0] == key:
                target_index = i
    if target_index is not None:
        storage[target_index] = None
    else:
        print('target does not exist')


# '''
# Fill this in.

# Should return None if the key is not found.
# '''
def hash_table_retrieve(hash_table, key):
    storage = hash_table.storage
    target_index = None
    for i in range(len(storage)):
        if storage[i] is not None:
            if storage[i][0] == key:
                target_index = i
    if target_index is not None:
        return storage[i][1]
    else:
        return None


def Testing():
    ht = BasicHashTable(16)

    hash_table_insert(ht, "line", "Here today...\n")

    hash_table_remove(ht, "line")

    if hash_table_retrieve(ht, "line") is None:
        print("...gone tomorrow (success!)")
    else:
        print("ERROR:  STILL HERE")


Testing()
