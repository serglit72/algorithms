

#Creating a node for doubly linked list 
class Node(object):
    #Constructor to create a new node
    def __init__(self,key,data, next=None, prev=None): 
        self.next = next # reference to next node in DLL 
        self.prev = prev # reference to previous node in DLL 
        self.data = data #data of the node (going to be an index of DLL)
        self.key = key #key for the hash_map

#Creating an algorithm based on doubly linked list and hash_map


class LRU_Cache:

    def __init__(self, capacity):
        # Initialize class variables
        if capacity <= 0:
            print("Capacity should be > 0 !")
            return
        self.capacity = capacity
        self.hash_map = {}
        self.head = None
        self.end = None
        self.size = 0

    
    def get(self, key):
        # Retrieve data from provided key. Return -1 if nonexistent. 
        if key not in self.hash_map:
            print("-1, key "+str(key)+" doesn't exist")
            return
        
        node = self.hash_map[key]
        # return the data if we are already looking at head
        if self.head == node:
            print(node.data)
            return node.data

        self.delete_element_by_data(key)
        self.insert_start(node)
        print(node.data)
        return node.data

    def _set(self, key, data):
        if key > self.capacity:
            print("Capacity is 0.Check the value")
            return
        #check if the key is present in the hash_map
        if key in self.hash_map:
            node = self.hash_map[key] #assign  a key to the node
            node.data = data    #assign data to the node

        else:
            new_node = Node(key,data) # new instanse of the Node
            if self.size == self.capacity:#check if capacity is not exceed (cache hit)
                data = self.end.data #moving to the end
                del self.hash_map[self.end.key] #delete the key from hash_map, where 
                self.delete_element_by_data(data) #delete element from the end
                self.insert_start(new_node)
                self.hash_map[key] = new_node
            else:
                self.insert_start(new_node)
                self.hash_map[key] = new_node
            
        # return
            


    def ssize(self): #getting a size of the DLL
        
        if self.head is None:
            print("List has no element")
            return
        else:
            n = self.head
            while n is not None:
                n = n.next
                self.size +=1
        return(self.size)
    
    # def is_empty(self):

    #     if self.head is None:
    #         print("DLL is empty")
    #         return
    
    
    def insert_start(self,node):  # pushing new node to the upfront of the DLL
        
        if not self.head:
            self.head = node
            self.end = self.head
        else:
            node.prev = None
            node.next = self.head
            self.head.prev = node
            self.head = node
        # self.hash_map[node.key] = node
        self.size += 1
        

    def delete_element_by_data(self, x):
            cur = self.head
            if cur is None: #check if the DLL is empty
                print("The list has no element to delete")
                return 
                
            elif cur.data == x: # and the only one node == head == x
                self.head = cur.next
                self.size -=1  
           
            elif self.end.data == x: #deleting node from the end
                self.end = self.end.prev
                self.end.next = None
                self.size -=1
            else:
            #removing node from the middle
                
                while cur:
                    if cur.data == x:
                        cur.prev.next = cur.next
                        cur.next.prev = cur.prev
                        self.size -=1
                    cur = cur.next
                    
            
    def print_elements(self):
        
        n = self.head
        print("[head = %s, end = %s]" % (self.head.data, self.end.data), end=" ")
        while n:
            print("%s <-> " % (n.data), end = "")
            n = n.next
        print("None")
      
   
# Testcase #1 cache capacity == 5       
# our_cache = LRU_Cache(5)

# our_cache._set(1, 1)
# our_cache._set(2, 2)
# our_cache._set(3, 3)
# our_cache._set(4, 4)
# our_cache.print_elements()
# our_cache.get(1)       # returns 1
# our_cache.get(2)       # returns 2
# our_cache.get(9)      # returns -1 because 9 is not present in the cache
# our_cache._set(5, 5) 
# our_cache._set(6, 6)
# our_cache.get(3)      # returns -1 because the cache reached it's capacity and 3 was the least recently used entry

# Testcase #2  cache capacity == 1
# our_cache = LRU_Cache(1)
# our_cache._set(1, 1)
# our_cache.print_elements()
# our_cache._set(2, 2)
# our_cache.print_elements()
# our_cache._set(3, 3)
# our_cache._set(4, 4)
# our_cache.print_elements()

# our_cache.get(1)       # returns -1

# our_cache.get(2)       # returns -1

# our_cache.get(4)      # returns 4 because 4 is present in the cache

# our_cache.get(3)      # returns -1 because the cache reached it's capacity and 3 was the least recently used entry

# Testcase #3  cache capacity == 0
our_cache = LRU_Cache(0)
our_cache._set(1, 1)
our_cache.print_elements()
our_cache._set(2, 2)
our_cache.print_elements()

our_cache.get(1)       # returns -1

our_cache.get(2)       # returns -1


