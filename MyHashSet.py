#   设计哈希集合
# 不使用任何内建的哈希表库设计一个哈希集合
#
# 具体地说，你的设计应该包含以下的功能
#
# add(value)：向哈希集合中插入一个值。
# contains(value) ：返回哈希集合中是否存在这个值。
# remove(value)：将给定值从哈希集合中删除。如果哈希集合中没有这个值，什么也不做。
#
# 示例:
#
# MyHashSet hashSet = new MyHashSet();
# hashSet.add(1);
# hashSet.add(2);
# hashSet.contains(1);    // 返回 true
# hashSet.contains(3);    // 返回 false (未找到)
# hashSet.add(2);
# hashSet.contains(2);    // 返回 true
# hashSet.remove(2);
# hashSet.contains(2);    // 返回  false (已经被删除)
#
# 注意：
#
# 所有的值都在 [1, 1000000]的范围内。
# 操作的总数目在[1, 10000]范围内。
# 不要使用内建的哈希集合库。


class MyHashSet_myself:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.table = [0] * 1000000

    def add(self, key):
        """
        :type key: int
        :rtype: void
        """
        k = key % 1000000
        self.table[k] = 1

    def remove(self, key):
        """
        :type key: int
        :rtype: void
        """
        k = key % 1000000
        # if self.table[k] == 1
        self.table[k] = 0
    def contains(self, key):
        """
        Returns true if this set did not already contain the specified element
        :type key: int
        :rtype: bool
        """
        k = key % 1000000
        if self.table[k] == 1:
            return True
        return False


class MyHashSet:
    def __init__(self):
        self.data = [[] for i in range(0, 10000)]
    def add(self, key):
        if not key in self.data[(key-1)//100]:#在[1,1000000]的范畴内，key//100-1和(key-1)//100不等效
        # if not self.contains(key):##这里能直接用contain的
            self.data[(key-1)//100].append(key)
    def remove(self, key):
        if self.contains(key):
            self.data[(key-1)//100].remove(key)
    def contains(self, key):
        return key in self.data[(key-1)//100]

class MyHashSet_v2:

    def __init__(self):
        self.bucket = 1000
        self.inner_bucket = 1001
        self.hashset = [[] for i in range(self.inner_bucket)]#他为了逻辑简洁，多出来了一个？这是桶的内部，其实算下来，就是多了1000个

    def hash(self, key):
        return key % self.bucket

    def point(self, key):
        return key // self.bucket

    def add(self, key):
        hashkey = self.hash(key)
        if not self.hashset[hashkey]:
            self.hashset[hashkey] = [0] * self.inner_bucket#还要一次初始化
        self.hashset[hashkey][self.point(key)] = 1

    def remove(self, key):
        """
        :type key: int
        :rtype: void
        """
        hashkey = self.hash(key)
        if self.hashset[hashkey]:
            self.hashset[hashkey][self.point(key)] = 0

    def contains(self, key):
        """
        Returns true if this set did not already contain the specified element
        :type key: int
        :rtype: bool
        """
        hashkey = self.hash(key)
        return self.hashset[hashkey] != [] and self.hashset[hashkey][self.point(key)] == 1


# Your MyHashSet object will be instantiated and called as such:
obj = MyHashSet()
obj.add(5)
print(obj.contains(5))
obj.remove(5)
print(obj.contains(5))


print(1//100)