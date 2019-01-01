# 设计哈希映射
# 不使用任何内建的哈希表库设计一个哈希映射
#
# 具体地说，你的设计应该包含以下的功能
#
# put(key, value)：向哈希映射中插入(键,值)的数值对。如果键对应的值已经存在，更新这个值。
# get(key)：返回给定的键所对应的值，如果映射中不包含这个键，返回-1。
# remove(key)：如果映射中存在这个键，删除这个数值对。
#
# 示例：
#
# MyHashMap hashMap = new MyHashMap();
# hashMap.put(1, 1);
# hashMap.put(2, 2);
# hashMap.get(1);            // 返回 1
# hashMap.get(3);            // 返回 -1 (未找到)
# hashMap.put(2, 1);         // 更新已有的值
# hashMap.get(2);            // 返回 1
# hashMap.remove(2);         // 删除键为2的数据
# hashMap.get(2);            // 返回 -1 (未找到)
#
# 注意：
#
# 所有的值都在 [1, 1000000]的范围内。
# 操作的总数目在[1, 10000]范围内。
# 不要使用内建的哈希库。


# 我这个的缺点是数组过大！！！！！！！理想情况下，1000个桶均匀分布，每个桶10个数据，那我还是用掉了1000000的存储空间，没什么意义，所以不要随便学别人。
class MyHashMap_myself:
    def __init__(self):
        self.bucket = [[] for _ in range(1000)]
        self.inner_bucket = [-1 for _ in range(1000)]
    def hash(self,key):

        return (key - 1) // 1000

    def put(self, key, value):
        if not self.bucket[self.hash(key)]:
            self.bucket[self.hash(key)].extend(self.inner_bucket)
        self.bucket[self.hash(key)][key % 1000] = value
        print(self.bucket[self.hash(key)][key % 1000])

    def get(self, key):
        if not self.bucket[self.hash(key)]:
            print('not exist')
            return -1
        return self.bucket[self.hash(key)][key%1000]

    def remove(self, key):
        if not self.bucket[self.hash(key)]:
            return
        self.bucket[self.hash(key)][key % 1000] = -1

# 这是利用下标手动匹配key和value的方案
# 这不是1000乘以1000，是给key专门配了一个value。理想情况应该是1000*（10+10）
class MyHashMap:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.keys = [[] for i in range(1000)]
        self.values = [[] for i in range(1000)]

    def put(self, key, value):
        """
        value will always be positive.
        :type key: int
        :type value: int
        :rtype: void
        """
        se = key % 1000
        if key not in self.keys[se]:
            self.keys[se].append(key)
            self.values[se].append(value)
        else:
            self.values[se][self.keys[se].index(key)] = value

    def get(self, key):
        """
        Returns the value to which the specified key is mapped, or -1 if this map contains no mapping for the key
        :type key: int
        :rtype: int
        """
        se = key % 1000
        if key not in self.keys[se]:
            return -1
        else:
            return self.values[se][self.keys[se].index(key)]

    def remove(self, key):
        """
        Removes the mapping of the specified value key if this map contains a mapping for the key
        :type key: int
        :rtype: void
        """
        se = key % 1000
        if key in self.keys[se]:
            self.values[se].pop(self.keys[se].index(key))
            self.keys[se].remove(key)


# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)
["MyHashMap","remove","put","put","put","put","put","put","get","put","put"]
[[],[2],[3,11],[4,13],[15,6],[6,15],[8,8],[11,0],[11],[1,10],[12,14]]
# Your MyHashMap object will be instantiated and called as such:
obj = MyHashMap()
obj.remove(2)
obj.put(3,1)
obj.put(4,13)
obj.put(15,6)
obj.put(6,15)
obj.put(8,8)
obj.put(11,0)
print(obj.get(11))
obj.put(1,10)
obj.put(12,14)


l = [1,2,3,4,5,6,7]
print(l.index(5))



