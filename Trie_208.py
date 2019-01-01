#TrieNode Demo


#leetcode 208
# 实现一个 Trie (前缀树)，包含 insert, search, 和 startsWith 这三个操作。
#
# 示例:
#
# Trie trie = new Trie();
#
# trie.insert("apple");
# trie.search("apple");   // 返回 true
# trie.search("app");     // 返回 false
# trie.startsWith("app"); // 返回 true
# trie.insert("app");
# trie.search("app");     // 返回 true
# 说明:
#
# 你可以假设所有的输入都是由小写字母 a-z 构成的。
# 保证所有输入均为非空字符串。



#不靠插入算法，手动构建一个Trie树先
TRIE_MAX_CHAR_NUM = 26

class TrieNode:
    def __init__(self):
        self.child = [None] * TRIE_MAX_CHAR_NUM
        self.is_end = False



#按层写逻辑有点乱，不如按字符串写
#abc\abcd\abd\b\bcd\efg
root = TrieNode()
#layer 1
l1_a = TrieNode()
l1_b = TrieNode()
l1_b.is_end = True
l1_e = TrieNode()
root.child[ord('a') - ord('a')] = l1_a
root.child[ord('b') - ord('a')] = l1_b
root.child[ord('e') - ord('a')] = l1_e
print(root.child)

#layer 2
l2_b = TrieNode()
l2_c = TrieNode()
l2_f = TrieNode()
l1_a.child[ord('b') - ord('a')] = l2_b
l1_b.child[ord('c') - ord('a')] = l2_c
l1_e.child[ord('f') - ord('a')] = l2_f

#layer 3

l3_c = TrieNode()
l3_d = TrieNode()
l3_d2 = TrieNode()
l3_g = TrieNode()

l2_b.child[ord('c') - ord('a')] = l3_c
l2_b.child[ord('d') - ord('a')] = l3_d
l2_c.child[ord('d') - ord('a')] = l3_d2
l2_f.child[ord('g') - ord('a')] = l3_g


l3_c.is_end = True
l3_d.is_end = True
l3_d2.is_end = True
l3_g.is_end = True

#layer 4
l4_d = TrieNode()
l3_c.child[ord('d') - ord('a')] = l4_d
l4_d.is_end = True


def preorder_trie(root,layer):
    for i in range(TRIE_MAX_CHAR_NUM):
        if root.child[i]:
            for j in range(layer):
                print('---',end='')
            print(chr(ord('a') + i),end='')
            if root.child[i].is_end:
                print('(end)',end='')
            print()
            preorder_trie(root.child[i],layer + 1)


preorder_trie(root,0)


def get_all_word_from_trie(root,stack,result):
    # stack = []
    # result = []#from stack

    for i in range(TRIE_MAX_CHAR_NUM):
        if root.child[i]:
            stack.append(chr(ord('a')+i))
            get_all_word_from_trie(root.child[i],stack,result)
            stack.pop()
    if root.is_end:
        # print('is end')
        result.append([stack[i] for i in range(len(stack))])
        # print('result is ',result)


stack = []
result = []
get_all_word_from_trie(root, stack, result)
print(result)

stack = ['a', 'b', 'c']
result = []
result.append([stack[i] for i in range(len(stack))])
stack = ['a', 'b', 'c', 'd']
result.append([stack[i] for i in range(len(stack))])
print(result)
print(result[0])
print(str(result[0]))
s = ''
for i in range(len(result[0])):
    s += result[0][i]
print('s is:', s)
s = s[:-1]
print('s is ', s)



# 想要结果是正常的字符串，stack就得用字符串操作了，
def get_all_word_from_trie_v2(root,stack,result):
    for i in range(TRIE_MAX_CHAR_NUM):
        if root.child[i]:
            stack += chr(ord('a')+i)
            get_all_word_from_trie_v2(root.child[i],stack,result)
            stack = stack[:-1]
    if root.is_end:
        result.append(stack)

stack = ''
result = []
get_all_word_from_trie_v2(root,stack,result)
print(result)

#或者把第一个版本的list做一个什么转换？''.join(stack)
#DFS
def get_all_word_from_trie_v3(root,stack,result):
    for i in range(TRIE_MAX_CHAR_NUM):
        if root.child[i]:
            stack.append(chr(ord('a')+i))
            get_all_word_from_trie_v3(root.child[i],stack,result)
            stack.pop()
    if root.is_end:
        result.append(''.join(stack))


stack = []
result = []
get_all_word_from_trie_v3(root, stack, result)
print('result is :',result)



