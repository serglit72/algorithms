The Huffmann algorithm is most known algorithm for compress data without losses. It's implemented by using library **heapq** which handles inserting and removing from the heap pretty fast.
The main idea is to use proper approach to mapping data symbols from input. In order to simplify the implementation I converted the pairs of character occurence and frequency in reversed way. 

That made much easier to build a tree and traverse it on the next phase where I created a code map.
    The code mapping is created recursively (**Time complexity = O(n)**)

The time complexity of the Huffman algorithm is **O(nlogn)**. Using a heap to store the weight of each tree, each iteration requires **O(logn)** time to determine the cheapest weight and insert the new weight. There are **O(n)** iterations, one for each item.