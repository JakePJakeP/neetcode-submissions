class MyHashSet:

    def __init__(self):
        self.size = 769
        self.buckets = [[] for _ in range(self.size)]
        

    def add(self, key: int) -> None:
        bucketIndex = key % self.size
        if key not in self.buckets[bucketIndex]:
            self.buckets[bucketIndex].append(key)

    def remove(self, key: int) -> None:
        bucketIndex = key % self.size
        if key in self.buckets[bucketIndex]:
            self.buckets[bucketIndex].remove(key)

    def contains(self, key: int) -> bool:
        bucketIndex = key % self.size
        return key in self.buckets[bucketIndex]


# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)