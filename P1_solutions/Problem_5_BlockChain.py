import hashlib
from datetime import datetime  

# timestamp = datetime.datetime.now(datetime.timezone.utc).strftime("%Y-%m-%dT%H:%M:%S.%f%Z")


class Block:

    def __init__(self, data, previous_hash=0):
        self.timestamp = self.get_timestamp()
        self.data = data
        self.previous_hash = previous_hash
        self.hash = self.calc_hash()
        self.next = None

    def calc_hash(self):
        sha = hashlib.sha256()
        hash_str = ("We are going to encode this string of data!"+self.get_timestamp()).encode('utf-8')
        sha.update(hash_str)
        return sha.hexdigest()

    def get_hash(self):
        return self.hash

    def get_prev_hash(self):
        return self.previous_hash

    def get_data(self):
        return self.data
    
    def get_timestamp(self):
        timestamp = datetime.utcnow().strftime("%Y-%m-%dT%H:%M:%S.%f%Z")
        return timestamp


class Chain:

    def __init__(self,head=0,tail=None):
        self.head = head
        self.tail = tail
        
    def add_block(self,data,previous_hash):
    
        if self.head == 0:
            self.head = Block(data, 0)
            self.tail = self.head
            return self.tail.previous_hash
        node = Block(data,previous_hash)
        node.previous_hash = self.tail.get_hash()
        if self.head.next is None:
            self.head.next = node
        self.tail.next = node
        self.tail = node      
        return self.tail.previous_hash


# CHAIN DATA

data = "some data string1"
data1 = "ajhsdflhaelifqiewfhdsvjax"
data2 = "poiuytaqwtrwerhfbxvdajax"
data3 = "121232234(@&ˆ(@&#ˆ(#@&@werhfbxvdajax"
chain =  Chain()


#Test 1
block0 = chain.add_block(data, 0)
print ("Pass" if (chain.head.get_data()== 'some data string1')else "Fail")

#Test 2
block1 = chain.add_block(data1, block0)
print ("Pass" if (chain.tail.get_data()== 'ajhsdflhaelifqiewfhdsvjax')else "Fail")

#Test 3
block2= chain.add_block(data2,block1)
print ("Pass" if (chain.tail.get_data()== 'poiuytaqwtrwerhfbxvdajax')else "Fail")

#Test 4
block3= chain.add_block(data3,block2)
print ("Pass" if (chain.tail.get_data()== '121232234(@&ˆ(@&#ˆ(#@&@werhfbxvdajax')else "Fail")

