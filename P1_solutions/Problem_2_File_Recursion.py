import os

path = "P1_solutions/testdir"
suffix = ".h"
suffix1 = ".c"
suffix2 = ".txt"
suffix3 = ".gitkeep"
def find_files(pth,sffix):
    """
    Find all files beneath path with file name suffix.

    Note that a path may contain further subdirectories
    and those subdirectories may also contain further subdirectories.

    There are no limit to the depth of the subdirectories can be.

    Args:
      suffix(str): suffix if the file name to be found
      path(str): path of the file system

    Returns:
       a list of paths
    """

    path = pth
    suffix = sffix
    found_pathes = []
    
    def find_recursively(path,suffix,found_pathes):
        for i in os.listdir(path):
            if os.path.isfile(path+"/"+i):
                name = i
                if name.endswith(suffix):
                    p = path+"/"+i
                    found_pathes.append(p)
                    
            #check if path is DIRECTORY
            elif os.path.isdir(path+"/"+i):
                find_recursively(path+"/"+i,suffix,found_pathes) 
    find_recursively(path,suffix,found_pathes)        
    return found_pathes 
             
print(find_files(path,suffix))  
#Test 1
print ("Pass" if ((find_files(path,".h") == ['P1_solutions/testdir/subdir3/subsubdir1/b.h',\
     'P1_solutions/testdir/subdir5/a.h', 'P1_solutions/testdir/t1.h', 'P1_solutions/testdir/subdir1/a.h'])) else "Fail")

#Test 2
print(find_files(path,suffix1))
print ("Pass" if ((find_files(path,".c") == ['P1_solutions/testdir/subdir3/subsubdir1/b.c',\
 'P1_solutions/testdir/t1.c', 'P1_solutions/testdir/subdir5/a.c', 'P1_solutions/testdir/subdir1/a.c'])) else "Fail")

#Test 3
print(find_files(path,suffix2))
print ("Pass" if ((find_files(path,".txt") == [])) else "Fail")  

#Test 4
print(find_files(path,suffix3))
print ("Pass" if ((find_files(path,".gitkeep") == ['P1_solutions/testdir/subdir4/.gitkeep', 'P1_solutions/testdir/subdir2/.gitkeep'])) else "Fail") 