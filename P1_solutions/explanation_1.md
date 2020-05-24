To implement **LRU Cache** (Least Recent Used Cache) I used a **doubly linked list** and **hash table**.
The linked list data structure used to implement the fastest access to frequently using data and move the lower frequent used data to the end of the list. Once we hit the maximum size of the cache, we have to remove the least recently used entry and then insert new element. The doubly linked list data structure allowes to reach, move, remove, insert the new element into list. 

The hash table is implemented to assign a unique address to the node (element of the linked list). This data structure allowes to get any element value by key and the key is unique.
    
**Time complexity** - **O(1)**
 because the hash table makes the time of **'get()'** like **O(1)**. The list of double linked nodes makes the nodes adding/removal operations **O(1)**.