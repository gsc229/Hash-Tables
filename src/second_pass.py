# '''
# Linked List hash table key/value pair
# '''


class LinkedPair:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None

    def delete(self):
        self.key = ""
    
    def update(self, newValue):
        self.value = newValue


class HashTable:
    '''
    A hash table that with `capacity` buckets
    that accepts string keys
    '''

    def __init__(self, capacity):
        self.capacity = capacity  # Number of buckets in the hash table
        self.storage = [None] * capacity
        self.size = 0

    def _hash(self, key):
        '''
        Hash an arbitrary key and return an integer.

        You may replace the Python hash with DJB2 as a stretch goal.
        '''
        
        return hash(key)

    def _hash_djb2(self, key):
        '''
        Hash an arbitrary key using DJB2 hash

        OPTIONAL STRETCH: Research and implement DJB2
        '''
        pass

    def _hash_mod(self, key):
        '''
        Take an arbitrary key and return a valid integer index
        within the storage capacity of the hash table.
        '''

        return self._hash(key) % self.capacity

    def insert(self, key, value):
        '''
        Store the value with the given key.

        Hash collisions should be handled with Linked List Chaining.

        Fill this in.        
        '''
        hased_key = self._hash_mod(key)
        current_node = self.storage[hased_key] 
        prev_node = None

        if current_node == None:
            self.storage[hased_key] = LinkedPair(key, value)
            
        else:
            #print(f"ELSE")
            
            while current_node:                
                if current_node.key == key:
                    print(f"SAME KEY")                    
                    current_node.update(value) 
                    print(f"UPDATED: {current_node.key}: {current_node.value}")
                    return current_node.value
                prev_node = current_node
                current_node = current_node.next
                
                #print(f"INSERT")
            
            prev_node.next = LinkedPair(key, value)           
            

    def remove(self, key):
        '''
        Remove the value stored with the given key.

        Print a warning if the key is not found.

        Fill this in.
        '''
        hased_key = self._hash_mod(key)
        examining_node = self.storage[hased_key]
        prev_node = examining_node
        next_node = examining_node.next                   

        while examining_node is not None:
            if examining_node.key == key:
                if prev_node is None: # meaning, the first node in the list is a match
                    print(f"removing {examining_node.key}: {examining_node.value}")
                    examining_node.delete() # just deletet the node bc the next doesn't care about prev in the list. 
                    return
                else:
                    print(f"removing {examining_node.key}: {examining_node.value}")
                    prev_node.next = next_node
                    examining_node.delete()
                    return
                print("MATCH BREK")
                break
            else:
                prev_node = examining_node
                examining_node = next_node
                next_node = next_node.next

        
                   

    def retrieve(self, key):
        '''
        Retrieve the value stored with the given key.

        Returns None if the key is not found.

        Fill this in.
        
        '''
        hased_key = self._hash_mod(key)
        current_node = self.storage[hased_key]
        
        while current_node:
            if current_node.key is key:
                break
            current_node = current_node.next

        if not current_node:
            return None
        else:
            return current_node.value

    def resize(self):
        '''
        Doubles the capacity of the hash table and
        rehash all key/value pairs.

        Fill this in.
        '''
        old_storage = self.storage
        self.storage = [None]
        self.storage = self.storage * (self.capacity * 2)
        current_node = None
        for i in range(0, len(old_storage)):
            self.storage[i] = old_storage[i]
            
    


# if __name__ == "__main__":
#     ht = HashTable(2)    
    
#     print(ht._hash_mod('line_1'))
#     print(ht._hash_mod('line_2'))
#     print(ht._hash_mod('line_3'))
#     ht.insert("line_1", "Tiny hash table")
#     ht.insert("line_2", "Filled beyond capacity")
#     ht.insert("line_3", "Linked list saves the day!")

#     print("")

#     # Test storing beyond capacity
#     print(ht.retrieve('line_1'))
#     print(ht.retrieve("line_2"))
#     print(ht.retrieve("line_3"))

#     # Test resizing
#     old_capacity = len(ht.storage)
#     ht.resize()
#     new_capacity = len(ht.storage)

#     print(f"\nResized from {old_capacity} to {new_capacity}.\n")


#     print(ht._hash_mod('line_1'))
#     print(ht._hash_mod('line_2'))
#     print(ht._hash_mod('line_3'))

#     # Test if data intact after resizing
#     print(ht.retrieve("line_1"))
#     print(ht.retrieve("line_2"))
#     print(ht.retrieve("line_3"))

#     print("")


# hash1 = HashTable(5)

# print(
#     f"hash1.hash('key'): {hash1._hash('key6')}")

# hash1.insert('key6', 'six')
# print(hash1.retrieve('key6'))

#lp = LinkedPair("key1", 1)


ht = HashTable(8)

ht.insert("key-0", "val-0")
ht.insert("key-1", "val-1")
ht.insert("key-2", "val-2")
ht.insert("key-3", "val-3")
ht.insert("key-4", "val-4")
ht.insert("key-5", "val-5")
ht.insert("key-6", "val-6")
ht.insert("key-7", "val-7")
ht.insert("key-8", "val-8")
ht.insert("key-9", "val-9")

print(f"hash: {ht._hash_mod('key-0')}")
print(f"hash: {ht._hash_mod('key-1')}")
print(f"hash: {ht._hash_mod('key-2')}")
print(f"hash: {ht._hash_mod('key-3')}")
print(f"hash: {ht._hash_mod('key-4')}")
print(f"hash: {ht._hash_mod('key-5')}")
print(f"hash: {ht._hash_mod('key-6')}")

ht.insert("key-0", "new-val-0")
ht.insert("key-1", "new-val-1")
ht.insert("key-2", "new-val-2")
ht.insert("key-3", "new-val-3")
ht.insert("key-4", "new-val-4")
ht.insert("key-5", "new-val-5")
ht.insert("key-6", "new-val-6")
ht.insert("key-7", "new-val-7")
ht.insert("key-8", "new-val-8")
ht.insert("key-9", "new-val-9")

return_value = ht.retrieve("key-0")
print(f"key-0: {return_value}")
return_value = ht.retrieve("key-1")
print(f"key-1: {return_value}")
return_value = ht.retrieve("key-2")
print(f"key-2: {return_value}")
return_value = ht.retrieve("key-3")
print(f"key-3: {return_value}")
return_value = ht.retrieve("key-4")
print(f"key-4: {return_value}")
return_value = ht.retrieve("key-5")
print(f"key-5: {return_value}")
return_value = ht.retrieve("key-6")
print(f"key-6: {return_value}")
return_value = ht.retrieve("key-7")
print(f"key-7: {return_value}")

ht.remove('key-0')
print(f"retrieve key-0: {ht.retrieve('key-0')}")


print(ht.storage)
