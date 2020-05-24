import hashlib
from datetime import datetime  

timestamp = datetime.datetime.now(datetime.timezone.utc).strftime("%Y-%m-%dT%H:%M:%S.%f%Z")


class Block:

    def __init__(self, timestamp, data, previous_hash=0):
        self.timestamp = timestamp
        self.data = data
        self.previous_hash = previous_hash
        self.hash = self.calc_hash()
        self.next = None

    def calc_hash(self):
        sha = hashlib.sha256()
        hash_str = ("We are going to encode this string of data!"+timestamp).encode('utf-8')
        sha.update(hash_str)
        return sha.hexdigest()

    def get_hash(self):
        return self.hash

    def get_prev_hash(self):
        return self.previous_hash

    def get_data(self):
        return self.data

class Chain:
    def __init__(self,head=0):
        self.head = head
        
    def add_block(self,timestamp,data,previous_hash):
        if self.head == 0:
            self.head = Block(timestamp, data, 0)
            return
        node = self.head
        while node.next:
            node = node.next

        node.next = Block(timestamp, data, previous_hash)
        node.previous_hash = self.head.get_hash()
        self.head = node
        print(self.head.data,self.head.timestamp)
        return self.head.previous_hash


#TESTING
# timestamp = datetime.datetime.now(datetime.timezone.utc).strftime("%Y-%m-%dT%H:%M:%S.%f%Z")
# data = "some data string1"
# data1 = "ajhsdflhaelifqiewfhdsvjax"
# data2 = "poiuytaqwtrwerhfbxvdajax"
# data3 = "123123124t2563674684"
# chain =  Chain()

# last_hash = chain.add_block(timestamp, data, 0)
# timestamp = datetime.datetime.now(datetime.timezone.utc).strftime("%Y-%m-%dT%H:%M:%S.%f%Z")
# last_hash2 = chain.add_block(timestamp, data1, last_hash)
# timestamp = datetime.datetime.now(datetime.timezone.utc).strftime("%Y-%m-%dT%H:%M:%S.%f%Z")
# last_hash3= chain.add_block(timestamp, data2,last_hash2)
# timestamp = datetime.datetime.now(datetime.timezone.utc).strftime("%Y-%m-%dT%H:%M:%S.%f%Z")
# chain.add_block(timestamp, data3,last_hash3)
# print(chain)