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


#############################################################################################################
#############################################################################################################
#############################################################################################################
#############################################################################################################
# 给定一种 pattern(模式) 和一个字符串 str ，判断 str 是否遵循相同的模式。
#
# 这里的遵循指完全匹配，例如， pattern 里的每个字母和字符串 str 中的每个非空单词之间存在着双向连接的对应模式。
#


# 这个是做映射，我的思路是用dict[dog]=a的形式来存，str遍历，遇到一个新词，词典没有则插入，有则查询，看一下pattern是否对应。
# 但是单向的映射好像不够，或者还需要遍历？如果是dict[dog] = a的形式，那我新来的dict[fish]也是插入，结果又插了a，还不认为算错。
# 反过来，同理，dict[a]=dog，那么再遇到dict[c]=dog也是插入，实际错了吧
# 双向词典才能解决了吧？

class Solution(object):
    def wordPattern(self, pattern, str):
        words = str.split(' ')

        print('words:',words)
        print('len:',len(words))
        if len(pattern) != len(words):
            return False
        dict_p = {}
        dict_s = {}
        for i in range(len(words)):
            print('pattern and words:',pattern[i],words[i])
            # 这不适合用get(k,0)==0这个形式了，存的不是数值，这不是计数器,最好还是用None来区分
            if dict_p.get(pattern[i]) == None and dict_s.get(words[i]) == None:#查找也必须两个词典都查了才能算
                dict_p[pattern[i]] = words[i]
                dict_s[words[i]] = pattern[i]
            else:#pattern found
                if dict_p.get(pattern[i]) == words[i] and dict_s.get(words[i]) == pattern[i]:
                    pass
                else:
                    return False
            print('p:',dict_p)
            print('s:',dict_s)

        return True




#意思一样，就是方法略不同。这个128长的数组，也相当于手动做了一个字符串的哈希集，虽然不是哈希映射
#网课的思路借用了一个used数组，单向字典+used数组，如果想给字典更新，必须不是used，但是他这个按理说复杂度不好，这不是个遍历吗？
# 原来used也可以直接访问，used设置128，dict映射存的内容是字符，，每个具体字符已经固定好了在used中的位置。


# 他的逻辑是单向映射:1.如果没有这个映射，好说，加上。2.如果有这个映射，查询到映射的pattern对不对。
# 但是1.这个情况还要额外加一个条件，虽然从单词出发查不到那个pattern，但是pattern依然可能存在，这算是没直接查pattern对应的word是谁，但是也算佐证，如果pattern已经占用了，说明有一个其他词，肯定不是当前word,占用了。
class Solution(object):
    def wordPattern(self, pattern, str):
        words = str.split(' ')
        print('words:',words)
        print('len:',len(words))
        if len(pattern) != len(words):
            return False
        dict_p = {}
        used = 128*[0]
        for i in range(len(words)):
            print('pattern and words:',pattern[i],words[i])

            if dict_p.get(words[i]) == None:
                if used[ord(pattern[i])] != 0:#没有这个词，但有这个模式
                    return False
                dict_p[words[i]] = pattern[i]
                used[ord(pattern[i])] = 1
            else:#pattern found
                print('else')
                print(used[ord(dict_p.get(words[i]))])
                print(pattern[i])
                if dict_p.get(words[i]) != pattern[i]:
                    return False
                else:
                    pass
            print('p:',dict_p)
            print('used:',used)

        return True

pattern = "abba"
str = "dog cat cat dog"

# pattern = "ab"
# str = "dog dog"
pattern = "abba"
str = "dog cat cat fish"
# pattern = ""
# str = "beef"

# 输出: true
sol = Solution()
print('ret:',sol.wordPattern(pattern,str))


test = 128*[0]
test[ord('a')] = 5
test[ord('9')] = 5
test[ord('8')] = 5
test[ord('7')] = 5
print(test)



