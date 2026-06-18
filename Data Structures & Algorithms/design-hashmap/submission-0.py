class MyHashMap:

    def __init__(self):
        self.hashmap = []

    def put(self, key: int, value: int) -> None:
        there = False
        for k in range(len(self.hashmap)):
            if self.hashmap[k][1] == key:
                self.hashmap[k][1] = value
                there = True
        if there == False:
            self.hashmap.append([key, value])

    def get(self, key: int) -> int:
        for k in range(len(self.hashmap)):
            if self.hashmap[k][0] == key:
                print(f"key: {key}, hashmap item: [{self.hashmap[k][0]}, {self.hashmap[k][1]}]")
                return self.hashmap[k][1]
        return -1
        

    def remove(self, key: int) -> None:
        for k in range(len(self.hashmap)):
            if self.hashmap[k][0] == key:
                self.hashmap.pop([k][0])


# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)