

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
        if capacity<=0:
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
            print("-1")
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

    def set(self, key, data):
        #check if the key is present in the hash_map
        if key in self.hash_map:
            node = self.hash_map[key] #assign  a key to the node
            node.data = data    #assign data to the node

        else:
            new_node = Node(key,data) # new instanse of the Node
            if self.size == self.capacity:#check if capacity is not exceed (cache hit)
                data = self.end.data #
                del self.hash_map[self.end.key] #delete the key from hash_map, where 
                self.delete_element_by_data(data)

            self.insert_start(new_node)
            self.hash_map[key] = new_node
      
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
            self.end = node
        else:
            node.prev = None
            node.next = self.head
            self.head.prev = node
            self.head = node
        self.size += 1
        

    def delete_element_by_data(self, x):
            
            if self.head is None: #check if the DLL is empty
                print("The list has no element to delete")
                return 
        
            if self.head.next is None: #check if DLL has 1 node
                if self.head.data == x: # and the only one node == x
                    self.head = self.head.next
                    self.head.prev = None # deleting the head
                    self.size-=1  
                else:
                    print("Item not found")
                return 

            if self.end.data == x: #deleting end node
                node = self.end
                self.end = node.prev
                self.end.next = None
                self.size -=1
            else:
            #removing node from the middle
                node = self.head
                while node.next:
                    if node.data == x:
                        break
                    node = node.next
                
                node.prev.next = node.next
                node.next.prev = node.prev   


    def print_elements(self):
        
        n = self.head
        print("[head = %s, end = %s]" % (self.head.data, self.end.data), end=" ")
        while n:
            print("%s <-> " % (n.data), end = "")
            n = n.next
        print("None")
      
   
        
our_cache = LRU_Cache(5)

our_cache.set(1, 1)
our_cache.set(2, 2)
our_cache.set(3, 3)
our_cache.set(4, 4)
our_cache.print_elements()

our_cache.get(1)       # returns 1

our_cache.get(2)       # returns 2

our_cache.get(9)      # returns -1 because 9 is not present in the cache

our_cache.set(5, 5) 

our_cache.set(6, 6)

our_cache.get(3)      # returns -1 because the cache reached it's capacity and 3 was the least recently used entry
