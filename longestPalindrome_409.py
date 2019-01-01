#hash map  practice
random = [999,333,545,333,33,23,23,23,2,344]

hash_map = 1000*[0]


#等于做了个排序，其实没真的去调整顺序，用的是本来哈希表设定的顺序。for循环过滤了计数为0的情况
for i in random:
    hash_map[i] += 1

for i in range(1000):
    for j in range(hash_map[i]):
        print(i)

print(hash_map)



class listNode(object):
    def __init__(self,val):
        self.val = val
        self.next = None

def hash_func(value,length):
    return value % length

def insert(hash_table,val,length):
    hash_key = hash_func(val,length)
    node = listNode(val)#这叫头插,新建的node的下一个是原来的，，我以为他的意思是在虚拟的头节点后边插入,我怎么感觉像甩尾那个？感觉他说的很乱啊!典型的头插法确实有一个专门的表头，插入在表头之后!
    node.next = hash_table[hash_key]
    hash_table[hash_key] = node#update new head



def search(hash_table,value,length):
    hash_key = hash_func(value,length)
    head = hash_table[hash_key]
    while head:
        print('hash_value:',head.val)
        if head.val == value:
            return True
        head = head.next

hash_table = [0]*11
insert(hash_table,9,11)
insert(hash_table,20,11)
print(search(hash_table,9,11))
print(search(hash_table,20,11))












# 给定一个包含大写字母和小写字母的字符串，找到通过这些字母构造成的最长的回文串。
#
# 在构造过程中，请注意区分大小写。比如 "Aa" 不能当做一个回文字符串。
#
# 注意:
# 假设字符串的长度不会超过 1010。
# 是求你随便组合，最长的，不是问你能不能把所有都用上能不能算回文。
# 我觉得要想让回文最长，首先，中心肯定要用奇数的，1个a，3个a，5个a，都可以用a当中心，其他那4个放哪都能行。所以说，就是把dict中所有计数都除以2，把成功的部分再乘以2，如果有多余的，+1


class Solution(object):
    def longestPalindrome(self, s):
        dict_s = {}
        for x in s:
            dict_s[x] = dict_s.get(x, 0) + 1

        has_single_left = False
        valid_cnt = 0
        for x in dict_s:
            cnt = dict_s[x]
            if cnt % 2 == 1:
                has_single_left = True
            valid_cnt += (cnt // 2)*2
        if has_single_left:
            valid_cnt += 1
        return valid_cnt



s = "abccccdd"
#
# 输出:
# 7

sol = Solution()
print('ret:',sol.longestPalindrome(s))



# dict_s = dict(s)
# print(dict_s)
