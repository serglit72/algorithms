import heapq
import sys

# 1. Each character occurence counting:
def occurence(data_string):
    char_occurence = dict()
    string = data_string
    for i in string:
        if i in char_occurence:
            char_occurence[i]+=1
        else:
            char_occurence[i]=1
    
    return char_occurence

def convertToTuples(data_dict):
    mylist =  []
    for k,v in data_dict.items():
        mylist.append((v,k))
    return mylist

def occurenceToTree(mylist):
    s_list = []
    for each in mylist:
        heapq.heappush(s_list,[each])
    while len(s_list)>1:
        left_child = heapq.heappop(s_list)
        right_child = heapq.heappop(s_list)
        freq_l, label_l = left_child[0]
        freq_r,label_r = right_child[0]
        freq = freq_l+freq_r
        label = "".join([str(label_l),str(label_r)])
        node = [(freq,label),left_child,right_child]
        heapq.heappush(s_list,node)
    return s_list.pop()

def codeMapCreate(codeTree):
    codeMap = {}
    code = ''
    def traverse(codeTree,codeMap,code):
       
        if  len(codeTree)==1:
            label = str(codeTree[0][1])
            codeMap[label] = code    
        else:
            freq,left_child,right_child = codeTree
            traverse(left_child,codeMap,code+'0')
            traverse(right_child,codeMap,code+'1')
    traverse(codeTree,codeMap,code)

    return codeMap

def huffman_encoding(data):
    data_dict = occurence(data)
    s_list = convertToTuples(data_dict)
    codeTree = occurenceToTree(s_list)
    tree = codeTree.copy()
    codeMap = codeMapCreate(codeTree)
    encoded_data = ''
    for each in data:
        if each in codeMap.keys():
            code = codeMap.get(each)
            encoded_data += code
        else:
            print("No such letter in data")
    
    return encoded_data, tree

def huffman_decoding(data,tree):
    
    codeTree = tree
    root = tree
    
    decoded_data = ""
    for each in data:
        
        if each=="0":
            label = codeTree[1]
            codeTree = label
        else:
            label = codeTree[2]
            codeTree = label
        if len(codeTree)==1: 
            decoded_data +=label[0][1]
            codeTree = root
    return decoded_data

if __name__ == "__main__":
    codes = {}

    a_great_sentence = "The bird is the word"
    a_great_sentence1 = 'AAAAAAABBBCCCCCCCDDEEEEEE'
    a_great_sentence2 = 'This article isn’t intended to provide an exhaustive list of the idiomatic usages in Python programming'


#Test 1

    print ("The size of the data is: {}\n".format(sys.getsizeof(a_great_sentence)))
    print ("The content of the data is: {}\n".format(a_great_sentence))
   
    encoded_data, tree = huffman_encoding(a_great_sentence)

    print ("The size of the encoded data is: {}\n".format(sys.getsizeof(int(encoded_data, base=2))))
    print ("The content of the encoded data is: {}\n".format(encoded_data))

    decoded_data = huffman_decoding(encoded_data, tree)

    print ("The size of the decoded data is: {}\n".format(sys.getsizeof(decoded_data)))
    print ("The content of the encoded data is: {}\n".format(decoded_data))

#Test 2

    print ("The size of the data is: {}\n".format(sys.getsizeof(a_great_sentence1)))
    print ("The content of the data is: {}\n".format(a_great_sentence1))
   
    encoded_data, tree = huffman_encoding(a_great_sentence1)

    print ("The size of the encoded data is: {}\n".format(sys.getsizeof(int(encoded_data, base=2))))
    print ("The content of the encoded data is: {}\n".format(encoded_data))

    decoded_data = huffman_decoding(encoded_data, tree)

    print ("The size of the decoded data is: {}\n".format(sys.getsizeof(decoded_data)))
    print ("The content of the encoded data is: {}\n".format(decoded_data))

#Test 3

    print ("The size of the data is: {}\n".format(sys.getsizeof(a_great_sentence2)))
    print ("The content of the data is: {}\n".format(a_great_sentence2))
   
    encoded_data, tree = huffman_encoding(a_great_sentence2)

    print ("The size of the encoded data is: {}\n".format(sys.getsizeof(int(encoded_data, base=2))))
    print ("The content of the encoded data is: {}\n".format(encoded_data))

    decoded_data = huffman_decoding(encoded_data, tree)

    print ("The size of the decoded data is: {}\n".format(sys.getsizeof(decoded_data)))
    print ("The content of the encoded data is: {}\n".format(decoded_data))