import os

path = "./testdir"
suffix = ".c"

def find_files(path,suffix):
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
    
    for i in os.listdir(path):
        if os.path.isfile(path+"/"+i):
            name = i
            if name.endswith(suffix):
                print(path+"/"+i)
        #check if path is DIRECTORY
        if os.path.isdir(path+"/"+i):
            find_files(path+"/"+i,suffix) 
                
                
print(find_files(path,suffix))  