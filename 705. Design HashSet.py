class MyHashSet:

    def __init__(self):
        self.l = []
        # print(self.l)
        

    def add(self, key: int) -> None:
        if key not in self.l : 
            self.l.append(key)
        # print(self.l)

    def remove(self, key: int) -> None:
        if key in self.l :
            self.l.remove(key)
        # print(self.l)

    def contains(self, key: int) -> bool:
        return key in self.l
        


# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)