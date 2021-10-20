class MyHashMap:

    def __init__(self):
        self.d = {}
        

    def put(self, key: int, value: int) -> None:
        if self.d.get(key) :
            self.d[key] = value
        else :
            self.d.update({key:value})
        

    def get(self, key: int) -> int:
        return self.d.get(key,-1)
        

    def remove(self, key: int) -> None:
        self.d.pop(key,-1)       


# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)