This problem is required to walk all directory **recursively** so I have implemented a function
 def find_files() 
 which is call itself until the end of the directory will be reached. 

**Space complexity** - **O(nm)**, where **m** is the maximum depth of recursion. 
**Time complexity** is **O(n)** because where **n** is time and embedded recursive function has O(n).

```py
for i in os.listdir(path):
        if os.path.isfile(path+"/"+i):
            name = i
            if name.endswith(suffix):
                print(path+"/"+i)
                ```


    if os.path.isdir(path+"/"+i):
        find_files(path+"/"+i,suffix) 
```