#一个trie树的基本模型
#先不考虑数据结构的批量管理和删除，不做那个容器。
class TrieTree(object):
    def __init__(self):
        self.root = TrieNode()
        # return self.root
    def get_root(self):
        return self.root
    def preorder_trie(self, layer=0):
        for i in range(TRIE_MAX_CHAR_NUM):
            if self.root.child[i]:
                for j in range(layer):
                    print('---', end='')
                print(chr(ord('a') + i), end='')
                if self.root.child[i].is_end:
                    print('(end)', end='')
                print()
                self.preorder_trie(self.root.child[i], layer + 1)

    def get_all_word_from_trie(self, stack, result):
        self.__get_all_word_from_trie(self.root,stack,result)#把独立函数复制到类中，再把原来函数的root直接改成self.root来递归就不正确了，所以先套一层
    def __get_all_word_from_trie(self,root, stack, result):#这个root只是子树root，习惯而已，要不就叫node
        for i in range(TRIE_MAX_CHAR_NUM):
            if root.child[i]:
                stack.append(chr(ord('a') + i))
                self.__get_all_word_from_trie(root.child[i], stack, result)
                stack.pop()
        if root.is_end:
            result.append(''.join(stack))
    def insert(self,word):
        ptr = self.root
        n = len(word)
        for i in range(n):
            if not ptr.child[ord(word[i]) - ord('a')]:
                ptr.child[ord(word[i]) - ord('a')] = self.__new_node()
            ptr = ptr.child[ord(word[i]) - ord('a')]
        ptr.is_end = True

    def search(self,word):
        ptr = self.root
        n = len(word)
        for i in range(n):
            if not ptr.child[ord(word[i]) - ord('a')]:
                return False
            ptr = ptr.child[ord(word[i]) - ord('a')]
        return ptr.is_end
    def starsWith(self,prefix):
        ptr = self.root
        n = len(prefix)
        for i in range(n):
            if not ptr.child[ord(prefix[i]) - ord('a')]:
                return False
            ptr = ptr.child[ord(prefix[i]) - ord('a')]
        return True
    def __new_node(self):
        # print('new node')
        return TrieNode()



tree = TrieTree()
print('the tree is :',tree)
print('the root is :',tree.get_root())
# tree.__new_node()


result = []
stack = []
tree.insert('hello')
tree.insert('hellb')
tree.insert('abcd')
tree.preorder_trie()
tree.get_all_word_from_trie(stack,result)
print('result:',result)
print('search result:',tree.search('hello'))
print('search result:',tree.search('hellc'))
print('search result:',tree.search('abcd'))
print('search result:',tree.search('abc'))
print('starsWith result:',tree.starsWith('abc'))
print('starsWith result:',tree.starsWith('abcd'))
print('starsWith result:',tree.starsWith('hel'))
print('starsWith result:',tree.starsWith('hd'))



# #他这个是用dict实现的动态扩展，不是用的写死的数组，每一层都是如此。
#快在哪？因为是动态增长的node，动态创建的这些node，越大就越费时间，是吧？
#虽然我也可以认为dict也不一定就小，但是自动dict和手动dict肯定不一样，手动dict其实就等于创建数组了，比如这26个字母,自动dict被优化了，没办法！
class Trie:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.root = dict()
        self.word_end = -1  # key -1: True###然后也用字典的约定key作为结束标记

    def insert(self, word):
        """
        Inserts a word into the trie.
        :type word: str
        :rtype: void
        """
        cur_node = self.root
        for c in word:
            if c not in cur_node:
                cur_node[c] = dict()
            cur_node = cur_node[c]
        cur_node[self.word_end] = True

    def search(self, word):
        """
        Returns if the word is in the trie.
        :type word: str
        :rtype: bool
        """
        cur_node = self.root
        for c in word:
            if c not in cur_node:
                return False
            cur_node = cur_node[c]
        if self.word_end not in cur_node:
            return False
        return True

    def startsWith(self, prefix):
        """
        Returns if there is any word in the trie that starts with the given prefix.
        :type prefix: str
        :rtype: bool
        """
        cur_node = self.root
        for c in prefix:
            if c not in cur_node:
                return False
            cur_node = cur_node[c]
        return True




#证明dict更“快”，但是这个证明也不完整，只是证明创建数组是要花时间的。
#实际操作中，随着dict插入数量的增长，时间也不少，但是问题是，可能题目给的测试用例没怎么庞大！！！
import time
start = time.time()
a = dict()
end = time.time()
print(end-start)

start = time.time()
a = [0] * TRIE_MAX_CHAR_NUM
end = time.time()
print(end-start)

start = time.time()
a = [0] * 1000000
end = time.time()
print('list1:',end-start)

start = time.time()
a = [0 for i in range(1000000)]
end = time.time()
print('list2:',end-start)


start = time.time()
a = []
for i in range(1000000):
    a.append(i)
end = time.time()
print('list3:',end-start)

start = time.time()
a = dict()
for i in range(1000000):
    a[i] = i
end = time.time()
print('dict:',end-start)

