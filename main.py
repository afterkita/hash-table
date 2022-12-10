def ASCI_int(s):
    sum1 = 0
    for i in s:
        print(ord(i))
        sum1 += ord(i)
    return sum1
class HashTable:
    def __init__(self):
	    self.capacity = 50
	    self.size = 0
	    self.buckets = [None] * self.capacity
    def Sizze(self):
        return self.size
    def hash(self, key):
        hashsum = 0
        for idx, c in enumerate(key):
            hashsum += (idx + len(key)) ** ord(c)
            hashsum = hashsum % self.capacity
        return hashsum
    def insert(self, key, value):
        self.size += 1
        index = self.hash(key)
        node = self.buckets[index]
        if node is None:
            self.buckets[index] = Node(key, value)
            return
        # Колизия двигаемся по связ списку
        prev = node
        while node is not None:
            prev = node
            node = node.next
        prev.next = Node(key, value)
    def find(self, key):
        index = self.hash(key)
        node = self.buckets[index]
        while node is not None and node.key != key:
            node = node.next
        if node is None:
            return None
        else:
            return node.value
    def to_write(self, key):
        index = self.hash(key)
        node = self.buckets[index]
        while node is not None and node.key != key:
            node = node.next
        if node is None:
            return None
        else:
            for i in range(0, self.size):
                print(node.value)
                node = node.next
                print(node.value)

    def remove(self, key):
        index = self.hash(key)
        node = self.buckets[index]
        prev = None
        while node is not None and node.key != key:
            prev = node
            node = node.next
        if node is None:
            return None
        else:
            self.size -= 1
            result = node.value
            if prev is None:
                node = None
            else:
                prev.next = prev.next.next
            return result
class Node:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None
class HashTable2:
    def __init__(self):
	    self.capacity = 50
	    self.size = 0
	    self.buckets = [None] * self.capacity
    def Sizze(self):
        return self.size
    def hash(self, key):
        hashsum = 0
        for idx, c in enumerate(key):
            hashsum += (idx + len(key)) ** ord(c)
            hashsum = hashsum % self.capacity
        return hashsum
    def insert(self, key, val):
        self.size += 1
        index = self.hash(key)
        node = self.buckets[index]
        if node is None:
            self.buckets[index] = Node2(key, val)
            return
        node.value.append(val)
    def find(self, key):
        index = self.hash(key)
        node = self.buckets[index]
        while node is not None and node.key != key:
            node = node.next
        if node is None:
            return None
        else:
            return node.value
    def remove(self, key):
        index = self.hash(key)
        node = self.buckets[index]
        prev = None
        while node is not None and node.key != key:
            prev = node
            node = node.next
        if node is None:
            return None
        else:
            self.size -= 1
            result = node.value
            if prev is None:
                node = None
            else:
                prev.next = prev.next.next
            return result
class Node2:
    def __init__(self, key, value):
        self.key = key
        self.value = [value]
        self.next = None

with open("input.txt", mode="r") as f:
    text = f.read()
    text_arr = text.split()
    print(len(text_arr))

ht = HashTable2()

for i in range(0, len(text_arr)):
    ht.insert(str(i), text_arr[i])
ht.insert('0','first')
ht.insert('0','second')
ht.insert('0','deside')
with open("output.txt", mode="w") as f1:
    f1.write('Key  Data'+'\n')
    for i in range(0, ht.Sizze()):
        f1.write(str(i)+ ' - ' + str(ht.find(str(i))) +'\n')

#print(ht.find("4"))
#print(ht.find("6"))
#ht.remove("4")
#print(ht.find("4"))
#print('----')
#ht.insert('jojo', 'strars')
#ht.insert('jojo', 'Strars')
#ht.to_write('jojo')