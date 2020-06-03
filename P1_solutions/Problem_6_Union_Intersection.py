class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

    def get_value(self):
        return self.value

    def __repr__(self):
        return str(self.value)

#Intersection = only common elements in two sets

#union = all unique elements from both set

class LinkedList:
    def __init__(self):
        self.head = None

    def __str__(self):
        cur_head = self.head
        out_string = ""
        while cur_head:
            out_string += str(cur_head.value) + " -> "
            cur_head = cur_head.next
        return out_string


    def append(self, value):

        if self.head is None:
            self.head = Node(value)
            return

        node = self.head
        while node.next:
            node = node.next

        node.next = Node(value)
        return node
    
    def size(self):
        size = 0
        node = self.head
        while node:
            size += 1
            node = node.next
        return size

def union(llist_1, llist_2):
    union_set = set()
    node = llist_1.head

    while node:
        if node.value not in union_set:
            val = node.value
            union_set.add(val)
            node = node.next
        else:
            node = node.next

    node = llist_2.head
    while node:
        if node.value not in union_set:
            val = node.value
            union_set.add(val)
            node = node.next
        else:
            node = node.next
     
    
    union_llist = LinkedList()
    for x in union_set:
        union_llist.append(x)    

    return union_llist

def intersection(llist_1, llist_2):
    # Your Solution Here
    first_set = set()
    common_set = set()
    node = llist_1.head

    while node:
        if node.value not in first_set:
            val = node.value
            first_set.add(val)
            node = node.next
        else:
            node = node.next
        
    node = llist_2.head
    while node:
        if node.value in first_set:
            val = node.value
            common_set.add(val)
            node = node.next
        else:
            node = node.next
        
    
    common_llist = LinkedList()
    for x in common_set:
        common_llist.append(x)    

    return common_llist
     


# Test case 1

linked_list_1 = LinkedList()
linked_list_2 = LinkedList()

element_1 = [3,2,4,35,6,65,6,4,3,21]
element_2 = [6,32,4,9,6,1,11,21,1]

for i in element_1:
    linked_list_1.append(i)

for i in element_2:
    linked_list_2.append(i)

print (union(linked_list_1,linked_list_2))
print (intersection(linked_list_1,linked_list_2))

# Test case 2

linked_list_3 = LinkedList()
linked_list_4 = LinkedList()

element_3 = [3,2,4,35,6,65,6,4,3,23]
element_4 = [1,7,8,9,11,21,1]

for i in element_3:
    linked_list_3.append(i)

for i in element_4:
    linked_list_4.append(i)

print (union(linked_list_3,linked_list_4))
print (intersection(linked_list_3,linked_list_4))

# Test case 3

linked_list_5 = LinkedList()
linked_list_6 = LinkedList()

element_5 = [0,0,0]
element_6 = []

for i in element_5:
    linked_list_5.append(i)

for i in element_6:
    linked_list_6.append(i)

print (union(linked_list_5,linked_list_6))
print (intersection(linked_list_5,linked_list_6))

# Test case 4

linked_list_7 = LinkedList()
linked_list_8 = LinkedList()

element_7 = []
element_8 = []

for i in element_7:
    linked_list_7.append(i)

for i in element_8:
    linked_list_8.append(i)

print (union(linked_list_7,linked_list_8))
print (intersection(linked_list_7,linked_list_8))