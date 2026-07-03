class MyHashMap:

    def __init__(self):
        self.size = 769
        self.buckets = [[] for _ in range(self.size)]

    def put(self, key: int, value: int) -> None:
        bucket_index = key % self.size
        bucket = self.buckets[bucket_index] 
        for i, pair in enumerate(bucket):
            if pair[0] == key:
                bucket[i][1] = value
                return
        bucket.append([key, value])

    def get(self, key: int) -> int:
        bucket_index = key % self.size
        bucket = self.buckets[bucket_index] 
        for pair in bucket:
            if pair[0] == key:
                return pair[1]
        return -1

    def remove(self, key: int) -> None:
        bucket_index = key % self.size
        bucket = self.buckets[bucket_index] 
        for i, pair in enumerate(bucket):
            if pair[0] == key:
                bucket.pop(i)
                return         


# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)